import time
import random

def check_int_decorator(fn):
    def wrapper(*args, **kwargs):

        for index, value in enumerate(args):
            if not isinstance(value, (str, list, set, tuple, dict)):
                raise TypeError(f"Позиционный аргумент {index+1} со значением = "
                                f"{value} тип {type(value)}"
                                f" не является итерируемым)")
        #Тут вопрос из условия задачи у kwargs ключ тоже считать что
        # не может быть int)????
        #т.е. ключ только str или tuple(неизменяемые)
        for index, value in kwargs.items():
            if not isinstance(value, (str, list, set, tuple, dict)):
                raise TypeError(f"Позиционный аргумент с именем {index} со значением = "
                                f"{value} тип {type(value)}"
                                f" не является итерируемым)")

        st_time = time.time()
        print(st_time)
        result = fn(*args, **kwargs)
        time.sleep(random.randint(1, 3))
        end_time = time.time()
        print(f"Время выполения {end_time - st_time}")
        return result
    return wrapper


@check_int_decorator
def get_int(*args, **kwargs):
    print(args)
    print(kwargs)
    print("Успех")

    return


if __name__ == "__main__":
    print(get_int([4, 6, 5], 'dfr', d1 = "bcd", e1 = "[5, 6, 9]"))


    print(get_int([4, 6, 5], 'dfr', d1="bcd", e1=10))

    #print(get_int(1, '2', 'd'))

