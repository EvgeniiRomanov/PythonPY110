from itertools import repeat

def task() -> list:
    temp_tuple = (0, 36.6, 100)
    temp_ = map(lambda x: (x * 9/5) + 32, temp_tuple)
    #return ...  # TODO  вернуть список температур по Фаренгейту
    return list(map(round, temp_, repeat(2)))

if __name__ == "__main__":
    print(task())
