# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 22:21:07 2023

@author: harik
"""

def eliminate(matrix):
    c = 0
    n = len(matrix)
    for p in range(1, n):
        if (matrix[c][p] or not matrix[p][c]):
            c = p
    return c
def check(c,matrix):
    for i in range(n):
        if matrix[c][i] is True:
            return False
    for i in range(n):
        if matrix[i][c] is False:
            if i != c:
                return False
    return True
n = int(input('Number of people: '))
m = [[False]*n for _ in range(n)]
 
for i in range(n):
    people = input('Enter list of people known to {}: '.format(i)).split()
    for p in people:
        p = int(p)
        m[i][p] = True
c = eliminate(m)
if check(c,m):
    print('{} is the celebrity.'.format(c))
else:
    print('There is no celebrity.')
