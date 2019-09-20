import numpy as np
import time

def strassen(A, B):

    A_m2 = int(A.shape[0] / 2)
    A_n2 = int(A.shape[1] / 2)
    B_m2 = int(B.shape[0] / 2)
    B_n2 = int(B.shape[1] / 2)

    A11 = A[:A_m2, :A_n2]
    A12 = A[:A_m2, A_n2:]
    A21 = A[A_m2:, :A_n2]
    A22 = A[A_m2:, A_n2:]

    B11 = B[:B_m2, :B_n2]
    B12 = B[:B_m2, B_n2:]
    B21 = B[B_m2:, :B_n2]
    B22 = B[B_m2:, B_n2:]

    S1 = B12 - B22
    S2 = A11 + A12
    S3 = A21 + A22
    S4 = B21 - B11
    S5 = A11 + A22
    S6 = B11 + B22
    S7 = A12 - A22
    S8 = B21 + B22
    S9 = A11 - A21
    S10 = B11 + B12

    P1 = np.dot(A11, S1)
    P2 = np.dot(S2, B22)
    P3 = np.dot(S3, B11)
    P4 = np.dot(A22, S4)
    P5 = np.dot(S5, S6)
    P6 = np.dot(S7, S8)
    P7 = np.dot(S9, S10)

    C11 = P5 + P4 - P2 + P6
    C12 = P1 + P2
    C21 = P3 + P4
    C22 = P5 + P1 - P3 - P7

    C1 = np.hstack((C11, C12))
    C2 = np.hstack((C21, C22))
    C = np.vstack((C1, C2))

    return C


# a = np.array([[1, 2], [3, 4]])
# b = np.array([[5, 6], [7, 8]])
a = np.random.rand(50, 50)
b = np.random.rand(50, 50)
t1 = time.time()
c = strassen(a, b)
t2 = time.time()
print(t2 - t1)
d = np.dot(a, b)
print(time.time() - t2)
# print(a)
# print('--------------------------')
# print(b)
# print('--------------------------')
# print(c)
# print('--------------------------')
# print(d)
