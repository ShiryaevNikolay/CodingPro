n = int(input("Введите кол-во чисел: "))
a = []
for i in range(2, n+1):
    a.append(i)
    print(a[i-2], end=' ')
print()
p = 2
p_default = p
for k in range(5):
    for i in range(n - 1):
        x = 2
        while a[i] >= p:
            p = p_default * x
            if a[i] != 0 and a[i] % p == 0:
                a[i] = 0
            x += 1

    for i in range(n - 1):
        print(a[i], end=' ')

    j = 0
    while a[j] <= p_default and j < n-2:
        j += 1
    p = a[j]
    p_default = a[j]
    print(p_default)