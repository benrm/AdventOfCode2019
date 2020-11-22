#!/usr/bin/python

import argparse
import math
import re
import sys

parser = argparse.ArgumentParser("Parse optional file inputs")
parser.add_argument("-i", "--input", nargs="?", type=argparse.FileType("r"), default=sys.stdin)
parser.add_argument("-t", "--time", type=int, default=100)
parser.add_argument("-s", "--step", type=int, default=10)
args = parser.parse_args()

p = re.compile("<x=(-?\d+), y=(-?\d+), z=(-?\d+)>")

moons = []
for line in args.input:
    m = p.match(line)
    if m == None:
        print("Failed to parse")
        exit(1)
    moons.append({"x_pos": int(m.group(1)), "y_pos": int(m.group(2)), "z_pos": int(m.group(3)), "x_vel": 0, "y_vel": 0, "z_vel": 0})

for time in range(args.time):
    for a in moons:
        for b in moons:
            if a == b:
                continue
            if a["x_pos"] > b["x_pos"]:
                a["x_vel"] -= 1
                b["x_vel"] += 1
            elif a["x_pos"] < b["x_pos"]:
                a["x_vel"] += 1
                b["x_vel"] -= 1
            if a["y_pos"] > b["y_pos"]:
                a["y_vel"] -= 1
                b["y_vel"] += 1
            elif a["y_pos"] < b["y_pos"]:
                a["y_vel"] += 1
                b["y_vel"] -= 1
            if a["z_pos"] > b["z_pos"]:
                a["z_vel"] -= 1
                b["z_vel"] += 1
            elif a["z_pos"] < b["z_pos"]:
                a["z_vel"] += 1
                b["z_vel"] -= 1

    for moon in moons:
        moon["x_pos"] += moon["x_vel"]
        moon["y_pos"] += moon["y_vel"]
        moon["z_pos"] += moon["z_vel"]

    if time % args.step == 0:
        print("Step " + str(time))
        for moon in moons:
            print(str(moon))
        print()

energy = 0
for moon in moons:
    potential = math.fabs(moon["x_pos"]) + math.fabs(moon["y_pos"]) + math.fabs(moon["z_pos"])
    kinetic = math.fabs(moon["x_vel"]) + math.fabs(moon["y_vel"]) + math.fabs(moon["z_vel"])
    energy += potential * kinetic

print("Total energy: " + str(energy))
