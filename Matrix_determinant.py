from random import randint

matrix = []

while True:
    try:
        n = int(input("Введите степень матрицы: "))
        if n > 0:
            break
    except ValueError:
        print("Некорректный ввод! Введите целое положительное число.")
#============================================================================================
for i in range(n):                              #
    matrix.append([])                           # Заполнение матрицы
    for j in range(n):                          # и вывод на экран
        matrix[i].append(randint(-9, 10))       #
    print(matrix[i])                            #
#============================================================================================
#print(matrix)
print("\n")

def determinant(i_det, det_matrix):
    opred_matrix = 0
    if len(det_matrix) == 1:
        return det_matrix[i_det][i_det]
    min_matrix = []
    for i in range(i_det, len(det_matrix)):
        index = 0
        for j in range(i_det + 1, len(det_matrix)):
            min_matrix.append([])
            for k in range(i_det, len(det_matrix)):
                if k != i:
                    min_matrix[index].append(det_matrix[j][k])
            print(min_matrix[index])
            index += 1
            #determinant(0, det_matrix)
        if i % 2 == 0:
            opred_matrix = opred_matrix + determinant(0, min_matrix) * det_matrix[0][i]
        else:
            opred_matrix = opred_matrix - determinant(0, min_matrix) * det_matrix[0][i]
        print(opred_matrix)
        min_matrix = []
    return opred_matrix
        #print("\n")


determinant(0, matrix)