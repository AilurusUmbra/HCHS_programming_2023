import math
r = 3**(1.5)
a1 = 3

A = [0] + [a1*r**(i-1) for i in range(1,30)]
B = [ ((-1)**(n+1))*math.log(A[n],3) for n in range(1,29)]

for answer in range(23, 28):
    if (sum(B[:(answer)]) > 18):
        print(answer, ' ')
