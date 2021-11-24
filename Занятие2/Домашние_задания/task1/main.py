from itertools import count


def count(start_number: float = 1, step: float = 1):

    while True:
        yield start_number
        start_number *= step


if __name__ == "__main__":
    a = float(input("Введите основание: "))
    q1 = float(input("Введите знаменатель 'q': "))

    my_count = count(a, q1)
    for _ in range(10):
        print(next(my_count))

