import queue_handler
import sys
import select
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
    while True:
        while not queue.empty():                              #checking the q first, not sure about the efficiency lol
            queue_handler.handle_queue(queue)

        rlist, _, _ = select.select([sys.stdin], [], [], 0.1) #If sys.stdin has some stuff to be read in, we write sys.stdin in the rlist
        if rlist:                                             #else, we give 0.1 timeout 
            command = input(">> ").split(" ")                 #if rlist is non-empty, then we run the command contained in sys.stdin
            command_switcher(command)



