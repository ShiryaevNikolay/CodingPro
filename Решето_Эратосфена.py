n = int(input("Введите кол-во чисел: "))
a = []
for i in range(2, n+1):
    a.append(i)
    print(a[i-2], end=' ')
print()
p = 2
p_default = p
while p*p <= n:
    for i in range(n - 1):                  # Вычёркиваем
        x = 2                               # в списке
        while a[i] >= p:                    # числа
            p = p_default * x               # от
            if a[i] != 0 and a[i] % p == 0: # "2p"
                a[i] = 0                    # до
            x += 1                          # "n"

    for i in range(n - 1):      # Вывод результат после
        print(a[i], end=' ')    # кождого прохода

    j = 0                                   # Поиск
    while a[j] <= p_default and j < n-2:    # первого
        j += 1                              # незачёркнутого
    p = a[j]                                # числа
    p_default = a[j]                        # в списке,
    print(p_default)                        # большего "p"