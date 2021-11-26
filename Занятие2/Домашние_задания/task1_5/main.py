from string import digits, ascii_letters
import random
from itertools import count
#from traceback import print_exc

def password_min_8symbols(lenght_ = 8):

    #while True:
    for _ in count(1):
        tmp_pwd = random.sample(digits+ascii_letters, lenght_)
        random.shuffle(tmp_pwd)

        yield "".join(tmp_pwd)


if __name__ == "__main__":

    while True:
        try:
            n = int(input("Введите желаемую длину пароля: "))
            if n < 8:
                print(f"Вы ввели длину пароля {n}, это слабый пароль, будет сгенерирован пароль из 8 символов")
                break
            else:
                print(f"Вы ввели длину пароля {n}, это стойкий пароль")
                break
        except ValueError:
            print("Вы ввели не число, попробуйте снова")

    # while True:
    #     try:
    #         n = int(input("Введите желаемую длину пароля: "))
    #     except ValueError:
    #         print_exc("Вы ввели не число, поробуйте снова")
    #     else:
    #         break

    n = 8 if n < 8 else n

    my_count = password_min_8symbols(n)

    for i in range(5):
         print(next(my_count))

