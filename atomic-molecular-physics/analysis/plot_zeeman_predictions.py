"""Plot electronic Zeeman predictions for Unit 4; no experimental data are used."""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


MU_B_OVER_H_GHZ_PER_T = 13.996245  # CODATA 2018, rounded
FIGURE = Path(__file__).resolve().parents[1] / "figures" / "zeeman-predictions.svg"


def main():
    plt.rcParams.update(
        {"font.size": 11, "svg.fonttype": "none", "axes.spines.top": False,
         "axes.spines.right": False}
    )
    field = np.linspace(0.0, 0.5, 101)
    styles = {
        0: ("#5a6478", "-", r"$\pi$: $q=0$"),
        1: ("#b5561f", "--", r"$\sigma^+$: $q=+1$"),
        -1: ("#1f4e9c", "--", r"$\sigma^-$: $q=-1$"),
    }
    models = [
        (r"Normal Zeeman: $g_u=g_l=1$", [(0.0, 0), (1.0, 1), (-1.0, -1)]),
        (r"Na D1: $g_u=2/3$, $g_l=2$",
         [(-2 / 3, 0), (2 / 3, 0), (4 / 3, 1), (-4 / 3, -1)]),
    ]
    fig, axes = plt.subplots(1, 2, figsize=(9.5, 4.5), sharey=True)
    for ax, (title, components) in zip(axes, models):
        labelled = set()
        for slope, q in components:
            color, linestyle, label = styles[q]
            ax.plot(
                field, slope * MU_B_OVER_H_GHZ_PER_T * field,
                color=color, linestyle=linestyle, linewidth=2,
                label=label if q not in labelled else "_nolegend_",
            )
            labelled.add(q)
        ax.set(title=title, xlabel="Magnetic field B (T)", xlim=(0, 0.5), ylim=(-10.5, 10.5))
        ax.grid(alpha=0.2)
        ax.legend(loc="upper left", frameon=False, fontsize=9)
    axes[0].set_ylabel(r"Frequency offset $\nu-\nu_0$ (GHz)")
    fig.suptitle("Predicted electronic Zeeman component frequencies", fontsize=13)
    fig.text(
        0.5, 0.025,
        "Calculated positions; hyperfine structure omitted. Line strengths are not shown.",
        ha="center", fontsize=10, color="#5a6478",
    )
    fig.tight_layout(rect=(0, 0.06, 1, 0.94))
    FIGURE.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(FIGURE)
    plt.close(fig)


if __name__ == "__main__":
    main()
