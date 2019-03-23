from random import randint
N = 9
a = []
for k in range(N):
    a.append(randint(1, 50))
print(a)
print("------------------------------------------------------------")

i = N - 1
while i>0:
    for j in range(i):
        if a[j] > a[j+1]:
            t = a[j]
            a[j] = a[j+1]
            a[j+1] = t
            print(a)
    i -= 1
if a[i] > a[i+1]:
    t = a[i]
    a[i] = a[i+1]
    a[i+1] = t
print(a)

print("------------------------------------------------------------")
print(a)