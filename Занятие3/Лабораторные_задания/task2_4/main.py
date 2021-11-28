import json


def task():
    filename = "input.json"
    # TODO считать содержимое JSON файла
    with open(filename, "r") as input_f:
        data = json.load(input_f)
        #print(data)
      # TODO записать выражение-генератор возвращающее значение по ключу contains_improvement_appeals
    gen_exr = (i['contains_improvement_appeals'] for i in data)
    return sum(gen_exr)


if __name__ == "__main__":
    print(task())
