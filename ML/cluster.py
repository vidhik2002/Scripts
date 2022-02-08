import math
import numpy as np
from tabulate import tabulate



print("---------------------------------------------------")
n=int(input("enter number of elements: "))

d=int(input("enter degree of distance: "))

def dist(a,b):
    return round(((math.fabs(a[0] - b[0])**d) + (math.fabs(a[1] - b[1])**d)) ** (1/d), 2)


X=[]
Y=[]
print("enter points space seperated: \nX Y")
for i in range(n):
    x,y = [float(j) for j in input().split(' ')]
    X.append(x)
    Y.append(y)


table =[]

def getMinIndex(table,n):
    Min=float('inf')
    k,l = 0,0
    for i in range(2,n+1):
        for j in range(1,i):
            if table[i][j] <= Min:
                Min = table[i][j]
                k=i
                l=j
    return k,l




for i in range(n+1):
    temp=[]
    for j in range(n+1):
        if i==0 and j==0:
            temp.append(" ")
            continue
        elif i==0:
            temp.append(f'P{j}')
            continue
        elif j==0:
            temp.append(f'P{i}')
            continue
        elif i==j:
            temp.append("0")
            continue
        else:
            temp.append(dist([X[i-1],Y[i-1]], [X[j-1],Y[j-1]]))
    table.append(temp)



print(tabulate(table, headers="firstrow"))
        
z = n

while(z!=2):
    new_table=[]
    k,l = getMinIndex(table,z)

    for i in range(z+1):
        temp=[]
        flag=True
        for j in range(z+1):
            if i==0 and j==0:
                temp.append(" ")
                continue
            elif (i==0 or j==0) and (j==l or i==l) and flag:
                temp.append(f'{table[0][l]},{table[0][k]}')
                flag=False
                continue
            elif (i==0 or j==0) and not (j==l or i==l):
                temp.append(table[i][j])
                continue
            elif i==j:
                temp.append("0")
                continue
            elif (i==l or i==k) and not (table[k][j] == "0" or table[l][j] == "0"):
                temp.append(min(table[k][j],table[l][j]))
            else:
                temp.append(table[i][j])
        new_table.append(temp)
    new_table.pop(k)
    for i in range(z):
        new_table[i].pop(k)
    
    table = new_table.copy()
    print_table=[]
    for i in range(z):
        temp=[]
        for j in range(z):
            if j>i and not (i==0 or j==0):
                temp.append("-")
            else:
                temp.append(new_table[i][j])
        print_table.append(temp)

    print(tabulate(print_table, headers="firstrow"))
    print("\n\n-----------------------------------------------------------------------------\n\n")
    z = z-1



# 0.4 0.53
# 0.22 0.38
# 0.35 0.32
# 0.26 0.19
# 0.08 0.41
# 0.45 0.30