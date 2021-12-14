import json


def task(input_filename: str, output_filename: str) -> None:
    # TODO считать содержимое json файл input.json
    with open(input_filename, "r") as f, open(output_filename, "w") as out:
        #json_data = json.load(f)
        #json.dump(json_data, out, indent=4)
    # TODO записать содержимое в json файл output.json с отступами
        json.dump(json.load(f), out, indent=4)

if __name__ == "__main__":
    input_file = "input.json"
    output_file = "output.json"

    task(input_file, output_file)

    with open(output_file) as output_f:
        #for line in output_f:
        print(output_f.read())
            #print(line, end="")