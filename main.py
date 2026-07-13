# -- imports --
import yaml

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
0,472.4409448818898,4,1,0,100,1,0

[HitObjects]
"""

osu_content += "\n".join(hit_lines)


# -- output --
with open("converted.osu", "w", encoding="utf-8") as file:
    file.write(osu_content)

print("Done :3 Created converted.osu")

# -- lane assign (fuck english spelling, I hate this language) --
# x, y, time, type, hitsound, extras
# x = 64 + ((lane - 1) * 128)   -> Note calculation
# y = 192                       -> why does osu! do this? idk and I'm too afraid to ask 
# type = 1                      -> normal
# type = 128                    -> ln