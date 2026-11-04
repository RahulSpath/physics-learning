"""Inspect a processed PypeIt arc template and demonstrate conditional Ritz sums.

Python + NumPy are sufficient. Reference matches are candidates, not confirmed
identifications. No raw-count noise model or centroid uncertainty is supplied.
"""

import argparse
import csv
import hashlib
import json
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "hg-cd-ar-lamp-spectrum.csv"
REFERENCE = {
    3261.9951: ("Cd", "5s5p 3P1", "5s2 1S0"),
    4679.4587: ("Cd", "5s6s 3S1", "5s5p 3P0"),
    4801.2540: ("Cd", "5s6s 3S1", "5s5p 3P1"),
    5087.2393: ("Cd", "5s6s 3S1", "5s5p 3P2"),
    4047.7080: ("Hg", "6s7s 3S1", "6s6p 3P0"),
    4359.5600: ("Hg", "6s7s 3S1", "6s6p 3P1"),
    5462.2680: ("Hg", "6s7s 3S1", "6s6p 3P2"),
}
FIELDS = (
    "sample_peak_index", "sample_wavelength_angstrom", "peak_height",
    "centre_vacuum_angstrom", "fwhm_angstrom", "fit_status", "flags",
    "core_samples", "log_rms", "unconstrained_vertex_angstrom",
    "unconstrained_fwhm_angstrom", "reference_wavelength_angstrom",
    "species", "upper_level", "lower_level", "offset_from_reference_angstrom",
    "assignment_status",
)


def load_spectrum(path=DATA):
    values = np.loadtxt(path, delimiter=",", comments="#", skiprows=6)
    wave, signal = values[:, 0], values[:, 1]
    if not (np.all(np.isfinite(values)) and np.all(np.diff(wave) > 0)):
        raise ValueError("Expected finite samples in increasing wavelength order")
    return wave, signal


def find_lines(wave, signal, fraction=0.002):
    """Return local-max candidates; this relative threshold is not an S/N test."""
    if not 0 <= fraction < 1:
        raise ValueError("fraction must lie in [0, 1)")
    baseline = np.percentile(signal, 20)
    threshold = baseline + fraction * (signal.max() - baseline)
    return [i for i in range(2, len(signal) - 2)
            if signal[i] > threshold and signal[i] >= signal[i - 1]
            and signal[i] > signal[i + 1] and signal[i] >= signal[i - 2]
            and signal[i] > signal[i + 2]]


def fit_line(wave, signal, i, half_window=5):
    """Guarded Gaussian-core estimate; fit diagnostics are not formal errors.

    Continuum subtraction was done upstream. A residual background, blend or
    non-Gaussian instrument profile can bias this log-space approximation.
    Values at 10000 are valid normalization maxima and are INCLUDED.
    """
    flags = []
    if np.isclose(signal[i], 10000):
        flags.append("normalization_maximum")
    row = {"sample_peak_index": int(i), "sample_wavelength_angstrom": float(wave[i]),
           "peak_height": float(signal[i]), "centre_vacuum_angstrom": None,
           "fwhm_angstrom": None, "fit_status": "invalid", "flags": flags,
           "core_samples": 0, "log_rms": None,
           "unconstrained_vertex_angstrom": None, "unconstrained_fwhm_angstrom": None}
    if i < half_window or i + half_window >= len(signal):
        flags.append("window_reaches_spectrum_edge")
        return row
    window = np.arange(i - half_window, i + half_window + 1)
    core = window[(signal[window] > 0) & (signal[window] > 0.15 * signal[i])]
    row["core_samples"] = len(core)
    if len(core) < 4:
        flags.append("fewer_than_four_core_samples")
        return row
    x = wave[core] - wave[i]
    design = np.column_stack((x*x, x, np.ones_like(x)))
    coefficients, _, rank, _ = np.linalg.lstsq(design, np.log(signal[core]), rcond=None)
    if rank != 3:
        flags.append("rank_deficient_fit")
        return row
    c2, c1, _ = coefficients
    row["log_rms"] = float(np.sqrt(np.mean((design @ coefficients - np.log(signal[core]))**2)))
    if c2 >= 0:
        flags.append("nonnegative_curvature")
        return row
    centre = float(wave[i] - c1 / (2*c2))
    fwhm = float(2*np.sqrt(2*np.log(2))*np.sqrt(-1/(2*c2)))
    row["unconstrained_vertex_angstrom"] = centre
    row["unconstrained_fwhm_angstrom"] = fwhm
    if not wave[window[0]] <= centre <= wave[window[-1]]:
        flags.append("vertex_outside_fit_window")
        return row
    if fwhm > wave[window[-1]] - wave[window[0]]:
        flags.append("width_exceeds_fit_window")
        return row
    if abs(centre-wave[i]) > np.median(np.diff(wave[window])):
        flags.append("vertex_far_from_sample_peak")
        return row
    row.update(centre_vacuum_angstrom=centre, fwhm_angstrom=fwhm, fit_status="core_estimate")
    return row


def wavenumber(wavelength_angstrom):
    return 1e8 / wavelength_angstrom


def analyse(path=DATA, fraction=0.002):
    wave, signal = load_spectrum(path)
    candidates = [fit_line(wave, signal, i) for i in find_lines(wave, signal, fraction)]
    selected = {}
    for row in candidates:
        row.update(reference_wavelength_angstrom=None, species="", upper_level="",
                   lower_level="", offset_from_reference_angstrom=None,
                   assignment_status="not_compared_with_a_full_line_list")
        if row["centre_vacuum_angstrom"] is None:
            continue
        ref = min(REFERENCE, key=lambda value: abs(value-row["centre_vacuum_angstrom"]))
        offset = row["centre_vacuum_angstrom"]-ref
        if abs(offset) <= 1.5:
            species, upper, lower = REFERENCE[ref]
            row.update(reference_wavelength_angstrom=ref, species=species,
                       upper_level=upper, lower_level=lower,
                       offset_from_reference_angstrom=offset,
                       assignment_status="reference_candidate_not_confirmed")
            if ref not in selected or abs(offset) < abs(selected[ref]["offset_from_reference_angstrom"]):
                selected[ref] = row
    ritz = None
    if set(selected) == set(REFERENCE):
        sigma = {ref: wavenumber(row["centre_vacuum_angstrom"]) for ref, row in selected.items()}
        cd10 = sigma[4679.4587]-sigma[4801.2540]
        cd21 = sigma[4801.2540]-sigma[5087.2393]
        hg10 = sigma[4047.7080]-sigma[4359.5600]
        hg21 = sigma[4359.5600]-sigma[5462.2680]
        p1 = sigma[3261.9951]
        s1 = p1+sigma[4801.2540]
        ritz = {
            "status": "conditional_on_imported_assignments_and_archive_calibration",
            "independent_cycles": 0,
            "cadmium_intervals_cm_inverse": {"P1_minus_P0": cd10, "P2_minus_P1": cd21},
            "mercury_intervals_cm_inverse": {"P1_minus_P0": hg10, "P2_minus_P1": hg21},
            "cadmium_levels_cm_inverse": {"5s5p 3P0": s1-sigma[4679.4587],
                "5s5p 3P1": p1, "5s5p 3P2": s1-sigma[5087.2393], "5s6s 3S1": s1},
            "cadmium_interval_ratio": cd21/cd10, "mercury_interval_ratio": hg21/hg10,
        }
    summary = {
        "input": {"path": str(Path(path).name), "sha256": hashlib.sha256(Path(path).read_bytes()).hexdigest(),
                  "samples": len(wave), "wavelength_units": "vacuum angstrom",
                  "signal_units": "independently normalized archive segments",
                  "wavelength_range": [float(wave[0]), float(wave[-1])],
                  "median_sample_spacing_angstrom": float(np.median(np.diff(wave)))},
        "method": {"relative_threshold": fraction, "half_window_samples": 5,
                   "core_fraction": 0.15, "reference_tolerance_angstrom": 1.5,
                   "formal_centroid_uncertainties": None,
                   "notes": ["10000 maxima arise from normalization, not established saturation",
                     "A core estimate is not a validated single-line profile",
                     "Only seven selected references are considered; legacy full-list IDs are not reproduced",
                     "No independent wavelength calibration or intensity-response calibration is supplied"]},
        "counts": {"local_maximum_candidates": len(candidates),
                   "core_estimates": sum(row["fit_status"] == "core_estimate" for row in candidates),
                   "invalid_core_fits": sum(row["fit_status"] == "invalid" for row in candidates),
                   "selected_reference_candidates": len(selected),
                   "normalization_maxima": int(np.isclose(signal, 10000).sum())},
        "selected_candidates": [selected[ref] for ref in sorted(selected)], "ritz_demo": ritz,
    }
    return candidates, summary


def export_report(directory, candidates, summary):
    directory = Path(directory)
    directory.mkdir(parents=True, exist_ok=True)
    with (directory / "candidate-lines.csv").open("w", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=FIELDS)
        writer.writeheader()
        for row in candidates:
            writer.writerow({**row, "flags": "|".join(row["flags"])})
    (directory / "analysis-summary.json").write_text(json.dumps(summary, indent=2, allow_nan=False)+"\n")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--no-plot", action="store_true", help="Print results without an interactive plot")
    parser.add_argument("--output-dir", type=Path, help="Explicitly export CSV diagnostics and JSON summary")
    parser.add_argument("--fraction", type=float, default=0.002, help="Relative candidate threshold, not S/N")
    args = parser.parse_args()
    candidates, summary = analyse(fraction=args.fraction)
    print("Processed wavelength-calibration template; reference matches remain candidates.")
    print(json.dumps(summary["counts"], indent=2))
    for row in summary["selected_candidates"]:
        print(f"{row['centre_vacuum_angstrom']:.4f} A  {row['species']} candidate  "
              f"FWHM {row['fwhm_angstrom']:.3f} A; flags: {','.join(row['flags']) or 'none'}")
    if summary["ritz_demo"]:
        print("Conditional Ritz reconstruction (no independent closure or formal errors):")
        print(json.dumps(summary["ritz_demo"], indent=2))
    if args.output_dir:
        export_report(args.output_dir, candidates, summary)
    if not args.no_plot:
        import matplotlib.pyplot as plt
        wave, signal = load_spectrum()
        plt.plot(wave/10, signal, lw=0.8)
        plt.xlabel("Vacuum wavelength (nm)")
        plt.ylabel("Processed archive signal (arbitrary units)")
        plt.title("Empirical Hg–Cd–Ar calibration template")
        plt.tight_layout()
        plt.show()


if __name__ == "__main__":
    main()
