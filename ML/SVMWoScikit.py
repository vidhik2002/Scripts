import math, numpy


n = int(input("n:"))

pos, neg = [], []
#Positive elements
print("pos")
for i in range(n):
    pos.append([float(input("X:")),])
for i in range(n):
    pos[i].append(float(input("Y:")))

#Negative elements
print("neg")
for i in range(n):
    neg.append([float(input()),])
for i in range(n):
    neg[i].append(float(input()))

# Support vectors
sup = [[1,0],[3,1],[3,-1]]

# Augmented supports
asup = [[1,0,1],[3,1,1],[3,-1,1]]
ns = 3


def matmul(l1, l2):
    return sum(l1[i]*l2[i] for i in range(3))


consts = []
eqd = []
for i in range(3):
    temp = []
    for j in range(3):
        temp.append(matmul(asup[i], asup[j]))
    consts.append(temp)
    if sup[i] in pos:
        eqd.append(1)
    else:
        eqd.append(-1)

sols = numpy.linalg.solve(numpy.array(consts, dtype='f'), numpy.array(eqd, dtype='f'))

w1, w2, b = 0, 0, 0
for i in range(3):
    w1 += sols[i]*asup[i][0]
    w2 += sols[i]*asup[i][1]
    b += sols[i]*asup[i][2]
print(f"[{int(w1)},{int(w2)}]")
print(int(b))