def binaryRepresentation(x, h):
    c = x % 2
    x = x // 2
    h += str(c)
    if x > 0:
        return binaryRepresentation(x, h)
    else:
        return print(h[::-1])


binaryRepresentation(125, "")
