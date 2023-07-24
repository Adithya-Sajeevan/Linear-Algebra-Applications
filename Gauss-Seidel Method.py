m = int(input("Enter the number of equations: "))
#m = no. of rows of coefficient matrix A or augmented matrix A|B
#for augmented matrix A|B if n = no. of columns then n = m + 1
print()
print("Enter the augmented matrix A|B:")

#enter augmented matrix A|B
A = list()
for i in range(m):
    R = [h for h in input().split(' ')]
    
    #loop to convert fractional input (a/b form) to decimal
    for j in range(m + 1):
        Frac = R[j].split('/')
        if (len(Frac) == 1):
            R[j] = float(Frac[0])
        else:
            R[j] = float(Frac[0]) / float(Frac[1])
            
    A = A + [R]
    R = list()
print()

#check if the matrix is diagonally dominant or not
e = 0 #variable, initially set as 0, to indicate matrix is diagonally dominant
for i in range(m):
    S = 0
    for j in range(m):
        if (i != j):
            S = S + abs(A[i][j])
    if (abs(A[i][i]) <= S):
        e = 1 #indicates matrix is not diagonally dominant
        break

if (e == 0):
    print("The coefficient matrix A is diagonally dominant.")
    print()
else:
    print("The coefficient matrix A is not diagonally dominant.")
    print()

#initial guess
X = [x for x in input("Enter the initial approximation: ").split(' ')]
for g in range(m):
    Frac = X[g].split('/')
    if (len(Frac) == 1):
        X[g] = float(Frac[0])
    else:
        X[g] = float(Frac[0]) / float(Frac[1])
print()

#solve using Gauss - Seidel Elimination
for h in range(100):
    for i in range(m):
        Sum = 0
        for j in range(m):
             if (i != j):
                Sum = Sum + (A[i][j] * X[j])
        X[i] = (A[i][m] - Sum) / A[i][i]
    if (h in {0, 97, 98, 99}):
        print("Iteration {}: X = {}".format(h+1, X))
        print()

#display the result
if (e == 0):
    print("Solution of the system after 100 iterations is,")
else:
    print("Solution of the system appears after 100 iterations as,")
for x in range(m):
    print("x{} = {}".format(x+1, X[x]))
