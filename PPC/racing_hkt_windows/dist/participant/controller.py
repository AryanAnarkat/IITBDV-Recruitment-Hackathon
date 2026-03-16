
import math
'''
PPC Hackathon — Participant Boilerplate
You must implement two functions: plan() and control()
'''

# ─── TYPES (for reference) ────────────────────────────────────────────────────

# Path: list of waypoints [{"x": float, "y": float}, ...]
# State: {"x", "y", "yaw", "vx", "vy", "yaw_rate"} 
# CmdFeedback: {"throttle", "steer"}         

# ─── CONTROLLER ───────────────────────────────────────────────────────────────
import numpy as np
a=0
b=.3
heavy=0
speed=0
def angle(x1,y1,x2,y2,x3,y3):
    a1=math.atan2(y2-y1,x2-x1)
    a2=math.atan2(y2-y3,x2-x3)
    steer=a2-a1
    math.atan2(math.sin(steer), math.cos(steer))
    return steer
def steering(path: list[dict], state: dict):
    global a
    global b,heavy,speed
    if (path[a]["x"]-state["x"])*(path[a]["x"]-state["x"])+(path[a]["y"]-state["y"])*(path[a]["y"]-state["y"])>(path[a+1]["x"]-state["x"])*(path[a+1]["x"]-state["x"])+(path[a+1]["y"]-state["y"])*(path[a+1]["y"]-state["y"]):
        if a<len(path)-2:
            a=a+1
            
    length_of_car = 2.6
# Calculate steering angle based on path and vehicle state
    angl=math.atan2((path[a+1]["y"]-state["y"]),(path[a+1]["x"]-state["x"]))
    # if angle<1.57 and state["yaw"]>4.71:
    #     angle=angle+6.28
    steer = angl - state["yaw"]
    steer = math.atan2(math.sin(steer), math.cos(steer))
    if a<len(path)-4:
        angl1=math.atan2((path[a+3]["y"]-state["y"]),(path[a+3]["x"]-state["x"]))
        # if angle<1.57 and state["yaw"]>4.71:
        #     angle=angle+6.28
        steer1 = angl1 - state["yaw"]
        steer1 = math.atan2(math.sin(steer1), math.cos(steer1))
        steer=(steer+steer1)/2
    b=abs(steer)
    if b>.8:
        heavy=1
    speed=pow(state["vx"]*state["vx"]+state["vy"]*state["vy"],.5)
    if (a>0 and a<len(path)-2 and (angle(path[a]["x"],path[a]["y"],path[a+1]["x"],path[a+1]["y"],path[a+2]["x"],path[a+2]["y"]))>0.3):
        steer=steer+.1

    # Default steer value
    # 0.5 in the max steering angle in radians (about 28.6 degrees)
    return np.clip(steer*1.9, -0.5, 0.5)

def throttle_algorithm(target_speed, current_speed, dt):
    global b,speed
    k=9*(.4-b)
    if k>0:
        throttle=k*.7+.108
        brake=0
        if b<0.2:
            throttle=1
    else:
        brake=-.1*k
        throttle=0
        if b>0.16:
            brake=.08    
    # generate the output for throttle command
    # clip throttle and brake to [0, 1]
    return np.clip(throttle, 0.0, 1.0), np.clip(brake, 0.0, 1.0)

def control(
    path: list[dict],
    state: dict,
    cmd_feedback: dict,
    step: int,
) -> tuple[float, float, float]:
    """
    Generate throttle, steer, brake for the current timestep.
    Called every 50ms during simulation.

    Args:
        path:         Your planned path (waypoints)
        state:        Noisy vehicle state observation
                        x, y        : position (m)
                        yaw         : heading (rad)
                        vx, vy      : velocity in body frame (m/s)
                        yaw_rate    : (rad/s)
        cmd_feedback: Last applied command with noise
                        throttle, steer, brake
        step:         Current simulation timestep index

    Returns:
        throttle  : float in [0.0, 1.0]   — 0=none, 1=full
        steer     : float in [-0.5, 0.5]  — rad, neg=left
        brake     : float in [0.0, 1.0]   — 0=none, 1=full
    
    Note: throttle and brake cannot both be > 0 simultaneously.
    """
    throttle = 0.0
    steer    = 0.0
    brake = 0.0
   
    # TODO: implement your controller here
    steer = steering(path, state)
    target_speed = 100.0  # m/s, adjust as needed
    global integral
    throttle, brake = throttle_algorithm(target_speed, state["vx"], 0.02)

    return throttle, steer, brake
