# print('Hello world')

# print("Как тебя зовут?")
# name = input()
# print("Привет,", name)

# name = input("Как тебя зовут?")
# print("Привет,", name)

# name = input()
# age = input()
# print("Я", name, "и мне", age, "лет.")

# cat_name = input()
# print("Моего кота зовут", cat_name)

# print("a", "b", "c", sep="", end="")

# print("Python", end="\n\n\n")

# print("a", "b", "c", sep="*")
# print("d", "e", "f", sep="**", end="")
# print("g", "h", "i", sep="+", end="%")
# print("j", "k", "l", sep="-", end="\n")
# print("m", "n", "o", sep="/", end="!")
# print("p", "q", "r", sep="1", end="%")
# print("s", "t", "u", sep="&", end="\n")
# print("v", "w", "x", sep="%")
# print("y", "z", sep="/", end="!")


# a = 7
# b = 2
# print(a + b)
# print(a - b)
# print(a / b)
# print(a * b)

# num1 = 3 + 4 * 2
# num2 = (3 + 4) * 2
# print(num1)
# print(type(num1))

# num1 = int(input())
# num2 = int(input())
# print(num1 + num2)

# Преобразование типов
# s = "1"
# print(type(s))
# a = int(s)
# print(type(a))

# s = 1
# print(type(s))
# a = str(s)
# print(type(a))

# num1 = int(input())
# print(num1)
# print(num1 + 1)
# print(num1 + 2)


# Напишите программу, вычисляющую объем куба и площадь его полной поверхности по введенному значению длины ребра.
# v = a * a * a # обьем
# s = 6 * a * a # площадь

# edge = int(input())
# v = edge * edge * edge
# s = 6 * edge * edge
# print("Объем =", v)
# print("Площадь полной поверхности =", s)

# a = int(input())
# b = int(input())
# f = 3 * (a + b) * (a + b) * (a + b) + 275 * b * b - 127 * a - 41
# print(f)


# Напишите программу, которая считывает целое число, после чего на экран выводится следующее и предыдущее целое число с пояснительным текстом.

# num1 = int(input())
# print('Следующее за числом', num1, 'число:', num1 + 1)
# print('Для числа', num1, 'предыдущее число:', num1 - 1)


# a1 = int(input())
# d = int(input())
# n = int(input())
# an = a1 + d * (n - 1)
# print(an)

# num1 = int(input())
# print(num1, 2 * num1, 3 * num1, 4 * num1, 5 * num1, sep="---")

# print(2**0)
# print(2**1)
# print(2**2)
# print(2**3)
# print(2 ** (-1))

# b1 = int(input())
# q = int(input())
# n = int(input())
# bn = b1 * q ** (n - 1)
# print(bn)

# Напишите программу, которая находит полное число метров по заданному числу сантиметров.
# num1 = int(input())
# print(num1 // 100)

# n школьников делят k мандаринов поровну, неделящийся остаток остается в корзине. Сколько целых мандаринов достанется каждому школьнику? Сколько целых мандаринов останется в корзине?
# pupils = int(input())
# tengerines = int(input())
# print(tengerines // pupils)
# print(tengerines % pupils)

# import math

# number = int(input())
# a = math.ceil(number / 2)
# print(a)


# В купейном вагоне имеется 9 купе с четырьмя местами для пассажиров в каждом. Напишите программу, которая определяет номер купе, в котором находится место с заданным номером
# n = int(input())
# print((n + 3) // 4)


# a = 17 // (23 % 7)
# b = 34 % a * 5 - 29 % 4 * 3
# print(a * b)

# a = int(input())
# b = str(a + a)
# print(b)

# num = int(input())
# num1 = num // 100
# num2 = (num // 10) % 10
# num3 = num % 10
# print("Сумма цифр =", num1 + num2 + num3)
# print("Произведение цифр =", num1 * num2 * num3)

# n = int(input())
# a = n % 100 // 10
# print(a)

# Задача 1. Напишите программу, которая считывает одну строку.
# Если это строка «Python», программа выводит «ДА», в противном случае программа выводит «НЕТ».
# a = input()
# if a == "Python":
#     print("ДА")
# else:
#     print("НЕТ")

# Задача 2. Напишите программу, которая определяет, состоит ли двузначное число, введенное с клавиатуры, из одинаковых цифр.
# Если состоит, то программа выводит «ДА», в противном случае программа выводит «НЕТ».
# num = int(input())
# num1 = num // 10
# num2 = num % 10
# if num1 == num2:
#     print("ДА")
# else:
#     print("НЕТ")

# Задача 3. Напишите программу, которая считывает три числа и подсчитывает количество чётных чисел.
# num1 = int(input())
# num2 = int(input())
# num3 = int(input())
# if num1 % 2 == 0 and num2 % 2 == 0 and num3 % 2 == 0:
#     print(3)
# if num1 % 2 == 0 and num2 % 2 == 0 and num3 % 2 >= 1:
#     print(2)
# if num1 % 2 == 0 and num3 % 2 == 0 and num2 % 2 >= 1:
#     print(2)
# if num2 % 2 == 0 and num3 % 2 == 0 and num1 % 2 >= 1:
#     print(2)
# if num1 % 2 == 0 and num2 % 2 >= 1 and num3 % 2 >= 1:
#     print(1)
# if num1 % 2 >= 1 and num2 % 2 == 0 and num3 % 2 >= 1:
#     print(1)
# if num1 % 2 >= 1 and num2 % 2 >= 1 and num3 % 2 == 0:
#     print(1)

# num1, num2, num3 = int(input()), int(input()), int(input())
# counter = 0  # переменная счётчик
# if num1 % 2 == 0:
#     counter = counter + 1  # увеличиваем счётчик на 1
# if num2 % 2 == 0:
#     counter = counter + 1  # увеличиваем счётчик на 1
# if num3 % 2 == 0:
#     counter = counter + 1  # увеличиваем счётчик на 1
# print(counter)

# age = int(input())
# if age <= 13:
#     print("детство")
# if age >= 14 and age <= 24:
#     print("молодость")
# if age >= 25 and age <= 59:
#     print("зрелость")
# if age >= 60:
#     print("старость")


# Напишите программу, которая определяет, является ли заданное натуральное число трёхзначным
# num = int(input())
# if 100 <= num <= 990:
#     print("YES")
# else:
#     print("NO")

# Напишите программу, которая проверяет, что все три цифры натурального трёхзначного числа различны.
# num = int(input())
# first_number = num // 100
# second_number = num // 10 % 10
# third_number = num % 10
# if first_number != second_number != third_number:
#     print("Различные")
# else:
#     print("Одинаковые")


# Напишите программу, которая по координатам точки, не лежащей
# на осях координат, определяет номер координатной четверти, в которой она находится.


# number = int(input())
# if 999 < number < 10000:
#     if number % 7 == 0 and number % 17 == 0:
#         print("YES")
# else:
#     print("NO")

# Шахматы
# a, b, c, d = int(input()), int(input()), int(input()), int(input())
# if -1 <= a - c <= 1 and -1 <= b - d <= 1:
#     print("YES")
# else:
#     print("NO")


# Задача 1. Даны три целых числа. Определите, сколько среди них совпадающих. Программа должна вывести одно из чисел:
# 3 (если все совпадают),
# 2 (если два совпадает) или
# 0 (если все числа различны).

# ПЕРВЫЙ СПОСОБ Использование каскадного условного оператора
# a, b, c = int(input()), int(input()), int(input())
# if a == b == c:
#     print(3)
# elif a == b:
#     print(2)
# elif b == c:
#     print(2)
# elif c == a:
#     print(2)
# else:
#     print(0)

# второй способ Использование каскадного условного оператора и логического оператора or
# a, b, c = int(input()), int(input()), int(input())
# if a == b == c:
#     print(3)
# elif a == b or b == c or c == a:
#     print(2)
# else:
#     print(0)

# num1 = int(input())
# num2 = int(input())
# str1 = input()
# if str1 == "+":
#     print(num1 + num2)
# if str1 == "-":
#     print(num1 - num2)
# if str1 == "*":
#     print(num1 * num2)
# elif str1 == "/":
#     if num2 == 0:
#         print("На ноль делить нельзя!")
#     else:
#         print(num1 / num2)
# else:
#     print("Неверная операция")


# numbers = [1, 8, 3, 8, 2, 6, 8, 8]
# index = 0
# maximum = numbers[index]
# count_maximal = 0
# while index < numbers.length do
#     if numbers[index] > maximum then
#         maximum = numbers[index]
#         count_maximal = 1
#     else
#         if numbers[index] == maximum then
#             count_maximal = count_maximal + 1
#     index = index + 1
# print(count_maximal)

# print("БЕСКОНЕЧНОСТЬ", "НЕ", "ПРЕДЕЛ!", sep="_", end="!")

# print("БЕСКОНЕЧНОСТЬ", "НЕ", "ПРЕДЕЛ", sep="_", end="")
# print("!")

# print("БЕСКОНЕЧНОСТЬ_НЕ_ПРЕДЕЛ", end="")
# print("!")

# a = input()
# b = input()
# if a == "красный" and b == "синий":
#     print("фиолетовый")
# elif a == "красный" and b == "желтый":
#     print("оранжевый")
# elif a == "синий" and b == "желтый":
#     print("зеленый")
# else:
#     print("ошибка цвета")
# a = int(input())
# print(a % 2)

# a1, b1, a2, b2 = int(input()), int(input()), int(input()), int(input())
# if a1 < b1 and a2 < b2:
#     if b1 < a2:
#         print("пустое множество")
# elif b1 == a2:
#     print(a2)
# elif b1 > a2:
#     print(a2, b1)
# elif a1 > a2:
#     print(a1, b1)
