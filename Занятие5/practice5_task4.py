# Найти слово в строке с наивысшей оценкой.
# Оценку слов проводить по буквам (символы не оцениваются), в соответсвии с
# позицией в алфавите (регистр можно не учитывать):
#
# ```
# # example
# а=1, б=2, в=3 и т.д.
# ```
#
# Если два слова имеют одинаковый балл, верните слово, которое встречается раньше.

def get_rus_alphabet_with_weight():
    """Функция возвращает русский алфавит с весами для каждой буквы без Ё"""
    # Можно попробовать возвращать в соответствии с кодировкой, т.к. там символ тоже
    # идут в порядке возрастания
    alphabet_weight = {}
    alphabet_start = ord('а')
    rus_alphabet = ''.join([chr(i) for i in range(alphabet_start, alphabet_start + 32)])
    for weight, char in enumerate(rus_alphabet, 1):
        alphabet_weight.update({char: weight})
    #print(alphabet_weight)
    return alphabet_weight

def get_word_with_max_weight(input_string):
    """Функция возвращает самое 'весомое' слово"""
    #print(input_string)
    word_weight_list = []
    alphabet_weight = get_rus_alphabet_with_weight()
    word_list = input_string.split(" ")
    #print(word_list)
    for word in word_list:
        word_weight = 0
        for char in word:
            word_weight += alphabet_weight.get(char, 0)
        word_weight_list.append(word_weight)
    return word_list[word_weight_list.index(max(word_weight_list))]

str_ = "мама мыла раму"
print(get_word_with_max_weight(str_))