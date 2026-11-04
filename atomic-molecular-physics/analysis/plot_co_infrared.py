"""Plot the supplied, processed NIST CO transmission record without new fitting."""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "co-infrared-nist" / "original-spectrum.jdx"
FIGURE = ROOT / "figures" / "co-infrared-measured.svg"


def read_spectrum(path):
    """Decode this file's uncompressed numeric X++(Y..Y) data rows."""
    header = {}
    x_values, y_values = [], []
    in_data = False
    for line in path.read_text(encoding="latin1").splitlines():
        if line.startswith("$$") or not line.strip():
            continue
        if line.startswith("##"):
            key, value = line[2:].split("=", 1)
            header[key] = value
            in_data = key == "XYDATA"
            if in_data and value != "(X++(Y..Y))":
                raise ValueError("Unexpected JCAMP data representation")
            continue
        if in_data:
            row = [float(value) for value in line.split()]
            x_factor = float(header["XFACTOR"])
            y_factor = float(header["YFACTOR"])
            delta_x = float(header["DELTAX"])
            x_values.extend((row[0] * x_factor + delta_x * np.arange(len(row) - 1)).tolist())
            y_values.extend(value * y_factor for value in row[1:])
    x = np.asarray(x_values)
    y = np.asarray(y_values)
    if len(x) != int(header["NPOINTS"]):
        raise ValueError("JCAMP point count does not match its header")
    if header["XUNITS"] != "1/CM" or header["YUNITS"] != "TRANSMITTANCE":
        raise ValueError("Unexpected spectrum units")
    if not np.all(np.diff(x) > 0):
        raise ValueError("Source wavenumbers must be increasing")
    return x, y, header


def main():
    x, transmission, _ = read_spectrum(DATA)
    window = (x >= 1900) & (x <= 2300)
    plt.rcParams.update({"font.size": 11, "svg.fonttype": "none"})
    fig, ax = plt.subplots(figsize=(9.3, 4.6))
    ax.plot(x[window], transmission[window], color="#1f2633", linewidth=1.4)
    ax.set(xlim=(1900, 2300), ylim=(0, 1.08),
           xlabel=r"Wavenumber (cm$^{-1}$)", ylabel="Transmittance",
           title="CO infrared transmission: processed measured reference record")
    ax.spines[["top", "right"]].set_visible(False)
    ax.grid(alpha=0.18)
    fig.text(0.5, 0.065,
             "Gas-phase CO; listed resolution 4 cm⁻¹. Congested rotational structure was smoothed upstream.",
             ha="center", fontsize=9, color="#5a6478")
    fig.text(0.5, 0.025,
             "NIST/Coblentz No. 8755 (1964), digitized from hardcopy. Supplied transmittance plotted directly.",
             ha="center", fontsize=9, color="#5a6478")
    fig.tight_layout(rect=(0, 0.11, 1, 1))
    FIGURE.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(FIGURE)
    plt.close(fig)


if __name__ == "__main__":
    main()
