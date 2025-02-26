import time
from queue import Queue

SLEEP_BETWEEN_UPDATES = 10


def handle_new_file(file):
    answer = input(f"New file found! Would you like to platesolve '{file}'? (y/n)")
    match answer:
        case 'y':
            print("#TODO Solving..")
        case 'n':
            print(f"Ignoring {file}..")


def handle_queue(queue: Queue):
    queue_val = queue.get()
    if(queue_val != None):
        handle_new_file(queue_val)
    