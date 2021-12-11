n, k = eval(input("please input n,k: "))
a = []
count = 0
num = 1
for i in range(n):
    a.append([i+1, 0])
while len(a) > 1:
    a[count][1] = num
    if num % k == 0 or (num-k) % 10 == 0:
        del a[count]
        num += 1
        if count == len(a):
            count = 0
        continue
    else:
        num += 1
        count += 1
        if count == len(a):
            count = 0
print(a[0][0])

