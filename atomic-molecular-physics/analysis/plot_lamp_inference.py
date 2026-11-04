"""Plot the processed lamp archive and its explicitly conditional reconstruction."""

import hashlib
import json
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

from raw_spectrum_to_levels import DATA, load_spectrum

ROOT = Path(__file__).resolve().parents[1]
FIGURES = ROOT / "figures"
REPORT = ROOT / "data/lamp-analysis/analysis-summary.json"


def finish(fig, name, note):
    fig.text(0.5, 0.02, note, ha="center", color="#5a6478", fontsize=9)
    fig.tight_layout(rect=(0, 0.065, 1, 1))
    fig.savefig(FIGURES / name)
    plt.close(fig)


def main():
    plt.rcParams.update({"font.size": 11, "svg.fonttype": "none"})
    report = json.loads(REPORT.read_text())
    if hashlib.sha256(DATA.read_bytes()).hexdigest() != report["input"]["sha256"]:
        raise ValueError("Recompute the analysis report for this source file")
    wave, signal = load_spectrum()
    wavelength = wave / 10
    fig, ax = plt.subplots(figsize=(10, 4.5))
    ax.plot(wavelength, np.where(signal > 0, signal, np.nan), color="#1f2633", lw=0.7)
    ax.set(yscale="log", xlabel="Vacuum wavelength (nm)",
           ylabel="Archive signal (arbitrary units)",
           title="Processed Hg–Cd–Ar wavelength-calibration template",
           xlim=(wavelength[0], wavelength[-1]))
    ax.spines[["top", "right"]].set_visible(False)
    finish(fig, "lamp-template-overview.svg",
           "Empirical, continuum-subtracted and separately normalized segments. Log display omits nonpositive samples.")

    fig, ax = plt.subplots(figsize=(10, 4.5))
    ax.plot(wavelength, signal, color="#1f2633", lw=0.9)
    for cut in (430, 530):
        ax.axvline(cut, color="#7f8794", ls=":", lw=1)
        ax.text(cut+1, 11500, "nominal stitch", color="#5a6478", fontsize=8)
    for row in report["selected_candidates"]:
        centre = row["centre_vacuum_angstrom"] / 10
        if not 400 < centre < 550:
            continue
        color = "#b5561f" if row["species"] == "Cd" else "#1f4e9c"
        ax.annotate(f"{row['species']}? {centre:.2f}",
                    (centre, row["peak_height"]), xytext=(3, 12),
                    textcoords="offset points", rotation=90, va="bottom", fontsize=9, color=color)
    ax.set(xlim=(400, 550), ylim=(-100, 14500), xlabel="Vacuum wavelength (nm)",
           ylabel="Archive signal (arbitrary units)", title="Selected reference candidates in the archive")
    ax.spines[["top", "right"]].set_visible(False)
    finish(fig, "lamp-candidate-features.svg",
           "Labels are imported candidates. Maxima at 10000 come from segment normalization, not established saturation.")

    levels = report["ritz_demo"]["cadmium_levels_cm_inverse"]
    by_ref = {row["reference_wavelength_angstrom"]: row for row in report["selected_candidates"]}
    fig, ax = plt.subplots(figsize=(9, 4.9))
    layout = [(0.4, "5s² ¹S₀", 0), (2.1, "5s5p ³P₀", levels["5s5p 3P0"]),
              (2.9, "5s5p ³P₁", levels["5s5p 3P1"]),
              (3.7, "5s5p ³P₂", levels["5s5p 3P2"]),
              (5.6, "5s6s ³S₁", levels["5s6s 3S1"])]
    for y, label, energy in layout:
        ax.hlines(y, 1, 4.3, color="#1f2633", lw=1.8)
        ax.text(4.45, y, f"{label}   {energy:.0f} cm⁻¹", va="center", fontsize=11)
    for x, upper, lower, ref in [(1.4, 5.6, 2.1, 4679.4587),
                                  (2.65, 5.6, 2.9, 4801.2540),
                                  (3.9, 5.6, 3.7, 5087.2393),
                                  (2.65, 2.9, 0.4, 3261.9951)]:
        ax.annotate("", (x, lower), (x, upper),
                    arrowprops={"arrowstyle": "->", "lw": 1.5, "color": "#b5561f"})
        nm = by_ref[ref]["centre_vacuum_angstrom"] / 10
        ax.text(x-0.12, (upper+lower)/2, f"{nm:.2f} nm", rotation=90,
                ha="right", va="center", fontsize=9, color="#b5561f")
    ax.set(xlim=(0.3, 8.2), ylim=(-0.1, 6.2), title="Conditional cadmium Ritz reconstruction")
    ax.axis("off")
    finish(fig, "cadmium-ritz-reconstruction.svg",
           "Schematic, not to scale. Imported assignments; rounded energies are not precision claims. Four edges, no closed cycle.")


if __name__ == "__main__":
    main()
