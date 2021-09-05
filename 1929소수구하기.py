min, max = map(int,input().split())

for i in range(min,max+1):
    tmp = 0
    for j in range(2,i):
        if i%j == 0:
            break
        else:
            tmp += 1
    if tmp + 2 == i:
        print(i)