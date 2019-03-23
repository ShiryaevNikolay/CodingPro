from random import randint

n = int(input("Введите кол-во элементов: "))

factors = []
for i in range(n):
    factors.append(randint(1, 200))

def findFactors(n):
    i = 2
    while i < n:
        while n % i == 0:
            factors.append(i)
            n = n / i
        i = i + 1
    if n > 1:
        factors.append(n)
    return print(factors)

print(findFactors(n))