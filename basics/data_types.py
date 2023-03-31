"====================Переменные===================="
# переменные - это именновванные ссылки на ячейки памяти, где хранятся какие-то данные, для дальнейшего использования, при обращении к названию переменной
num1 = 7
num2 = 10
print(num1 + num2) # 17

"=================Ввод и вывод данных================="
# input - функция, которая позволяет принимать данные с терминала
# print - функция, которая позволяет выводить данные в терминал

number = input("Введите число: ")
print("Введенное число -", number)

"===========Правила наименования переменных==========="
a = 5 # можно, но не совсем понятно
# 1num = 10  # нельзя начинать с чисел
hello_world = 'hello world' # для разделителя можно использовать только _
# print = 'print' # нельзя назвать переменные уже встроенными названиями
# if = 4  не получится использовать в качестве переменных ключевые слова

# Snake Case - python стиль написания переменных
hello_world_aaa_bbb = ''

# Camel Case - стиль написания переменных во всех других яп
helloWorldAaaBbb = ''

"================Типы данных в Python================"

# неизменяемые
int_ = 17
float_ = 34.0
str_ = 'hello 123'
bool_1 = True
bool_2 = False
none_ = None
tuple_ = (1,2,3,4,5,6,7,8,9,10)

# изменяемые
list_ = [1,2,3,4,5,6,7,8,9,10]
set_ = {1,2,1,4} # {1,2,4}
dict_ = {'a':1, 'b':2, 'c':3}
