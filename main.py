from cli_controller import start_cli
from update_checker import update_recent_files
from config_parser import get_input_loc
from queue import Queue
import threading

INPUT_FOLDER = get_input_loc()

def start():
    queue = Queue()
    cli_controller = threading.Thread(target=start_cli, args=(queue,))
    cli_controller.start()
    file_updater = threading.Thread(target=update_recent_files, args=(INPUT_FOLDER, queue,), daemon=True)
    file_updater.start()

if __name__ == "__main__":
    start()

