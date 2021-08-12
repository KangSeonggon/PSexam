import itertools
T = int(input())
tempset = set()
temp = T//3
templist = [i for i in range(temp+1)]
testcase = list(itertools.product(templist,repeat=2))
#print(testcase, templist)
while True:
    proceed = False
    for i in testcase:
        ans = 3*i[0]+5*i[1]
        tempset.add(ans)
        if T in tempset:
            proceed = True
            break
    if proceed == True:
        print(i[0]+i[1])
        break
    elif T not in tempset:
        print(-1)
        # print(tempset)
        break
        print(1)
