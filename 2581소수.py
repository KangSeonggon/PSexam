min = int(input())
max = int(input())
temp = []
breaker = True
for i in range(min,max+1):
    tmp = 0
    for j in range(2,i):
        if i%j == 0:
            break
        else:
            tmp+=1
    if tmp + 2 == i:
        temp.append(i)
if temp == []:
    print(-1)
else:
    print(sum(temp))
    print(temp[0])