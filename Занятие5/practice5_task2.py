# # Task 2
# Скрипт имитирующий зрительскую волну для строки.
# Строка ввода всегда будет в нижнем регистре, но может быть пустой.
# Если символ в строке является пробелом, пропустите его.
#
def volna(str_):
    for j in range(len(str_)):
        if str_[j] != " ":
            up_sym = str_[j].upper()
            print(f"{str_[:j]}{up_sym}{str_[j + 1:]}")

volna('ааааааххххххххффффф ccccccchhhhh')