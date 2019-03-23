from math import sin


x_min = float(input("Введите минимальное значение X:"))
x_max = float(input("Введите максимальное значение X:"))
max_slice_error = float(input("Введите максимальное значение погрешности:"))
n = int(input("Введите число разбиений:"))


def f(x):
    return 1 + x + sin(2 * x)


x1 = x_min
x2 = x_max


def sliceArea(x1, x2, max_slice_error):
    y1 = f(x1)
    y2 = f(x2)
    xm = (x1 + x2) / 2
    ym = f(xm)
    area12 = (x2 - x1) * (y1 + y2) / 2.0
    area1m = (xm - x1) * (y1 + ym) / 2.0
    aream2 = (x2 - xm) * (ym + y2) / 2.0
    area1m2 = area1m + aream2
    error = (area1m2 - area12) / area12
    if abs(error) < max_slice_error:
        return area1m2
    return sliceArea(x1, xm, max_slice_error) + sliceArea(xm, x2, max_slice_error)


def useAdaptiveTrapezoidRule(x_min, x_max, n, max_slice_error):
    dx = (x_max - x_min) / n
    total_area = 0
    x = x_min
    for i in range(n):
        total_area += sliceArea(x, x + dx, max_slice_error)
        x += dx
    return total_area


print(useAdaptiveTrapezoidRule(x_min, x_max, n, max_slice_error))