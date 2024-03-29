import math
import statistics
from statistics import mode

def find_dist(t1,t2):
    dist=len(t1)
    for a in range(len(t1)):
        if t1[a]==t2[a]:
            dist-=1
    return dist



points = [] 
n = int(input("Enter number of elements : ")) 
print("enter data points separated by space")
for i in range(0, n): 
    ele = tuple([x for x in input().split()])
    points.append(ele) 

it = int(input("Enter number of iterations : ")) 
k = int(input("Enter no. of seed points: ")) 
seed = []
print("enter seed points separated by space")
for i in range(0, k): 
    ele = tuple([x for x in input().split()])
    seed.append(ele) 

for i in range(it):
    distances=[]
    clusters=[]
    for i in range(0,k):
        temp=[]
        for j in range(n):
            dist = find_dist(seed[i], points[j])
            temp.append(dist)
        clusters.append(temp)
    
    ass_clust = []
    for j in range(n):
        temp_tup = tuple([x[j] for x in clusters])
        distances.append(temp_tup)
        ass_clust.append(temp_tup.index(min(temp_tup)))

    for j in range(len(points[0]) + k +1):
        if j<len(points[0]):
            print('{:<10}'.format("point"+str(j+1)), end="")
        elif j<(len(points[0]) + k):
            print("{:<10}".format("d to C"+str(j-len(points[0])+1)), end="")
        else:
            print("{:<10}".format("cluster assign"), end="")
    print()
    rows=[]
    for j in range(n):
        row = []
        for p in points[j]:
            row.append(p)
        for a in range(k):
            row.append(distances[j][a])
        row.append(ass_clust[j]+1)

        for r in row:
            print("{:<10}".format(r), end="")
        print()
        rows.append(row)
    for j in range(k):
        new_seed=[]
        for x in range(len(points[0])):
            temp=[]
            for a in range(n):
                if(j+1==rows[a][-1]):
                    temp.append(rows[a][x])
            new_seed.append(mode(temp))
        seed[j]=tuple(new_seed)
    print("new seeds: ")
    for j in range(k):
        print(seed[j])
