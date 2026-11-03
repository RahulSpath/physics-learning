"""From a raw spectrum to energy levels.

Reads the mercury-cadmium-argon lamp spectrum in ../data/hg-cd-ar-lamp-spectrum.csv,
finds every line, measures its centre, identifies the cadmium and mercury lines,
and uses the Ritz combination principle to recover the energy levels of the
ns np 3P terms of cadmium and mercury.

Needs Python 3 and NumPy. If matplotlib is installed, it also plots the spectrum.
Run it with:  python raw_spectrum_to_levels.py
"""
import os

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "..", "data", "hg-cd-ar-lamp-spectrum.csv")
CLIP = 9990.0  # the four brightest lines are clipped at 10 000 counts

# Reference vacuum wavelengths in angstrom (NIST, as compiled in PypeIt).
# Each entry: (upper level, lower level).
REFERENCE = {
    3261.9951: ("Cd", "5s5p 3P1", "5s2 1S0"),
    4679.4587: ("Cd", "5s6s 3S1", "5s5p 3P0"),
    4801.2540: ("Cd", "5s6s 3S1", "5s5p 3P1"),
    5087.2393: ("Cd", "5s6s 3S1", "5s5p 3P2"),
    4047.7080: ("Hg", "6s7s 3S1", "6s6p 3P0"),
    4359.5600: ("Hg", "6s7s 3S1", "6s6p 3P1"),
    5462.2680: ("Hg", "6s7s 3S1", "6s6p 3P2"),
}

# NIST energy levels (cm^-1), used only to check the results at the end.
NIST = {
    "Cd 5s5p 3P0": 30113.990,
    "Cd 5s5p 3P1": 30656.087,
    "Cd 5s5p 3P2": 31826.952,
    "Cd 5s6s 3S1": 51483.980,
    "Hg 3P1 - 3P0": 1767.220,
    "Hg 3P2 - 3P1": 4630.677,
}


def load_spectrum(path=DATA):
    data = np.loadtxt(path, delimiter=",", comments="#", skiprows=6)
    return data[:, 0], data[:, 1]


def find_lines(wave, flux, fraction=0.002):
    """Local maxima higher than a fraction of the brightest line."""
    baseline = np.percentile(flux, 20)
    threshold = baseline + fraction * (flux.max() - baseline)
    peaks = []
    for i in range(2, len(flux) - 2):
        if (flux[i] > threshold and flux[i] >= flux[i - 1] and flux[i] > flux[i + 1]
                and flux[i] >= flux[i - 2] and flux[i] > flux[i + 2]):
            peaks.append(i)
    return peaks


def fit_line(wave, flux, i):
    """Fit a Gaussian to the top of a line: a parabola through log(intensity).

    Clipped pixels are left out. Returns the centre and the full width at half
    maximum, both in angstrom.
    """
    sel = [j for j in range(i - 5, i + 6)
           if 0 <= j < len(flux) and 0.15 * flux[i] < flux[j] < CLIP]
    x = wave[sel] - wave[i]
    c2, c1, _ = np.polyfit(x, np.log(flux[sel]), 2)
    centre = wave[i] - c1 / (2 * c2)
    fwhm = 2.3548 * np.sqrt(-1 / (2 * c2)) if c2 < 0 else float("nan")
    return centre, fwhm


def wavenumber(wavelength_angstrom):
    """Vacuum wavelength in angstrom -> wavenumber in cm^-1."""
    return 1e8 / wavelength_angstrom


def main():
    wave, flux = load_spectrum()
    print(f"Spectrum: {len(wave)} points, {wave.min():.0f} to {wave.max():.0f} angstrom (vacuum)")

    # Step 1: find the lines
    peaks = find_lines(wave, flux)
    print(f"\nStep 1. Lines above 0.2% of the brightest: {len(peaks)}")

    # Step 2: measure each line; Step 3: identify the ones we need
    print("\nSteps 2 and 3. Line centres and identifications")
    print(f"{'centre (A)':>11} {'height':>8} {'FWHM (A)':>9}  identification")
    measured = {}
    for i in peaks:
        centre, fwhm = fit_line(wave, flux, i)
        ref = min(REFERENCE, key=lambda r: abs(r - centre))
        if abs(ref - centre) < 1.5:
            atom, upper, lower = REFERENCE[ref]
            label = f"{atom}: {upper} -> {lower}  (reference {ref:.2f})"
            measured[ref] = (centre, flux[i], fwhm)
        else:
            label = ""
        print(f"{centre:11.2f} {flux[i]:8.0f} {fwhm:9.2f}  {label}")

    # Step 4: the Ritz combination principle
    sigma = {ref: wavenumber(m[0]) for ref, m in measured.items()}
    print("\nStep 4. Wavenumber differences of lines from a shared upper level (cm^-1)")
    cd_10 = sigma[4679.4587] - sigma[4801.2540]
    cd_21 = sigma[4801.2540] - sigma[5087.2393]
    hg_10 = sigma[4047.7080] - sigma[4359.5600]
    hg_21 = sigma[4359.5600] - sigma[5462.2680]
    print(f"  Cd 3P1 - 3P0 = {cd_10:7.1f}   (NIST {NIST['Cd 5s5p 3P1'] - NIST['Cd 5s5p 3P0']:.1f})")
    print(f"  Cd 3P2 - 3P1 = {cd_21:7.1f}   (NIST {NIST['Cd 5s5p 3P2'] - NIST['Cd 5s5p 3P1']:.1f})")
    print(f"  Hg 3P1 - 3P0 = {hg_10:7.1f}   (NIST {NIST['Hg 3P1 - 3P0']:.1f})")
    print(f"  Hg 3P2 - 3P1 = {hg_21:7.1f}   (NIST {NIST['Hg 3P2 - 3P1']:.1f})")

    # Step 5: build the cadmium levels, starting from the ground state
    p1 = sigma[3261.9951]          # 3P1 -> ground state
    s1 = p1 + sigma[4801.2540]     # 3S1 -> 3P1
    p0 = s1 - sigma[4679.4587]     # 3S1 -> 3P0
    p2 = s1 - sigma[5087.2393]     # 3S1 -> 3P2
    print("\nStep 5. Cadmium energy levels above the ground state (cm^-1)")
    for name, value in [("5s5p 3P0", p0), ("5s5p 3P1", p1), ("5s5p 3P2", p2), ("5s6s 3S1", s1)]:
        ref = NIST["Cd " + name]
        print(f"  {name}: {value:9.1f}   NIST {ref:9.1f}   difference {value - ref:+5.1f}")

    # Step 6: label the levels
    h = [measured[r][1] for r in (4679.4587, 4801.2540, 5087.2393)]
    print("\nStep 6. Checks on the labels")
    print(f"  Cd interval ratio (3P2-3P1)/(3P1-3P0) = {cd_21 / cd_10:.2f}  (Lande interval rule for J = 0, 1, 2: 2)")
    print(f"  Hg interval ratio                    = {hg_21 / hg_10:.2f}  (the rule fails: intermediate coupling)")
    print(f"  Cd triplet heights 3P0 : 3P1 : 3P2 = 1 : {h[1] / h[0]:.2f} : {h[2] / h[0]:.2f}  (LS line strengths 1 : 3 : 5)")
    print(f"  Resolving power near 480 nm: {measured[4801.2540][0] / measured[4801.2540][2]:.0f}")

    try:
        import matplotlib.pyplot as plt
    except ImportError:
        return
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.semilogy(wave / 10, np.clip(flux, 3, None), lw=0.8)
    ax.set_xlabel("Wavelength in vacuum (nm)")
    ax.set_ylabel("Intensity (arbitrary units)")
    ax.set_title("Mercury-cadmium-argon lamp spectrum")
    fig.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
