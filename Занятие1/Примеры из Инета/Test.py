import itertools
import random

list_ = [random.randint(-10, 10) for _ in range(5)]
print(list_)


for _ in range(3):
    #a1 = itertools.count(1)
    a1 = itertools.cycle(list_)
    print(list(a1))
