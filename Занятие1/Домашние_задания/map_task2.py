# Задание 2.
# Напишите программу Python для разделения заданного словаря списков
# на список словарей с помощью функции map().
#
# Пример:
# INPUT:  {"Наука": [88, 89, 62, 95], "Язык": [77, 78, 84, 80]}
# OUTPUT: [{'Наука': 88, 'Язык': 77}, {'Наука': 89, 'Язык': 78}, {'Наука': 62, 'Язык': 84}, {'Наука': 95, 'Язык': 80}]


#def dict_to_list(elem_dict_key, elem_dict_number):
def dict_to_list(elem_dict_key):

    print(elem_dict_key, type(elem_dict_key)) #elem_dict_number, type(elem_dict_number))


    # str1 = str(elem_tuple[0])
    # str2 = str(elem_tuple[1])
    # str3 = str1 + ' ' + str2
    return elem_dict_key

    #return str(elem_tuple[0] + " " + str(elem_tuple[1]))


if __name__ == "__main__":

    dict_ = {"Наука": [88, 89, 62, 95], "Язык": [77, 78, 84, 80]}
    #for key, value in dict_.items():
     #   print(key, type(key), value, type(value))
    #print(dict_.keys(), dict_.values())
    #list_ = map(dict_to_list, dict_.keys(), dict_.values())
    list_ = map(dict_to_list, dict_.get("Наука"))
    print(list(list_))