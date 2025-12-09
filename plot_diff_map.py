import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python plot_diff_map.py <data.csv>")
        sys.exit(1)

    try:
        df = pd.read_csv(sys.argv[1])
        xref = pd.read_csv(sys.argv[1].replace("_diff_map.csv", "_xref.csv"))
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)

    max_diff = min(df["d_norm"].max(), 1.2)
    grid = df.pivot(index="x1", columns="x0", values="d_norm")

    fig, ax = plt.subplots(figsize=(8, 8))

    im = ax.imshow(
        grid,
        extent=(df["x0"].min(), df["x0"].max(), df["x1"].min(), df["x1"].max()),
        origin="lower",
        cmap="Reds",
        # cmap="bwr",
        aspect="auto",
    )
    im.set_clim(0, max_diff)
    plt.colorbar(im, ax=ax, label="Difference")
    ax.set_xlabel("x0")
    ax.set_ylabel("x1")
    ax.set_title("Difference heatmap")
    ax.grid()

    ax.plot(xref["x0"], xref["x1"], color="blue", linewidth=1)
    ax.plot(xref["x0"].iloc[0], xref["x1"].iloc[0], "bo", markersize=8)

    plt.subplots_adjust(bottom=0.15)
    axmax = plt.axes((0.2, 0.05, 0.7, 0.03), facecolor="lightgoldenrodyellow")
    smax = Slider(axmax, "Max Difference", 0.01, 5.0, valinit=max_diff)

    def update(_):
        new_max = smax.val
        im.set_clim(0, new_max)
        fig.canvas.draw_idle()

    smax.on_changed(update)
    plt.show()
