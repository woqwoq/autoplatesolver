import shutil
import os

def move_to_atlas_loc(file: str, atlas_loc: str):
    shutil.move(os.path.abspath(file), atlas_loc)