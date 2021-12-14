"""Написать генератор, возвращающий по одному слову текстового файла,
 при этом не загружая в память весь файл.
 В качестве разделителя слов использовать символ пробела."""

INPUT_FILE = "input_task3.txt"


def gen_return_one_word():
    with open(INPUT_FILE, "r", encoding="UTF8") as f:
        for word_ in f.read().split(" "):
            yield word_


if __name__ == "__main__":
    words_ = gen_return_one_word()

    for _ in range(5):
        print(next(words_), end=" ")