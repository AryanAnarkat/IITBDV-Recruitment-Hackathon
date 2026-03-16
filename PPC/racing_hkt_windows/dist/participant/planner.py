import numpy as np  # type: ignore

def plan(cones: list[dict]) -> list[dict]:
    """
    Generate a path from the cone layout.
    Called ONCE before the simulation starts.
    """

    path = []

    blue = np.array([[cone["x"], cone["y"]] for cone in cones if cone["side"] == "left"])
    yellow = np.array([[cone["x"], cone["y"]] for cone in cones if cone["side"] == "right"])

    a = 0

    # generate midpoints between cones
    for b, y in zip(blue, yellow):
        a += 1
        x = 0.48

        path.append({
            "x": (x * b[0] + y[0]) / (x + 1),
            "y": (x * b[1] + y[1]) / (x + 1)
        })

    return path