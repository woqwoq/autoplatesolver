import subprocess
import os

PATH_TO_ASTAP = r"C:\Program Files\astap\astap.exe"

def dec_to_spd(dec):
    return int(dec) + 90

def build_command(path_to_astap, target_file, search_radius, ra, dec, fov):
    return [
        path_to_astap,
        "-f", os.path.abspath(target_file),
        "-r", str(search_radius),
        "-ra", str(ra),
        "-spd", str(dec_to_spd(dec)),
        "-fov", str(fov),
        "-update"
    ]

def run_astap(command: list):
    subprocess.run(command)

def call_astap(memory: dict, file: str):
    command = build_command(PATH_TO_ASTAP, file, memory['search_radius'], memory['ra'], memory['dec'], memory['fov'])
    run_astap(command)

# print(build_command(PATH_TO_ASTAP, "astap_caller.py", 1, 2, 3, 4))
