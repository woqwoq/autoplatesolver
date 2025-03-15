import astap_caller
import ini_parser
import file_mover
import time

ATLAS_LOC = "C:\\Users\\admin\\AppData\\Local\\skychart\\pictures"
SOLVE_TIME = 6

def change_extension(file: str, new_ext: str):
    file = file.split('.')
    file[-1] = new_ext
    return '.'.join(file)

def process(file: str, memory: dict):
    print(f"Solving '{file}' ...")
    astap_caller.call_astap(memory, file)
    time.sleep(SOLVE_TIME)
    if(ini_parser.is_solved(change_extension(file, 'ini'))):
        print(f"Solved successfully! Moving '{file}' to {ATLAS_LOC}")
        file_mover.move_to_atlas_loc(change_extension(file, 'fits'), ATLAS_LOC)
        print("Moved successfully!")
    else:
        print(f"ERROR: '{file}' could not be solved!")