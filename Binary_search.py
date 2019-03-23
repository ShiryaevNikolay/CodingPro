from random import randint
N = 8
a = []
for k in range(N):
    a.append(randint(1, 50))
print(a)
print("------------------------------------------------------------")

for i in range(N-1):
    f = i
    for j in range(i+1, N):
        if a[j] < a[f]:
            f = j
    a_min = a[f]
    a[f] = a[i]
    a[i] = a_min


print("------------------------------------------------------------")
print(a)

n = int(input("Введите число: "))
l_1 = (N - 1) // 2
l_reserv = N
l_2 = 0
f = 0
while f == 0:
    if n == a[l_1]:
        f = 1
    else:
        if n < a[l_1]:
            l_reserv = l_1
            l_1 = l_2 + int((l_1 - l_2) / 2)
        else:
            if l_1 - l_2 > 1:
                if n > a[l_1]:
                    l_2 = l_1
                    l_1 = l_2 + int((l_reserv - l_1) / 2)
            else:
                if n == a[l_1]:
                    f = 1
                else:
                    if n == a[l_1 + 1]:
                        l_1 += 1
                        f = 1


print(l_1)