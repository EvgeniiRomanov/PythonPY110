from itertools import repeat


def task(list_args: list) -> bool:
    return all(map(isinstance, list_args, repeat(int)))

if __name__ == "__main__":
    print(task([1, 2, 3]))
    print(task(["str", 2, 3]))


# Тут по ходу от нас хотели что-то с 'any' и 'all'