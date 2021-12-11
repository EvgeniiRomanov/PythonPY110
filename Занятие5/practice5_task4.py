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

# def weight_rus_symbols():
#
#     alphabet_weight = {}
#     alphabet_start = ord('a')
#
#     rus_alphabet = ''.join([chr[j] for j in range(alphabet_start, alphabet_start + 32)])
#     for weight, char in enumerate(rus_alphabet, 1):
#         alphabet_weight.update({char: weight})
#
#
#     return alphabet_weight

