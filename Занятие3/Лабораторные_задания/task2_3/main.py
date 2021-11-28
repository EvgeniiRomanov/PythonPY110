import json


def task():
    filename = "input.json"
    # TODO считать содержимое JSON файла
    with open(filename, "r") as input_f:
        data = json.load(input_f)
        #print(data)
    return max(data, key=lambda item: item["score"])


if __name__ == "__main__":
    print(task())
