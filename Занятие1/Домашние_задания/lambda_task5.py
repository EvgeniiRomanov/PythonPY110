# Напишите программу Python для поиска палиндромов
# в заданном списке строк с помощью Lambda

if __name__ == "__main__":

    list_ = ['казак', 'китолов', 'gagag', 'заказ', 'море']

    list_int = filter(lambda x: x if x[:] == x[::-1] else None, list_)
    print(f"В списке следующие Палиндромы: {list(list_int)}")
