<<<<<<< HEAD

T=int(input())
L = []
L = list(map(int,input().strip().split()))
cnt=0
# print(L)
for i in L:
    tmp=0
=======
import sys
T=int(input())
L = []*T
L = list(map(int,input().strip().split()))
cnt=0
for i in L:
    tmp=0
    
>>>>>>> e44bdef1b4fc540e8f751d9405caa3fee7580e05
    for j in range(1,i):
        if i%j != 0:
            tmp+=1
    if tmp + 2 == i:
        cnt+=1
print(cnt)