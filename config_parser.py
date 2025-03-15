def get_config():
    file = 'config.ini'
    config = {}
    with open(file, "r") as file:
        for line in file:
            if "=" in line:
                key, value = line.split("=")
                config[key.strip()] = value.strip()
    return config

def get_astap_loc():
    return get_config()["ASTAP_LOC"]

def get_atlas_loc():
    return get_config()["ATLAS_LOC"]

def get_input_loc():
    return get_config()['INPUT_FOLDER']
