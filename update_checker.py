import os
import time

SLEEP_BETWEEN_UPDATES = 10

def get_files_within_folder(folder):
    filenames_within_folder = []
    for files in os.listdir(folder):
        filenames_within_folder.append(folder+files)
    return filenames_within_folder

def find_difference_between_file_lists(original, new):
    res = []
    for file in new:
        if file not in original:
            res.append(file)
    return res

def get_most_recent_file(file_list):
    most_recent_date = 0 - pow(2, 32)-1
    most_recent_file = None

    for file in file_list:
        current_file_date = os.path.getctime(file)

        if(current_file_date > most_recent_date):
            most_recent_date = current_file_date
            most_recent_file = file


    return most_recent_file

def update_file_list(folder):
    file_list = get_files_within_folder(folder)
    time.sleep(SLEEP_BETWEEN_UPDATES)
    candidate_list = get_files_within_folder(folder)
    if len(file_list) < len(candidate_list):
        difference = find_difference_between_file_lists(file_list, candidate_list)
        file_list = candidate_list
        return get_most_recent_file(difference)
    else:
        return None
        

def update_recent_files(folder, queue: list):
    while(True):
        result = update_file_list(folder)
        if result != None:
            most_recent_file = result
            queue.append(most_recent_file)