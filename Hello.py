#!/usr/bin/env python3
# -*- coding: utf-8 -*-

s = 'Python-中文'
print(s)
b = s.encode('utf-8')
print(b)
print(b.decode('utf-8'))
s1 = 72
s2 = 85
r = (s2 - s1) / s1 * 100
print(f'小明成绩提高了{r:.2f}%')
print('Hello,{0}成绩提高了 {1:.2f} %'.format('小明',r))
print('小明的成绩提高了%.2f %%' % (r))
print(ord('a'))
