"""Написать декоратор, сохраняющий результат в файл output.txt помимо возвращения.
 Результаты должны накапливаться в файле."""
import time

OUTPUT_FILE = "output.txt"

def time_decorator(fn):
    print("Этот код будет выведен в момент декорирования функции")

    def wrapper(*args, **kwargs):
        print("Этот код будет выполняться перед каждым вызовом функции")

        start = time.time()
        result = fn(*args, **kwargs)
        print(time.time()-start)
        with open(OUTPUT_FILE, "a") as f:
            f.write(f"time: {start} -> result: {result}\n")
        print("Этот код будет выполняться после каждого вызова функции")
        return result
    return wrapper


@time_decorator
def pow_(a, n):
    return pow(a, n)

#a = time_decorator(pow_(5, 2))

if __name__ == "__main__":
    print(pow_)
    print("=" * 25)

    print(pow_(5, 2))
    print("=" * 25)

    print(pow_(4, 4))
    print(pow_(3, 5))