# -*- coding: utf-8 -*-
def findMinAndMax(L):
    if len(L) == 0:
        return(None,None)
    Max = L[0]
    Min = L[0]
    for n in L:
        if n > Max:
            Max = n
        if n < Min:
            Min = n

    return(Min,Max)

#L = [1,5 ,7,3,19,0]
#print(findMinAndMax(L))
# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')
