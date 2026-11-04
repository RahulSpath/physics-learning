"""Compare tabulated experimental CO centres with a one-line rigid-rotor prediction."""

import csv
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "co-rotational-jpl" / "reference-lines.csv"
FIGURE = ROOT / "figures" / "co-rotational-test.svg"


def main():
    with DATA.open(newline="") as stream:
        rows = list(csv.DictReader(stream))
    upper_j = np.array([int(row["j_upper"]) for row in rows])
    measured = np.array([float(row["frequency_mhz"]) for row in rows])
    uncertainty = np.array([float(row["listed_uncertainty_mhz"]) for row in rows])

    # Only the first experimental centre determines this model parameter.
    b_mhz = measured[0] / 2
    predicted = 2 * b_mhz * upper_j
    residual = measured - predicted
    plt.rcParams.update(
        {"font.size": 11, "svg.fonttype": "none", "axes.spines.top": False,
         "axes.spines.right": False}
    )
    fig, axes = plt.subplots(1, 2, figsize=(10, 4.8))
    left, right = axes
    left.plot(upper_j, predicted / 1000, "--", color="#b5561f", linewidth=1.8,
              label="Rigid rotor: first centre sets B")
    left.errorbar(upper_j[1:], measured[1:] / 1000, yerr=uncertainty[1:] / 1000,
                  fmt="o", color="#1f2633", capsize=3, label="Unused experimental centres")
    left.plot(upper_j[0], measured[0] / 1000, "o", color="#7f8794",
              label="Calibration centre")
    left.set(title="Tabulated experimental frequencies", ylabel="Transition frequency (GHz)")
    left.legend(loc="upper left", fontsize=8.5, frameon=False)

    right.axhline(0, color="#7f8794", linewidth=1, linestyle="--")
    right.plot(upper_j[0], residual[0], "o", color="#7f8794")
    right.errorbar(upper_j[1:], residual[1:], yerr=uncertainty[1:], fmt="o",
                   color="#1f2633", capsize=3)
    for j, offset in zip(upper_j[1:], residual[1:]):
        right.annotate(f"{offset:.4f} MHz", (j, offset), xytext=(0, 10),
                       textcoords="offset points", ha="center", fontsize=10)
    right.set(title="Measured minus rigid-rotor prediction", ylabel="Frequency residual (MHz)",
               ylim=(-20.5, 2.8))
    for ax in axes:
        ax.set(xlabel=r"Upper rotational quantum number $J$", xlim=(0.7, 3.3),
               xticks=upper_j)
        ax.grid(alpha=0.2)
    fig.suptitle(r"$^{12}$C$^{16}$O: testing the next rotational lines", fontsize=13)
    fig.text(0.5, 0.055,
             "Points are tabulated experimental centres, not an intensity trace. Bars: listed frequency uncertainties only.",
             ha="center", fontsize=9, color="#5a6478")
    fig.text(0.5, 0.018,
             "Calibration uncertainty and correlations are not propagated; bars are smaller than symbols.",
             ha="center", fontsize=9, color="#5a6478")
    fig.tight_layout(rect=(0, 0.10, 1, 0.94))
    FIGURE.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(FIGURE)
    plt.close(fig)


if __name__ == "__main__":
    main()
