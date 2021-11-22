# Задание 2.
# Напишите скрипт для сортировки списка кортежей по второму элементу с помощью Lambda.

def sort_tuple2(tuple_):

    tuple_.sort(key=lambda x: x[1])

    return tuple_


if __name__ == "__main__":

    list_tuple = [(1, 2), (3, 5), (2, 1), (7, 0, 4), (1, 9)]

    #list_tuple.sort(key=lambda x: x[1])
    print(sort_tuple2(list_tuple))