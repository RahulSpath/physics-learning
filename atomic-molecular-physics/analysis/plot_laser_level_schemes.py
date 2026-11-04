"""Draw ideal three- and four-level pumping pathways for Unit 5."""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt


FIGURE = Path(__file__).resolve().parents[1] / "figures" / "laser-level-schemes.svg"


def arrow(ax, x, start, end, color, label, label_x):
    ax.annotate(
        "", xy=(x, end), xytext=(x, start),
        arrowprops={"arrowstyle": "->", "color": color, "lw": 2},
    )
    ax.text(label_x, (start + end) / 2, label, color=color, fontsize=10,
            va="center", rotation=90 if label in {"pump", "laser"} else 0)


def main():
    plt.rcParams.update({"font.size": 11, "svg.fonttype": "none"})
    fig, axes = plt.subplots(1, 2, figsize=(10, 4.6))
    for ax, four_level in zip(axes, [False, True]):
        levels = [(0, "ground" if four_level else "ground /\nlower laser"),
                  (2.7, "upper laser"), (4, "pump level")]
        if four_level:
            levels.append((1, "lower laser"))
        for y, label in levels:
            ax.hlines(y, 1, 2.8, color="#1f2633", linewidth=2)
            ax.text(3, y, label, va="center", fontsize=11)
        arrow(ax, 1.15, 0.05, 3.95, "#1f4e9c", "pump", 0.8)
        arrow(ax, 2.65, 3.95, 2.75, "#5a6478", "rapid", 2.8)
        arrow(ax, 1.9, 2.65, 1.05 if four_level else 0.05,
              "#b5561f", "laser", 2.02)
        if four_level:
            arrow(ax, 2.65, 0.95, 0.05, "#5a6478", "rapid", 2.8)
        ax.set(xlim=(0.5, 5.3), ylim=(-0.6, 4.6))
        ax.set_title("Four-level scheme" if four_level else "Three-level scheme")
        ax.axis("off")
    fig.text(0.5, 0.035, "Ideal population pathways; energy separations are not to scale.",
             ha="center", color="#5a6478", fontsize=10)
    fig.tight_layout(rect=(0, 0.07, 1, 1))
    FIGURE.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(FIGURE)
    plt.close(fig)


if __name__ == "__main__":
    main()
