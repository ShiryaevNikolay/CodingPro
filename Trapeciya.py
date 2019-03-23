from math import sin


def f(x):
    return 1 + x + sin(2*x)

def d(x_min, x_max, num):
    dx = (x_max - x_min) / num
    ploshad = 0
    x = x_min
    for i in range(num):
        ploshad = ploshad + (f(x) + f(x + dx)) / 2 * dx
        x = x + dx
    return ploshad
 
print(d(0, 3, 12))