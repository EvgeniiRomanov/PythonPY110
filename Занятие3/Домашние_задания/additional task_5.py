# Написать генератор, возвращающий  последние n строк из текстового файла,
# при этом не загружая в память весь файл.

# пока работает для случая БЕЗ переноса с последней строки

INPUT_FILE = "input_task5.txt"


def count_str() -> int:   #подсчитываем количество строк
    with open(INPUT_FILE, "r", encoding="UTF8") as f:
        count_str = sum(1 for _ in f)
        # count_str = 0
        # for line in f:
        #     count_str += 1

    return count_str

def read_rows_from_end(base: int):
    with open(INPUT_FILE, "r", encoding="UTF8") as f:
        f.seek(0, 2)
            print(line, end="")


            #yield line[:base]


if __name__ == "__main__":
    print(count_str())
    #a_ = int(input("Введите количество строк, которые желаете считать с конца файла: "))
    #symbols_ = read_symbols(3)

    # for _ in range(25):
    #     print(next(symbols_), end="")