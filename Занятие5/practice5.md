
# Task 3*

Написать генератор бесконечной волны, который будет "гонять" строку влево и
вправо пока будет происходить вызов генератора.

Можно сделать не со строкой, а с символами, где текущий знак будет заменяться на
другой символ

```
# example 1     example 2
"Hello"         "*---"
"hEllo"         "-*--"
"heLlo"         "--*-" 
"helLo"         "---*"
"hellO"         "--*-"
"helLo"         "-*--"
"heLlo"         "*---"
"hEllo"
"Hello"
```

# Task 4

Найти слово в строке с наивысшей оценкой.

Оценку слов проводить по буквам (символы не оцениваются), в соответсвии с
позицией в алфавите (регистр можно не учитывать):

```
# example
а=1, б=2, в=3 и т.д.
```

Если два слова имеют одинаковый балл, верните слово, которое встречается раньше.

# Task 5

"Вывернуть" строку

Вам дается строка слов, для каждого слова в строке вам нужно вывернуть слово
«наизнанку». Под этим подразумевается, что внутренние буквы будут выдвигаться
наружу, а внешние буквы двигаться к центру.

Если слово четной длины, все буквы переместятся. Если длина нечетная, ожидается,
что вы оставите «среднюю» букву слова на месте.

```
# example
male => amel
mouse => omues
```

# Task 6*

Создайте функцию, которая принимает римское число в качестве аргумента и
возвращает его значение как числовое десятичное целое число.

Современные римские цифры записываются, выражая каждую десятичную цифру числа,
которое нужно кодировать отдельно, начиная с крайней левой цифры и пропуская
любые нули. Таким образом, 1990 год отображается как «MCMXC» (1000 = M, 900 =
CM, 90 = XC), а 2008 год отображается как «MMVIII» (2000 = MM, 8 = VIII). В
римской цифре 1666 года «MDCLXVI» каждая буква используется в порядке убывания.

```
roman_to_int('XXI') => 21

Значения римских цифр

Symbol    Value
I          1
V          5
X          10
L          50
C          100
D          500
M          1,000
```

# Task 7

Написать функцию, которая будет создавать тестового пользователя. Можно
использовать в дальнейшем для генерации тестовых данных.

Данные пользователей должны различаться и валидироваться в зависимости от поля,
т.е. email должен быть формата email, phone - телефон нашего региона (т.е. +7).

Имя и фамилию сначала можно генерировать случайно (необязательно человеческие),
на ваш выбор они могут быть на русском или на английском.

Дополнительно:

* посмотреть библиотеки, которые могут генерировать человеческие :) имена и
  фамилии, попробовать поработать с ними для генерации name и surname
* продумать какие поля ещё можно добавить или добавить функционал для генерации
  только тех полей, которые будут указаны в параметрах
* сгенерировать n-пользователей и добавить в файл (можно формата json)

```
# example

generate_person() => {name: "Иван", 
                      surename: "Иванов", 
                      login: "@cool_ivan",
                      password:"qwerty", 
                      email:"abc@abc.com",
                      phone:"+7(123)456-78-99",
                      register_time: 2021-02-25T13:25:13}
```

# Task 8

Написать функцию, которая будет текущее время конвертировать в формат заданный
пользователем

```
time_from_pattern(time.time(), "YYYY-mm-dd") => "2021-12-22"
```

