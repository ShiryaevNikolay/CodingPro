from random import randint

array = []

while True:
    try:
        n = int(input("Введите размер массива: "))
        if n < 1:
            print("Размер массива не может быть отрицательным.")
        else:
            break
    except ValueError:
        print("Некорректный ввод!")

for i in range(n):
    array.append(randint(1,100))
print(array)


def fast_sort(array_def):
    if len(array_def) <= 1:  # Возвращает элемент, если в массиве только один или отсутствуют элементы
        return array_def
    else:  # Рекурсия
        pivot = array_def[0]
        less = []
        large = []
        for i in array_def[1:]:
            if i < pivot:
                less.append(i)  # Массив всех елементов, меньших опорного
            else:
                large.append(i)  # Массив всех элементов, больших опорного
        return fast_sort(less) + [pivot] + fast_sort(large)


print(fast_sort(array))