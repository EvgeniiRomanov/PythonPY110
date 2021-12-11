"""Написать генератор, возвращающий по 3 символа из текстового файла,
при этом не загружая в память весь файл."""

INPUT_FILE_1 = "input_task2.txt"

def read_symbols(base: int):
    with open(INPUT_FILE_1, "r", encoding="UTF8") as file_1:
        for line in file_1.read():
            yield line[:base]


if __name__ == "__main__":
    symbols_ = read_symbols(3)

    for _ in range(25):
        print(next(symbols_), end="")

