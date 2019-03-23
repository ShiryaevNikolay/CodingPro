from math import sin


def f(x):
    return 1 + x + sin(2*x)

def d(x_min, x_max, num):
    dx = (x_max - x_min) / num
    total_area = 0
    x = x_min
    for i in range(num):
        total_area = total_area + dx * f(x)
        x = x + dx
    return total_area

print(d(0, 3, 12))
