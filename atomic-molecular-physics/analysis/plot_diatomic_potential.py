"""Illustrate a Morse well, its harmonic limit and nuclear zero-point energy."""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


FIGURE = Path(__file__).resolve().parents[1] / "figures" / "diatomic-potential-model.svg"
A_RE = 2.5
HBAR_OMEGA_OVER_DE = 0.2


def main():
    plt.rcParams.update({"font.size": 11, "svg.fonttype": "none"})
    r = np.linspace(0.55, 3.15, 700)  # R / R_e
    morse = (1 - np.exp(-A_RE * (r - 1))) ** 2
    harmonic = (A_RE * (r - 1)) ** 2
    fig, ax = plt.subplots(figsize=(8.8, 4.8))
    ax.plot(r, morse, color="#1f2633", lw=2, label="Morse potential")
    ax.plot(r, harmonic, color="#b5561f", ls="--", lw=1.7,
            label="Local harmonic approximation")
    eta = HBAR_OMEGA_OVER_DE
    for v in range(8):
        n = v + 0.5
        energy = eta * n - eta**2 * n**2 / 4
        assert n < 2 / eta  # Only the bound-state branch of the Morse model
        left = 1 - np.log(1 + np.sqrt(energy)) / A_RE
        right = 1 - np.log(1 - np.sqrt(energy)) / A_RE
        ax.hlines(energy, left, right, color="#5a6478", linewidth=1)
        if v < 5:
            ax.text(right + 0.025, energy, f"v = {v}", va="center", fontsize=9)
    ground = eta / 2 - eta**2 / 16
    ax.axhline(1, color="#5a6478", linestyle=":", linewidth=1.3)
    ax.text(3.1, 1.025, "Dissociation limit", ha="right", color="#5a6478")
    ax.hlines(0, 1, 2.55, color="#5a6478", linestyle=":", linewidth=0.8)
    ax.hlines(ground, 1.2, 2.9, color="#1f4e9c", linestyle=":", linewidth=0.8)
    for x, bottom, label, color in [
        (2.55, 0, r"$D_e$", "#1f2633"),
        (2.9, ground, r"$D_0$", "#1f4e9c"),
    ]:
        ax.annotate("", xy=(x, 1), xytext=(x, bottom),
                    arrowprops={"arrowstyle": "<->", "color": color, "lw": 1.5})
        ax.text(x + 0.04, (1 + bottom) / 2, label, color=color, va="center")
    ax.set(xlim=(0.55, 3.15), ylim=(-0.06, 1.35), xlabel=r"Separation $R/R_e$",
           ylabel=r"Energy / $D_e$", title="A finite-depth well and its local harmonic limit")
    ax.spines[["top", "right"]].set_visible(False)
    ax.legend(loc="upper right", frameon=False, fontsize=10)
    fig.text(0.5, 0.02,
             r"Illustrative model: $aR_e=2.5$, $\hbar\Omega_e/D_e=0.2$; not a CO fit.",
             ha="center", color="#5a6478", fontsize=10)
    fig.tight_layout(rect=(0, 0.05, 1, 1))
    FIGURE.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(FIGURE)
    plt.close(fig)


if __name__ == "__main__":
    main()
