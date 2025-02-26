import time

SLEEP_BETWEEN_UPDATES = 10


def handle_new_file(file):
    answer = input(f"Would you like to platesolve {file}? (y/n)")
    match answer:
        case 'y':
            print("#TODO Solving..")
        case 'n':
            print(f"Ignoring {file}..")


def handle_queue(queue:list):
    queue_val = queue.pop() if len(queue) > 0 else None
    if(queue_val != None):
        handle_new_file(queue_val)

def queue_checker_loop(queue:list):
    while(True):
        time.sleep(SLEEP_BETWEEN_UPDATES)
        handle_queue(queue)
    