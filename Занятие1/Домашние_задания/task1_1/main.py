import itertools

def enum_zip(list1):

    #return list(zip(range(len(list1)), list1))

    return list(zip(itertools.count(0), list1))


if __name__ == "__main__":
    list_ = [1, 4, 6, 8, 4, 2]
    for elem, value in enumerate(list_):
        print(elem, value)

    print(enum_zip(list_))
