T = int(input())

for i in range(T):
    k = int(input())
    n = int(input())
    ps = [x for x in range(1,n+1)]
    
    for _ in range(k):
        for j in range(1,n):
            ps[j]+=ps[j-1]
    print(ps[-1])