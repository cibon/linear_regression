# -*- coding: utf-8 -*-

import numpy as np
from numpy.linalg import inv
from numpy import dot
from numpy import mat

A = np.mat([1,1])
print('A:\n', A)
# print('A.T:\n', A.T)
print(A.reshape(2,1))
print('----------------------------')

B = mat([[1,2],[2,3]])

print('B:\n', B)
print(B.reshape(1, 4))
print('----------------------------')
print('B的逆:\n', inv(B))
print(B[0, :])
print(B[:, 0])

# A 1*2 B 2*2
print('A.B:', dot(B, A.T))
