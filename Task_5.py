a = [int(i) for i in input().split()]
y = 0
for i in range(1, len(a) - 1):
    if a[i - 1] < a[i] > a[i + 1]:
        y += 1
print(y)
