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
        x0 = np.array(data["x0"])  # left, bottom of the grid
        params = data["params"]
        output_file = sys.argv[1].replace(".json", "_xref.csv")

    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)

    sol = solve_duffing_ivp(x0, params, nmap=2, dense_output=True)

    traj = sol.sol(np.linspace(0, 4 * np.pi, 1000))
    df = pd.DataFrame(traj.T, columns=["x0", "x1"])
    df.to_csv(output_file, index=False)
    print(f"Reference trajectory saved to {output_file}")
    print("Reference trajectory calculation completed.")
    sys.exit(0)
