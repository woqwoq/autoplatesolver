import threading
import update_checker
import queue_handler
from queue import Queue

memory ={
    "ra"    : 0,
    "dec"   : 0,
    "search_rad": 0,
    "fov"   : 0,
}

commands_usage ={
    "set":  "set var val",
    "get":  "get val"
}

def print_command_error(caller):
    print(f'Error: Command {caller} is to be used as follows: {commands_usage[caller]}')
    

def command_set(args):
    if(len(args) == 2):
        if(args[0] in memory):
            memory[args[0]] = args[1]
            print(f'{args[0]} has been set to {args[1]}')
        else:
            print(f'Error: {args[0]} is not a valid variable.')
    else:
        return -1
    
def command_get(args):
    if(len(args) == 1):
        if(args[0] in memory):
            print(f'{memory[args[0]]}')
        else:
            print(f'Error: {args[0]} is not a valid variable.')
    else:
        return -1
        
    
commands = {
    "set": lambda args: command_set(args),
    "get": lambda args: command_get(args),
}

def command_switcher(args):
    if(len(args) > 1):
        if(args[0] in commands):
            func = commands[args[0]]
            return_val = func(args[1:])
            if(return_val == -1):
                print_command_error(args[0])
    else:
        print(f"Error: Command '{args[0]}' does not exist or did not receive enought arguments")
        
        
def start_cli(queue: Queue):
    while(True):
        if queue.empty():
            command = input(">>").split(" ")
            command_switcher(command)
        else:
            queue_handler.handle_queue(queue)



