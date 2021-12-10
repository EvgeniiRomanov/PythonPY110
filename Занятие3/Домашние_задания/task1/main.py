import random

INPUT_FILE_1 = "input_1.txt"
INPUT_FILE_2 = "input_2.txt"

def task() -> None:


    with open(INPUT_FILE_1, "w") as file_1, open(INPUT_FILE_2, "w") as file_2:
        # for i in range(1, 15):
        #     list_1.append(random.randint(1, 100))
        #     list_2.append(random.randint(200, 300))
        list_1 = random.sample(range(1, 100), 15)
        list_2 = random.sample(range(200, 300), 10)
        file_1.write(f"{list_1}")
        file_2.write(f"{list_2}")
        #print(list_1, type(list_1))

    with open(INPUT_FILE_1, "r") as file_1, open(INPUT_FILE_2, "r") as file_2:

        tmp_1 = file_1.read()
        tmp_2 = file_2.read()

        a3 = [int(i) for i in tmp_1[1: len(tmp_1)-1].split(', ')]    # какая-то баржа конечно
        a4 = [int(i) for i in tmp_2[1: len(tmp_2)-1].split(', ')]
        #print(a5, type(a5))
        #print(a6, type(a6))
        print(a3+a4)


if __name__ == "__main__":
    task()
