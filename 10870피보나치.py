def Fibo(N):
    if N==0:
        return 0
    if N<=2:
        return 1
    else:
        return Fibo(N-1)+Fibo(N-2)
N = int(input())
print(Fibo(N))