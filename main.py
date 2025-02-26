from cli_controller import start_cli
from update_checker import update_recent_files
from queue_handler import queue_checker_loop
import threading

FOLDER = 'example_files/'

def start():
    queue = []
    cli_controller = threading.Thread(target=start_cli, args=(queue,))
    cli_controller.start()
    file_updater = threading.Thread(target=update_recent_files, args=(FOLDER, queue,), daemon=True)
    file_updater.start()
    queue_handler = threading.Thread(target=queue_checker_loop, args=(queue,), daemon=True)
    queue_handler.start()

if __name__ == "__main__":
    start()

