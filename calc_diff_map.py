import sys, json
import numpy as np
import pandas as pd

from system import solve_duffing_ivp


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python diff_map.py <data.json>")
        sys.exit(1)

    try:
        with open(sys.argv[1], "r") as f:
            data = json.load(f)
        dm_x0 = np.array(data["dm_x0"])  # left, bottom of the grid
        dm_x1 = np.array(data["dm_x1"])  # right, top of the grid
        params = data["params"]
        resolution = data.get("resolution", 256)  # Default resolution if not specified
        output_file = sys.argv[1].replace(".json", "_diff_map.csv")

    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)

    # Grid for the state space
    x0_range = np.linspace(dm_x0[0], dm_x1[0], resolution)
    x1_range = np.linspace(dm_x0[1], dm_x1[1], resolution)
    f = lambda x: solve_duffing_ivp(x, params, nmap=2).y[:, -1]
    diff_func = lambda x: f(x) - x

    results = []
    for x0 in x0_range:
        for x1 in x1_range:
            print(
                f"Computing difference at ({x0:+.4f}, {x1:+.4f})", end="\r", flush=True
            )
            diff = diff_func(np.array([x0, x1]))

            results.append([x0, x1, diff[0], diff[1], np.linalg.norm(diff)])

    df = pd.DataFrame(results, columns=["x0", "x1", "d0", "d1", "d_norm"])
    df.to_csv(output_file, index=False)
    print(f"Difference heatmap saved to {output_file}")
    print("Difference heatmap calculation completed.")
    sys.exit(0)
