import sys
T=int(input())
L = []*T
L = list(map(int,input().strip().split()))
cnt=0
for i in L:
    tmp=0
    
    for j in range(1,i):
        if i%j != 0:
            tmp+=1
    if tmp + 2 == i:
        cnt+=1
print(cnt)