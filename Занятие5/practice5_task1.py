# # Task 1
#
# Скрипт для конвертации списка с 1 и 0, в целочисленное значение.
#
# Списки могут иметь разную длину.
#
# ```
# # example
# [0, 1, 1, 0] ==> 6
# [1, 1, 1, 1] ==> 15
# ```


list_1 = [0, 1, 1, 0, 1]
str_ = "".join(map(str, list_1))
dec_ = int(str_, 2)
print(dec_)