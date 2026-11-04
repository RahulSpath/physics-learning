"""Plot two measured MPQ hydrogen excitation scans; see the data README."""

import csv
from decimal import Decimal
import json
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "hydrogen-2s-6p-mpq"
C_CM_S = 29_979_245_800  # Exact speed of light, in cm/s.


def main():
    provenance = json.loads((DATA / "provenance.json").read_text())
    reference = Decimal(provenance["reference_hz"])
    all_points = []
    scans = []
    for scan in provenance["scans"]:
        offset = Decimal(scan["unblind_offset_hz"])
        points = []
        with (DATA / scan["file"]).open(newline="") as stream:
            for line, row in enumerate(csv.DictReader(stream), start=2):
                # Preserve every measured point, including repeat centre readings.
                # Subtract a shared origin; never align scans by fitting their peaks.
                relative_hz = float(Decimal(row["Freq_Blind"]) + offset - reference)
                counts = int(row[provenance["count_column"]])
                point = {
                    "scan": scan["group"],
                    "source_csv_line": line,
                    "relative_frequency_mhz": relative_hz / 1e6,
                    "relative_wavenumber_cm-1": relative_hz / C_CM_S,
                    "detector_counts": counts,
                    "expected_shot_noise_counts": float(np.sqrt(counts)),
                }
                points.append(point)
                all_points.append(point)
        scans.append(sorted(points, key=lambda p: p["relative_frequency_mhz"]))

    with (DATA / "plotted-points.csv").open("w", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(all_points[0]))
        writer.writeheader()
        writer.writerows(all_points)

    plt.rcParams.update({"font.size": 11, "svg.fonttype": "none"})
    fig, ax = plt.subplots(figsize=(9.5, 4.3), layout="constrained")
    colours = ["#1f4e9c", "#b5561f"]
    for i, points in enumerate(scans):
        x = np.array([p["relative_wavenumber_cm-1"] for p in points])
        y = np.array([p["detector_counts"] for p in points])
        ax.errorbar(
            x, y / 1000, yerr=np.sqrt(y) / 1000,
            fmt="o", markersize=3.4, elinewidth=0.9, capsize=2,
            color=colours[i], label=f"Measured scan {i + 1}",
        )

    left_edge = max(p["relative_wavenumber_cm-1"] for p in scans[0])
    right_edge = min(p["relative_wavenumber_cm-1"] for p in scans[1])
    ax.axvspan(left_edge, right_edge, color="#eef0f3", zorder=-1)
    ax.text((left_edge + right_edge) / 2, 1.5, "Not scanned", ha="center", color="#606773")
    ax.set(
        xlabel=r"Relative wavenumber $\tilde\nu-\tilde\nu_{\rm ref}$ (cm$^{-1}$)",
        ylabel=r"Fluorescence signal ($10^3$ detector counts)",
        title="Hydrogen Hδ: measured excitation scans",
        xlim=(-0.0022, 0.0158), ylim=(-0.08, 4.0),
        xticks=[0, 0.005, 0.010, 0.015],
    )
    top = ax.secondary_xaxis(
        "top", functions=(lambda x: x * C_CM_S / 1e6, lambda f: f * 1e6 / C_CM_S)
    )
    top.set_xlabel("Relative excitation frequency (MHz)")
    top.set_xticks([0, 100, 200, 300, 400])
    ax.spines[["top", "right"]].set_visible(False)
    ax.grid(axis="y", color="#e6e8ec", linewidth=0.6)
    ax.legend(loc="upper center", frameon=False, ncol=2)

    figure = ROOT / "figures" / "hydrogen-2s-6p-measured.svg"
    fig.savefig(figure, metadata={"Creator": "MPQ measured data; plot by physics-learning"})
    plt.close(fig)
    print(f"Plotted {len(all_points)} measured points: {figure}")


if __name__ == "__main__":
    main()
