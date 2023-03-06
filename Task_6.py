c = 0
a = [int(i) for i in input().split()]
for i in range(1, len(a)):
    if a[i] > a[c]:
        c = i
print(a[c], c)
