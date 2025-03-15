from queue import Queue
import new_file_processor

def handle_new_file(file, memory: dict):
    answer = input(f"New file found! Would you like to platesolve '{file}'? (y/n)")
    match answer:
        case 'y':
            new_file_processor.process(file, memory)
        case 'n':
            print(f"Ignoring {file}..")


def handle_queue(queue: Queue, memory: dict):
    queue_val = queue.get()
    if(queue_val != None):
        handle_new_file(queue_val, memory)
    