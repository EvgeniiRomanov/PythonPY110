import itertools
from itertools import repeat


def task():
    a = 10
    for num in repeat(a, 4):  # TODO повторить переменную a 4 раза
        print(num)
    # for num in range(4):  # TODO повторить переменную a 4 раза
    #     print(a)

if __name__ == "__main__":
    task()
