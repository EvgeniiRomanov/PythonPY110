def task():
    filename = "input.txt"
    with open(filename) as f:  # менеджер контекста открывает файл в режиме чтения в текстовом формате "rt"
        for line in f:  # файл является итератором, который построчно возвращает свое содержимое
            # TODO c помощью метода строки strip очистить строку от непечатыемых символов
            line = line.strip()
            print(line)


if __name__ == "__main__":
    task()
