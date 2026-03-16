

'''
PPC Hackathon — Participant Boilerplate
You must implement two functions: plan() and control()
'''

# ─── TYPES (for reference) ────────────────────────────────────────────────────

# Cone: {"x": float, "y": float, "side": "left" | "right", "index": int}
# State: {"x", "y", "yaw", "vx", "vy", "yaw_rate"}  
# CmdFeedback: {"throttle", "steer"}        

# ─── PLANNER ──────────────────────────────────────────────────────────────────
import numpy as np # type: ignore

def plan(cones: list[dict]) -> list[dict]:
    """
    Generate a path from the cone layout.
    Called ONCE before the simulation starts.

    Args:
        cones: List of cone dicts with keys x, y, side ("left"/"right"), index

    Returns:
        path: List of waypoints [{"x": float, "y": float}, ...]
              Ordered from start to finish.
    
    Tip: Try midline interpolation between matched left/right cones.
         You can also compute a curvature-optimised racing line.
    """
    path = []
    # TODO: implement your path planning here
    blue = np.array([[cone["x"], cone["y"]] for cone in cones if cone["side"] == "left"])
    yellow = np.array([[cone["x"], cone["y"]] for cone in cones if cone["side"] == "right"])
    a=0
    # implement a planning algorithm to generate a path from the blue and yellow cones
    for b, y in zip(blue, yellow):
<<<<<<< HEAD
        a=a+1
=======
>>>>>>> e3e03186d94c200776238a17de8022323b994332
        x=.48
        path.append({
        "x": (x*b[0] + y[0]) / (x+1),
        "y": (x*b[1] + y[1]) / (x+1)})
<<<<<<< HEAD

        
=======
>>>>>>> e3e03186d94c200776238a17de8022323b994332
    return path
