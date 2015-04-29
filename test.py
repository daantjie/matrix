#!/usr/bin/env python

from matrix import *

M = Matrix([1, 2, 3],[4, 5, 6], [7, 8, 9])
print(M)
N = Matrix.Column([1, 2, 3], [4, 5, 6], [7, 8, 9])
print(N)
print(" --- ")
print(M + N)
print(" --- ")
print(M - N)
print(" --- ")
print(M*N)
print(" --- ")
print(N*M)
print(" --- ")
print(M*2)
print(" --- ")
print(2*M)
