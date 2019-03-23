a = int(input("Введите первное чилос: "))
b = int(input("Введите второе чилос: "))

def gcd(a, b):
    while (b !=0):
        remainder = a % b
        a = b
        b = remainder
    return a

print(gcd(a, b))