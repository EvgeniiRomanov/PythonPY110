# Задание 4.
# Напишите скрипт для сложения двух заданных списков, используя map и lambda.

import random

if __name__ == "__main__":
    list_1 = [random.randint(-10, 10) for _ in range(8)]
    print(list_1)
    list_2 = [random.randint(-10, 10) for _ in range(8)]
    print(list_2)
    result_list = list(map(lambda x, y: x + y, list_1, list_2))

    print(result_list)