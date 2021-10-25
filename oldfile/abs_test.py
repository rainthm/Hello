# -*- coding: utf-8 -*-
def my_abs(x):
    if not isinstance(x,(int, float)):
        raise TypeError('Bad operand type')
    if x >= 0 :
        return x
    else :
        return -x


#print('Input a num:')
#y = int(input('input:'))
#-9print('Input a num:'+str(y=input()))
#print(my_abs(y))