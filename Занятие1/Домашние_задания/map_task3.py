# Задание 3.
# Напишите скрипт для преобразования заданного списка кортежей в список строк с помощью функции map().

def tuple_to_str(elem_tuple):

    return str(elem_tuple[0] + " " + str(elem_tuple[1]))


if __name__ == "__main__":

    #list_ = [('red', 'pink'), ('white', 'black'), ('orange', 'green')]
    list_ = [('Sheridan', 'Gentry'), ('Laila', 'Mckee'), ('Ahsan', 'Rivas'), ('Conna', 'Gonzalez')]
    str_ = map(tuple_to_str, list_)
    print(list(str_))
