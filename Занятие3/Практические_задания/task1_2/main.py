def task():
    list_words = ["Один", "Два", "Три", "четыре", "Шарик ты балбес"]

    filename = "output.txt"
    with open(filename, "w", encoding="utf-8") as f:
        for word in list_words:
             # TODO с помощью метода write запишите построчно содержимое списка
            #f.writelines(f'{word}\n')
            #f.write(word+"\n")
            f.write(f'{word}\n')
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            print(line)


if __name__ == "__main__":
    task()
