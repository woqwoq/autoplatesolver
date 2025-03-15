def parse_header(file: str):
    header_data = {}
    with open(file, "r") as file:
        for line in file:
            if "=" in line:
                key, value = line.split("=")
                header_data[key.strip()] = value.strip()
    return header_data

def is_solved(file: str):
    header_data = parse_header(file)

    if(header_data["PLTSOLVD"] == 'T'):
        return True
    return False