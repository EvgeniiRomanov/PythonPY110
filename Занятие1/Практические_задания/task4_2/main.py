from itertools import count

def sqrt_(x):
    return x ** 2

def get_add(x):
    return x % 2 == 0

def task():
    iterator_numbers = count(1, 1)
    #numbers = [i ** 2 for i in iterator_numbers if i % 2 == 0]  # TODO заменить на map и filter
    #numbers = map(lambda x: x ** 2, filter(lambda y: y % 2 == 0, iterator_numbers))
    numbers = map(sqrt_, filter(get_add, iterator_numbers))

    # for num in numbers:  # TODO напечатать первые 10 чисел
    #     print(num)  # TODO с помощью next получать следующий элемент от итератора
    for _ in range(10):  # TODO напечатать первые 10 чисел
        print(next(numbers))  # TODO с помощью next п

if __name__ == "__main__":
    task()
