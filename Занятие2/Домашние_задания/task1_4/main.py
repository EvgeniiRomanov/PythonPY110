#from itertools import pairwise
from itertools import count

# def pairwise(iterable):
#     for i in range(len(iterable) - 1):
#        yield iterable[i], iterable[i+1]

def pairwise(str_):
    for j in count(0):
        yield str_[j], str_[j+1]

def task():
    for i in pairwise("ABCDEFG"):
        print(i)


if __name__ == "__main__":
    task()
