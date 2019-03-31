a = int(input("Введите первное число: "))
b = int(input("Введите второе число: "))

def gcd(a, b):
    while (b !=0):
        remainder = a % b
        a = b
        b = remainder
    return a

print(gcd(a, b))