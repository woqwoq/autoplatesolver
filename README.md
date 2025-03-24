# What is it?
This is a simple Python script that monitors the folder where your camera stores images. When a new image is detected, the script prompts the user to plate-solve the image. 
If the user confirms, the script processes the image and saves the plate-solved version in the designated picture location of your sky chart software

# Why?
I found it quite difficult to locate myself at the sky when I was starting. This script allowed me to simplify and automate the process using platesolving.

# Requirements
Python 3.1+
ASTAP v2025 or higher

# Config
Make sure to fill proper paths for your sky atlas software, astap and camera picture folder.
```
ATLAS_LOC=C:\Users\admin\AppData\Local\skychart\pictures
ASTAP_LOC=C:\Program Files\astap\astap.exe
INPUT_FOLDER=example_files/
```

# Usage 
```
git clone https://github.com/woqwoq/autoplatesolver.git
cd autoplatesolver
python3 main.py
```
