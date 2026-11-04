"""Illustrate equal-curvature displaced oscillators, not a fit to molecular data."""

from math import exp, factorial, sqrt
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


FIGURE = Path(__file__).resolve().parents[1] / "figures" / "franck-condon-model.svg"
S = 2.4
ELECTRONIC_OFFSET = 5.0  # In units of hbar * Omega; illustrative only


def main():
    plt.rcParams.update({"font.size": 11, "svg.fonttype": "none"})
    displacement = sqrt(2 * S)  # In oscillator lengths sqrt(hbar / (mu * Omega))
    x = np.linspace(-2.4, 5.6, 900)
    final_x = x - displacement
    initial_potential = x**2 / 2
    final_potential = ELECTRONIC_OFFSET + final_x**2 / 2
    initial_wavefunction = np.pi**(-0.25) * np.exp(-x**2 / 2)
    # Normalized Hermite oscillator state v'=2.
    final_wavefunction = (np.pi**(-0.25) / sqrt(8)
                          * (4 * final_x**2 - 2) * np.exp(-final_x**2 / 2))

    fig, (left, right) = plt.subplots(
        1, 2, figsize=(10.4, 4.9), gridspec_kw={"width_ratios": [1.25, 1]}
    )
    left.plot(x, initial_potential, color="#1f4e9c", lw=1.7, label="Initial potential")
    left.plot(x, final_potential, color="#2a7f62", lw=1.7, label="Final potential")
    left.hlines(0.5, -1, 1, color="#1f4e9c", lw=1)
    left.plot(x, 0.5 + 0.6 * initial_wavefunction, color="#1f4e9c", lw=1.4)
    for v in range(5):
        energy = ELECTRONIC_OFFSET + v + 0.5
        radius = sqrt(2 * v + 1)
        left.hlines(energy, displacement - radius, displacement + radius,
                    color="#7f8794", lw=0.8)
        if v < 4:
            left.text(displacement + radius + 0.08, energy, f"v'={v}", fontsize=9,
                      va="center")
    final_energy = ELECTRONIC_OFFSET + 2.5
    left.plot(x, final_energy + 0.6 * final_wavefunction, color="#2a7f62", lw=1.4)
    left.annotate("", xy=(0, ELECTRONIC_OFFSET + S), xytext=(0, 0),
                  arrowprops={"arrowstyle": "->", "color": "#b5561f", "lw": 1.7})
    left.text(-0.22, 3.8, "same R", rotation=90, va="center", ha="right",
              color="#b5561f", fontsize=10)
    left.text(-1.8, 0.55, "v''=0", color="#1f4e9c", fontsize=9)
    left.set(xlim=(-2.4, 5.6), ylim=(-0.25, 11),
              xlabel=r"Bond displacement $(R-R_e'')/\ell$",
              ylabel=r"Energy / $\hbar\Omega$", title="Displaced potentials and nuclear amplitudes")
    left.legend(loc="upper left", frameon=False, fontsize=9)

    vibrational = np.arange(10)
    weights = np.array([exp(-S) * S**int(v) / factorial(int(v)) for v in vibrational])
    colors = ["#b5561f" if v == 2 else "#1f4e9c" for v in vibrational]
    right.bar(vibrational, weights, color=colors, width=0.72)
    right.set(xlabel=r"Final vibrational level $v'$", ylabel=r"Overlap factor $q_{v'0}$",
               title="Predicted Franck–Condon weights", xticks=[0, 2, 4, 6, 8],
               ylim=(0, 0.33))
    for ax in (left, right):
        ax.spines[["top", "right"]].set_visible(False)
    fig.text(0.5, 0.02,
             "Equal-curvature model; S = 2.4; initial v'' = 0. Calculated weights, not measured intensities.",
             ha="center", color="#5a6478", fontsize=10)
    fig.tight_layout(rect=(0, 0.055, 1, 1))
    FIGURE.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(FIGURE)
    plt.close(fig)


if __name__ == "__main__":
    main()
