from random import randint
N = 9
a = []
for k in range(N):
    a.append(randint(1, 50))
print(a)
print("------------------------------------------------------------")

for i in range(N-1):
    j = i + 1
    k = i
    while a[j] < a[k]:
        t = a[j]
        a[j] = a[k]
        a[k] = t
        if k > 0:
            j -= 1
            k -= 1
        print(a)

print("------------------------------------------------------------")
print(a)