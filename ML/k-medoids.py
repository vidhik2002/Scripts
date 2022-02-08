import math
import matplotlib.pyplot as plt

from tabulate import tabulate

def dist(choice, p1, p2):
    if choice == 1:
        return (math.sqrt(sum(tuple(map(lambda i, j: (float(i) - float(j))**2, p1, p2)))))
    else:
        return (sum(tuple(map(lambda i, j: abs(float(i) - float(j)), p1, p2))))

lst = [ ] 
n = int(input("Enter number of elements : ")) 
print("enter data points separated by space")
for i in range(0, n): 
    ele = tuple([float(x) for x in input().split()]) 
    lst.append(ele) 

plt.scatter([a[0] for a in lst],[a[1] for a in lst],color='g')
plt.grid(True)
plt.show(block=False)


# it = int(input("Enter number of iterations : ")) 

k = int(input("Enter k: ")) 
prevcluster=[]
medoids=[]
index=0
index2=1
cost = float('inf')
print("enter mediod points separated by space")
for i in range(0, k): 
    ele = tuple([float(a) for a in input().split()]) 
    medoids.append(ele)

d = input("Enter type of distance e/m: ")

while(True):

    print("\n\nmedoids: {}\n".format(medoids))
    # print("used medoids: {}".format(used_meds))
    lst2=[]
    
    # print("enter mediod points separated by space")
    # for i in range(0, k): 
    #     a, b = [float(a) for a in input().split()]  
    #     ele = [a,b]
    #     medoids.append(ele) 
    # print(medoids)

    dists=[[] for i in range(n)]

    if d == "m":
        for i in range(0,k):
            #Manhattan Distance 
            # print("cluster", i+1, "distance")
            for j in range(n):
                # print(dist(2, lst[j], medoids[i]), end=" ")
                lst2.append(dist(2, lst[j], medoids[i]))
                dists[j].append(dist(2, lst[j], medoids[i]))
            # print()
    if d == "e":
            for i in range(0,k):
                # print("cluster", i+1, "distance")
                # for j in range(n):
                    # print(dist(1, lst[j], medoids[i]), end=" ")
                lst2.append(dist(1, lst[j], medoids[i]))
            # print()
    lst3 = [ ]
    lst4 = [ ]

    result = [lst2[i:i + n] for i in range(0, len(lst2), n)]
    lst5 = []
    for i in range(len(result[0])):
        for j in range(len(result)):
            lst4.append(result[j][i])
        lst5.append(lst4)
        lst4 = []
    
    minimum = []
    ind = []
    tempcost=0.0
    for i in range(len(lst5)):
        minimum.append(min(lst5[i]))
        ind.append(int(lst5[i].index(min(lst5[i])))+1)
    table=[]
    row=[]
    row.append("point")
    for j in range(len(dists[i])):
        row.append("d from C{}".format(j+1))
    row.append("min cost")
    row.append("clusters assigned")
    table.append(row)

    for i in range(n):
        row=[]
        row.append(lst[i])
        for j in dists[i]:
            row.append(j)
        row.append(minimum[i])
        row.append(ind[i])
        table.append(row)
    print(tabulate(table, headers="firstrow", tablefmt="github"))
    # print("minimum distances:",minimum)
    # print("cluster number they belong to",ind)
    for i in range(len(minimum)):
        tempcost += minimum[i]
    print("\ncost",tempcost)
    cost = min(cost, tempcost)
    ele = lst[index]
    flag=False
    while(ele in medoids):
        index+=1
        if index==len(lst):
            flag=True
            break
        ele = lst[index]
    if flag:
        if index2==k:
            break
        else:
            index2+=1
            index=0
    medoids[-index2]=ele

print("\n\nminimum cost: {}".format(cost))

"""
2 6
3 4
3 8
4 7
6 2
6 4
7 3
7 4
8 5
7 6
"""