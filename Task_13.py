a = input().split()
l = 0
for i in range(len(a)):
    for y in range(i +1, len(a)):
        if a[i] == a[y]:
            l+=1
print(l)