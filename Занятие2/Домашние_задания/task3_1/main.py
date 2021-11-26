def output_type_list(fn):
    def wrapper(*args, **kwargs):

        result = list(fn(*args, **kwargs))
        if not isinstance(result, list):
            raise TypeError(f"Результатом выполнения функции {fn} должен быть список")
    print("Успех")
    return wrapper


@output_type_list
def return_list() -> list:
    return []


@output_type_list
def return_tuple() -> str:
    return ""


if __name__ == "__main__":
    return_list()
    return_tuple()
