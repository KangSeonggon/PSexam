T = int(input())
# x,y= [],[]
templist = []
ans = []
for i in range(T):
    x,y = map(int,input().split())
    z = y-x # x y 두 지점 차이
    cnt=0
    if z == 1:
        ans.append(1)
        break
    else:
        while z > 0:
            cnt+=1
            z-=2*cnt
            print('--')
            print(cnt,z)
            if z == 0:
                ans.append(2*cnt)
                break
            elif z == cnt+1 or z == cnt:
                ans.append(2*cnt+1)
                break
            elif z < 0:
                ans.append(2*cnt)
                break
            
#1233321
for i in ans:
    print(i)

    # for j in range(1, y-x+1):
    #     temp = (j*j+j)/2
    #     templist.append(temp)
    #     if z < temp:
    #         # print("----------")
    #         # print(z)
    #         # print(temp)
    #         # print(templist)
    #         # print(j)
    #         # print(cnt+1)
    #         ans.append(cnt+1)
    #         break
    #     cnt+=1
