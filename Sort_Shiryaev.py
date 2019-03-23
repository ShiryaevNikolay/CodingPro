from random import randint
N = 9
a = []
for k in range(N):
    a.append(randint(1, 50))
print(a)
print("------------------------------------------------------------")

for i in range(N-1):
    f = i
    for j in range(i+1, N):
        if a[j] < a[f]:
            f = j
    a_min = a[f]
    a[f] = a[i]
    a[i] = a_min
    print(a)

print("------------------------------------------------------------")
print(a)