# # Task 5
#
# "Вывернуть" строку
#
# Вам дается строка слов, для каждого слова в строке вам нужно вывернуть слово
# «наизнанку». Под этим подразумевается, что внутренние буквы будут выдвигаться
# наружу, а внешние буквы двигаться к центру.
#
# Если слово четной длины, все буквы переместятся. Если длина нечетная, ожидается,
# что вы оставите «среднюю» букву слова на месте.
#
# ```
# # example
# male => amel
# mouse => omues
# ```

def wrong_side(word):
    center = int(len(word) / 2)
    if len(word) % 2 == 0:
        first_revers = "".join(reversed(word[0:center]))
        second_revers = "".join(reversed(word[center:]))
        print(first_revers + second_revers)
    else:
        first_revers = "".join(reversed(word[0:center]))
        second_revers = "".join(reversed(word[center+1:]))
        print(first_revers + word[center] + second_revers)

wrong_side("example")
wrong_side("abcdef")