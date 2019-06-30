import os

while True:
    try:
        print("Выберите вашу операционную систему:\n    1) Windows\n    2) Linux")
        OS = int(input("Введите номер ОС: "))
        if OS > 0 and OS < 3:
            break
        else:
            print("Такой ОС в списке нет или введено отрицательное (или 0) число.")
    except ValueError:
        print("Некорректный ввод! Введите целове положительное число.")

if OS == 1:
    path = 'D:/'
else:
    path = '/home/'

format_check = input("Введите формат файлов (файла), которые нужно найти: ")
format = ''
for i in range(len(format_check) - 1, -1, -1):
    if format_check[i] != '.':
        format += format_check[i]
    else:
        break

format = format[::-1]

for rootdir, dirs, files in os.walk(path):
    for file in files:
        if((file.split('.')[-1]) == format):
            print(os.path.join(rootdir, file))