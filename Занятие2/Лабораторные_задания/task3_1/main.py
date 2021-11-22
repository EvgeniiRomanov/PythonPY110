from traceback import print_exc

def positive_check(fn):
    def wrapper(arg):
        # TODO написать проверку положительности аргумента arg
        if arg < 0:
            raise ValueError("У Вас ошибка")
        result = fn(arg)
        return result

    return wrapper


# TODO задекорировать функцию
@positive_check
def some_func(num: int):
    print(num)


if __name__ == "__main__":
    some_func(5)  # всё хорошо

    some_func(-5)  # должна быть вызвана ошибка ValueError
