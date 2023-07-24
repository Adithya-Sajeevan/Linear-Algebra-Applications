def interchange(M, r1, r2): #Function for interchanging any two rows
    rt = M[r1]
    M[r1] = M[r2]
    M[r2] = rt
    return M

def const_multiplication(R, k): #Function for multiplying a row by a non-zero scalar
    for d in range(len(R)):
        R[d] = k*R[d]
    return R
    
def elementary_row_addition(R1, R2, k): #Function for multiplying a row with a non-zero scalar and then add it to another row
    for d in range(len(R1)):
        R1[d] = round(R1[d] + k*R2[d], 5)
    return R1

def sop(M, n, i, X): #Function for adding up product of coefficients a[i][j] (i < j) with corresponding x[j] value during back substitution
    s = 0
    for j, x in zip(range(i + 1, n - 1), range(len(X)-1, -1, -1)):
        s = s + M[i][j]*X[x]
    return s

import math #For using floor() function

m = int(input("Input no. of equations: "))
n = m + 1
#m and n will be no. of rows and columns of augmented matrix A|B respectively

print()
print("Input the augmented matrix A|B:")

A = list()
for i in range(m):
    R = [j for j in input().split(' ')]
    for k in range(n):
        if (len(R[k].split('/')) == 2):
            R[k] = int(R[k].split('/')[0]) / int(R[k].split('/')[1])
        else:
            R[k] = int(R[k])
    A = A + [R]
    R = list()
A.sort(); A.reverse()

for q in range(n - 1):
    zc = 0; zr = 1; e = 0
    S = set(A[m - 1])
    if (S == {0}):
        zc = 1
    #Checks if there is zero row in the augmented matrix or if the system is linearly dependent
        
    if (zc == 1):
            if (q == 0):
                e = 1
                break
            else:
                e = 3
                break
    else:
        zr = 1
        for c in range(q, m):
            if (A[c][q] != 0):
                A = interchange(A, c, q)
                zr = 0
                break
        #Checks if the system consists of m equations with no. of unknowns not equal to m

        if (zr == 0):
            for a in range(q + 1, m):
                if (A[a][q] == 0):
                    continue
                else:
                    mu = A[a][q] / A[q][q]
                    A[a] = elementary_row_addition(A[a], A[q], -mu)
        else:
            e = 2
            break
        
#Back substitution
if ((zr == 0) and (zc == 0)):
    X = [A[m - 1][n - 1] / A[m - 1][n - 2]]
    for b in range(m - 2, -1, -1):
        X = X + [(A[b][n - 1] - sop(A, n, b, X)) / A[b][b]]
    X.reverse()
    for r in range(m):
        if (X[r] == math.floor(X[r])):
            X[r] = math.floor(X[r])

print()
if ((zr == 0) and (zc == 0)):
    print("The solution to this system is")
    for y in range(m):
        print("x{} = {}".format(y + 1, X[y]))
else:
    if (e == 1):
        print("Zero row is present")
    elif (e == 2):
        print("Inconsistent system - No solution")
    elif (e == 3):
        print("Linearly dependent system")
    if (e != 2):
        print("Cannot be solved using Gaussian elimination")
