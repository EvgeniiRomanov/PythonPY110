#from itertools import pairwise
from itertools import count

# def pairwise(iterable):
#     for i in range(len(iterable) - 1):
#        yield iterable[i], iterable[i+1]

def pairwise(str_: str) -> tuple:

    j = 0
    while j < len(str_)-1:
        yield str_[j], str_[j + 1]
        j += 1


def task():
    for i in pairwise("ABCDEFGHIK"):
        print(f"{i[0]}{i[1]} ", end=" ")


if __name__ == "__main__":
    task()



# if __name__ == "__main__":
#     pts = [
#         (3, 4),
#         (4.5, 3),
#         (2.1, -1),
#         (6.8, -3),
#         (1.4, 2.9)
#     ]
