"""Generate neutral manuscript diagrams in PNG, SVG, and PDF formats."""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "docs" / "figures"
OUT.mkdir(parents=True, exist_ok=True)

INK = "#263238"
BLUE = "#4C78A8"
TEAL = "#59A14F"
ORANGE = "#F28E2B"
PURPLE = "#8F63A8"
LIGHT = "#F5F7FA"


def save(fig, stem):
    for ext in ("png", "svg", "pdf"):
        fig.savefig(OUT / f"{stem}.{ext}", dpi=220, bbox_inches="tight", facecolor="white")
    plt.close(fig)


def box(ax, xy, width, height, text, color=BLUE, fontsize=9):
    patch = FancyBboxPatch(
        xy,
        width,
        height,
        boxstyle="round,pad=0.02,rounding_size=0.03",
        linewidth=1.3,
        edgecolor=color,
        facecolor=LIGHT,
    )
    ax.add_patch(patch)
    ax.text(xy[0] + width / 2, xy[1] + height / 2, text, ha="center", va="center", fontsize=fontsize, color=INK)
    return patch


def arrow(ax, start, end, color=INK, style="-|>"):
    ax.add_patch(FancyArrowPatch(start, end, arrowstyle=style, mutation_scale=12, linewidth=1.2, color=color))


def figure1():
    fig, ax = plt.subplots(figsize=(12, 4.2))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 4.2)
    ax.axis("off")
    labels = [
        "Embodied\ncoupling",
        "Perturbation\nand correction",
        "Dynamic\nhomeostasis",
        "Hierarchical\ninvariants",
        "Multiscale\nACS",
        "EM\nmanifestation",
    ]
    xs = [0.25, 2.15, 4.05, 5.95, 7.85, 9.75]
    colors = [TEAL, TEAL, TEAL, BLUE, BLUE, ORANGE]
    for x, label, color in zip(xs, labels, colors):
        box(ax, (x, 2.25), 1.55, 0.85, label, color)
    for x in xs[:-1]:
        arrow(ax, (x + 1.55, 2.67), (x + 1.9, 2.67))
    box(ax, (4.45, 0.45), 3.1, 0.8, "Restricted identity hypothesis:\nintrinsic existence = subjective aspect", PURPLE, 9)
    arrow(ax, (8.62, 2.25), (7.15, 1.27), PURPLE)
    ax.text(3.0, 3.65, "MECHANISTIC PROPOSAL", ha="center", fontsize=10, weight="bold", color=TEAL)
    ax.text(8.7, 3.65, "EMPIRICAL SIGNATURES", ha="center", fontsize=10, weight="bold", color=BLUE)
    ax.text(6.0, 0.1, "ONTOLOGICAL PROPOSAL", ha="center", fontsize=10, weight="bold", color=PURPLE)
    save(fig, "figure1_mechanistic_chain")


def figure2():
    fig, (left, right) = plt.subplots(1, 2, figsize=(11, 4.4), gridspec_kw={"width_ratios": [1, 1.3]})
    left.axis("off")
    left.set_xlim(0, 5)
    left.set_ylim(0, 5)
    levels = [(0.7, 0.5, 3.6, 0.75, "Fast/local relations  Cₜ^(m)"),
              (1.0, 1.65, 3.0, 0.75, "Intermediate communities"),
              (1.3, 2.8, 2.4, 0.75, "Slow/global invariants")]
    for x, y, w, h, label in levels:
        box(left, (x, y), w, h, label, BLUE, 9)
    arrow(left, (2.5, 1.25), (2.5, 1.62), BLUE)
    arrow(left, (2.5, 2.4), (2.5, 2.77), BLUE)
    left.text(2.5, 4.25, "MULTISCALE ACS FAMILY", ha="center", weight="bold", color=BLUE)
    left.text(2.5, 3.85, "Different windows and relational operators", ha="center", fontsize=9, color=INK)

    right.set_facecolor(LIGHT)
    t = [0, 0.7, 1.5, 2.2, 2.8, 3.6, 4.1, 4.8, 5.4, 6.0]
    y = [1.1, 1.2, 1.15, 2.9, 3.0, 2.95, 1.8, 1.75, 3.7, 3.65]
    right.plot(t, y, color=PURPLE, linewidth=2.3, marker="o", markersize=4)
    right.axvspan(0, 1.5, color=TEAL, alpha=0.15)
    right.axvspan(2.2, 3.6, color=TEAL, alpha=0.15)
    right.axvspan(4.1, 4.8, color=TEAL, alpha=0.15)
    right.axvspan(5.4, 6.0, color=TEAL, alpha=0.15)
    right.text(0.75, 0.55, "finite dwell", ha="center", fontsize=8)
    right.text(2.9, 2.35, "finite dwell", ha="center", fontsize=8)
    right.annotate("transition", xy=(1.85, 2.0), xytext=(1.2, 3.6), arrowprops={"arrowstyle": "->"}, fontsize=8)
    right.set_xlabel("time")
    right.set_ylabel("position in relational state space")
    right.set_title("METASTABLE TRAJECTORY", fontsize=10, weight="bold", color=PURPLE)
    right.set_xticks([])
    right.set_yticks([])
    for spine in right.spines.values():
        spine.set_visible(False)
    save(fig, "figure2_acs_multiscale")


def figure3():
    fig, ax = plt.subplots(figsize=(10.5, 4.7))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8)
    ax.axis("off")
    dims = ["Content richness", "Selfhood", "Temporal continuity", "Access / report", "Valence", "Sensorimotor closure", "Perturbation recovery"]
    for i, label in enumerate(dims):
        y = 7.1 - i * 0.9
        ax.text(0.1, y, label, ha="left", va="center", fontsize=9, color=INK)
        ax.plot([2.5, 9.5], [y, y], color="#D6DCE3", linewidth=5, solid_capstyle="round")
        ax.plot([2.5, 9.5], [y, y], color=BLUE if i % 2 == 0 else TEAL, linewidth=2, alpha=0.75)
        ax.scatter([3.1 + (i * 0.77) % 5.7], [y], s=55, color=ORANGE, zorder=3)
    ax.text(6.0, 7.75, "MULTIDIMENSIONAL PROFILE", ha="center", weight="bold", color=PURPLE)
    ax.text(2.5, 0.35, "lower / absent evidence", fontsize=8, color=INK)
    ax.text(9.5, 0.35, "higher / different evidence", fontsize=8, color=INK, ha="right")
    ax.text(6.0, 0.05, "Illustrative markers are not measurements or classifications.", fontsize=8, ha="center", color="#5F6B73")
    save(fig, "figure3_multidimensional_spectrum")


def figure4():
    fig, ax = plt.subplots(figsize=(9.5, 5.2))
    ax.set_xlim(-0.3, 3.3)
    ax.set_ylim(-0.2, 3.3)
    ax.set_xticks([0, 1, 2, 3], ["Embodiment", "Relational\ndynamics", "Global / field\norganization", "Intrinsic\nontology"])
    ax.set_yticks([0, 1, 2, 3], ["Conceptual", "Mechanistic", "Empirical", "Ontological"])
    ax.grid(color="#D6DCE3", linewidth=1)
    points = {
        "Enactivism": (0.2, 1.0), "Predictive\nprocessing": (0.65, 1.35),
        "RPT": (1.2, 1.6), "GNW": (1.65, 1.8), "IIT": (1.9, 2.5),
        "CEMI": (2.45, 2.15), "Identity\ntheory": (2.8, 2.8),
        "Russellian\nmonism": (3.0, 3.05), "Present\nframework": (1.9, 2.25),
    }
    for name, (x, y) in points.items():
        special = name.startswith("Present")
        ax.scatter(x, y, s=150 if special else 85, color=PURPLE if special else BLUE, zorder=3)
        ax.text(x + 0.05, y + 0.08, name, fontsize=8, weight="bold" if special else "normal")
    ax.set_title("OVERLAPPING EMPHASES, NON-IDENTICAL COMMITMENTS", fontsize=10, weight="bold", color=PURPLE)
    for spine in ax.spines.values():
        spine.set_visible(False)
    save(fig, "figure4_theory_matrix")


def figure5():
    fig, ax = plt.subplots(figsize=(11.5, 4.8))
    ax.set_xlim(0, 11.5)
    ax.set_ylim(0, 5)
    ax.axis("off")
    programmes = [
        ("A", "Stable percepts"), ("B", "Relational signatures"), ("C", "Consciousness profile"),
        ("D", "Lesions & perturbations"), ("E", "Cultures & organoids"),
        ("F", "Minimal systems"), ("G", "Embodied agents"),
    ]
    positions = [(0.2, 3.25), (2.45, 3.25), (4.7, 3.25), (6.95, 3.25), (2.45, 1.25), (4.7, 1.25), (6.95, 1.25)]
    for (letter, label), (x, y) in zip(programmes, positions):
        color = BLUE if letter in "ABCD" else TEAL
        box(ax, (x, y), 1.85, 0.85, f"{letter}\n{label}", color, 8.5)
    for x in (2.05, 4.3, 6.55):
        arrow(ax, (x, 3.67), (x + 0.35, 3.67))
    arrow(ax, (7.85, 3.25), (7.85, 2.15))
    arrow(ax, (7.0, 1.67), (6.65, 1.67), style="<|-")
    arrow(ax, (4.75, 1.67), (4.4, 1.67), style="<|-")
    box(ax, (9.3, 2.2), 1.85, 0.95, "Shared tests:\nACS · recovery ·\ninvariants", ORANGE, 8.5)
    for target in [(8.8, 3.6), (8.8, 1.7)]:
        arrow(ax, target, (9.28, 2.68), ORANGE)
    ax.text(4.8, 4.55, "OBSERVATION AND CAUSAL INTERVENTION", ha="center", weight="bold", color=BLUE)
    ax.text(4.8, 0.45, "PROGRESSIVE CONSTRUCTION AND ABLATION", ha="center", weight="bold", color=TEAL)
    save(fig, "figure5_experimental_programme")


if __name__ == "__main__":
    figure1()
    figure2()
    figure3()
    figure4()
    figure5()
    print(f"Generated figures in {OUT}")
