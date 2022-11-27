import json

INPUT_FILE = "input.csv"


# TODO реализовать конвертер из csv в json
def csv_to_list_dict(filename, delimeter=",", new_line="\n") -> list[dict]:
    with open(filename, "r") as f:
        strings = [line.rstrip().split(",") for line in f]
        headers_ = strings[0]
        list_ = []
        for strings_ in range(1, headers_ + 1):
            list_.append(dict(zip()))
    return list_

print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))

