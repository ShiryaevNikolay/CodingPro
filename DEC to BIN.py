import re

while True:
    try:
        n = int(input("Введите число, которое нужно привести в двоичный вид: "))
        if n > 0:
            break
    except ValueError:
        print("Некорректный ввод! Введите целое положительное число.")


def binary_representation(x, h):
    c = x % 2
    x = x // 2
    h += str(c)
    if x > 0:
        return binary_representation(x, h)
    else:
        return print("\n", h[::-1], "\n")


def decimal_representation(x):
    string_number = str(x)
    number = 0
    for i in range(len(string_number)):
        number += (2 ** (len(string_number) - 1 - i)) * int(string_number[i])
    return print("\n", number, "\n")


binary_representation(n, "")

while True:
    try:
        n = int(input("Введите число в двоичном виде, чтобы привести в десятичный: "))
        if n > 0:
            string = str(n)
            check = r"[23456789]"
            if re.search(check, string):
                n = 1.2
            else:
                break
    except ValueError:
        print("Некорректный ввод! Чило должно состоять из 0 и 1.")

decimal_representation(n)
