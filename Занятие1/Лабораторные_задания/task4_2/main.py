import itertools


def task():
    a = (1, 2, 3)
    #repeater = ...  # TODO бесконечно повторяем элементы кортежа
    repeater = itertools.cycle(a)
    for _ in range(10):
        print(next(repeater))


if __name__ == "__main__":
    task()
