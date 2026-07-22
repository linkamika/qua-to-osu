# -- imports --
import yaml
import math

# -- path :3 --
qua_path = input("Path to .qua file: ")

with open(qua_path, "r", encoding="utf-8") as file:
    qua_data = yaml.safe_load(file)

hit_objects = qua_data["HitObjects"]

# -- metadata ask --
title = input("Title [Unknown]: ") or "Unknown"
artist = input("Artist: ")
creator = input("Creator: ")
version = input("Difficulty: ")
source = input("Source: ")
audio = "audio.mp3"

bpm = float(input("What is the song BPM?: "))
bpm_convert = 60000/bpm

# -- placement --
hit_lines = []

for note in hit_objects:
    lane = note["Lane"]
    start = note["StartTime"]

    x = 64 + ((lane - 1) * 128)
    y = 192

    if "EndTime" in note:
        end = note["EndTime"]

        note_line = f"{x},{y},{start},128,0,{end}:1:0:0:100:"
        hit_lines.append(note_line)

    else:
        note_line = f"{x},{y},{start},1,0,1:0:0:100:"
        hit_lines.append(note_line)


# -- create osu file --
osu_content = f"""osu file format v128

[General]
AudioFilename: {audio}
AudioLeadIn: 0
PreviewTime: -1
Countdown: 0
Mode: 3

[Metadata]
Title: {title}
Artist: {artist}
Creator: {creator}
Version: {version}
Source: {source}

[Difficulty]
CircleSize: 4

[TimingPoints]
0,{bpm_convert},4,1,0,100,1,0

[HitObjects]
"""

osu_content += "\n".join(hit_lines)


# -- output --
with open("converted.osu", "w", encoding="utf-8") as file:
    file.write(osu_content)

print("Done - Created converted.osu")