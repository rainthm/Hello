# -*- coding: utf-8 -*-

import math

def quadratic(a, b, c):
    # ax^2 + bx + c = 0
    # x1 = (-b + sqrt(b^2 - 4 * a * c))/2/a
    # x2 = (-b - sqrt(b^2 - 4 * a * c))/2/a
    if (a != 0 and (b*b-4*a*c >=0)):
        x1 = (-b + math.sqrt(b*b - 4 * a * c))/2/a
        x2 = (-b - math.sqrt(b*b - 4 * a * c))/2/a
        return x1, x2
    elif a == 0 :
        print('这个不是二元一次方程')
    elif b * b - 4 * a * c < 0 :
        print('无解')

print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')
print('quadratic(0, 3, 1) =', quadratic(0, 3, 1))