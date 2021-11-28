OUTPUT_FILE = "output.txt"


def task():
    ...  # TODO записать лесенку в файл
    with open(OUTPUT_FILE, "w") as f:
        for i in range(1, 11):
            f.write(f'{"*" * i}\n'.rjust(11))
            #f.write("\n")
            #print(f'{"*" * i}'.rjust(11))
if __name__ == "__main__":
    task()

    with open(OUTPUT_FILE) as file:
        for line in file:
            print(line, end="")
