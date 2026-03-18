# Vehicle Steering and Throttle Control – PPC Hackathon

## Overview

This project implements the control logic for an autonomous vehicle in the PPC Hackathon simulation environment. The objective is to generate appropriate **steering and throttle commands** that allow the vehicle to follow a given path of waypoints smoothly while maintaining stability. The controller operates at every simulation step and uses the vehicle’s current state to compute control actions.

## Path Planning

Waypoints are generated using blue and yellow cone pairs. A weighted midpoint is used instead of the exact midpoint, placing the path slightly closer to the inner cone for smoother turns and improved trajectory.

## Steering Control

The steering controller determines the direction the vehicle should turn in order to follow the planned path. The algorithm selects a target waypoint ahead of the vehicle and calculates the angle between the vehicle’s current heading and the direction of the waypoint. The steering command is computed as the difference between this desired heading and the vehicle’s current yaw. To avoid abrupt steering, the controller also averages the direction toward a farther waypoint when available. The final steering value is normalized and clipped to the allowed range ([-0.5, 0.5]) radians.

## Throttle Control

The throttle algorithm adjusts vehicle acceleration based on the steering demand. When the steering angle is small (indicating a straight path), the vehicle is allowed to accelerate with higher throttle. When the steering angle increases, the throttle is reduced and braking may be applied to maintain stability during turns. This ensures that the vehicle slows down in sharp curves and speeds up on straighter segments.

## Conclusion

The implemented steering and throttle algorithms allow the vehicle to follow the path while adapting its speed based on turning requirements, resulting in smoother and safer navigation.
values are mainly trial error based
