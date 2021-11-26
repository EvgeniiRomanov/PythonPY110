import time
import random

def check_int_decorator(fn):
    def wrapper(*args):

        for index, value in enumerate(args):
            if not isinstance(value, int):
                 raise TypeError("Позиционный аргумент не int")
        st_time = time.time()
        print(st_time)
        result = fn(*args)
        time.sleep(random.randint(1, 3))
        end_time = time.time()
        print(f"Время выполения {end_time - st_time}")
        return result
    return wrapper


@check_int_decorator
def get_int(a, b, c) -> int:
    return a+b+c


if __name__ == "__main__":
    print(get_int(4, 6, 5))

    print(get_int(1, '2', 'd'))

