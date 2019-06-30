n = int(input("Введите число, у которого нужно посчитать простые множества: "))

factors = []

def findFactors(n):
    i = 2
    while i < n:
        while n % i == 0:
            factors.append(i)
            n = n // i
        i = i + 1
    if n > 1:
        factors.append(n)
    return factors

print(findFactors(n))