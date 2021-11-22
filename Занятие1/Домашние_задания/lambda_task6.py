# Задание 6.
# Напишите скрипт, чтобы найти максимальное значение в заданном неоднородном списке с помощью лямбда.
# Пример списка: ['Python', 3, 2, 4, 5, 'version']

if __name__ == "__main__":

    # list_ = [3, 'a', 'tre', 15, 2, 10, 4, 12, 13]

    # list1 = [str(x) for x in list_]
    # k = list(filter(str.isdigit, list1))
    # k1 = [int(x) for x in k]
    # print(max(k1))

    list_ = [3, 'a', 'gagaga', 'tre', 17, 2, 10, 4, 12, -13]

    list_int = filter(lambda x: isinstance(x, int), list_)
    print(max(list(list_int)))
