x = int(input())
p = 2

while p <= x:
    if x % p == 0:
        print(p)
        x = x/p
    else:
        p = p+1