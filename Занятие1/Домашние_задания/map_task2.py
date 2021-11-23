# Задание 2.
# Напишите программу Python для разделения заданного словаря списков
# на список словарей с помощью функции map().
#
# Пример:
# INPUT:  {"Наука": [88, 89, 62, 95], "Язык": [77, 78, 84, 80]}
# OUTPUT: [{'Наука': 88, 'Язык': 77}, {'Наука': 89, 'Язык': 78}, {'Наука': 62, 'Язык': 84}, {'Наука': 95, 'Язык': 80}]

# Разбор на занятии

def dict_to_list(dict_):

    step1 = [[(k, v) for v in value] for k, value in dict_.items()]
    #print(step1)
    science = step1[0]
    lang = step1[1]

    step2 = list(zip(science, lang))
    #print(step2)
    for elem in step2:
        print(dict(elem))

        return list(map(dict, zip(science, lang)))


if __name__ == "__main__":

    dict_ = {"Наука": [88, 89, 62, 95], "Язык": [77, 78, 84, 80]}
    print(dict_)
    print(dict_to_list(dict_))