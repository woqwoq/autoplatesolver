from cli_controller import start_cli
from update_checker import update_recent_files
from queue import Queue
import threading

FOLDER = 'example_files/'

def start():
    queue = Queue()
    cli_controller = threading.Thread(target=start_cli, args=(queue,))
    cli_controller.start()
    file_updater = threading.Thread(target=update_recent_files, args=(FOLDER, queue,), daemon=True)
    file_updater.start()

if __name__ == "__main__":
    start()

