import math
import statistics
from statistics import mode

def find_dist(t1,t2):
    dist=len(t1)
    for a in range(len(t1)):
        if t1[a]==t2[a]:
            dist-=1
    return dist

def find_freq(lst, ele):
    cnt=0
    for i in lst:
        if i == ele:
            cnt+=1
    return cnt

points = [] 
n = int(input("Enter number of elements : ")) 
print("enter data points separated by space")
for i in range(0, n): 
    ele = tuple([x for x in input().split()])
    points.append(ele) 

# it = int(input("Enter number of iterations : ")) 
k = int(input("Enter no. of seed points: ")) 
modes_used=[[] for i in range(k)]
seed = []
print("enter seed points separated by space")
for i in range(0, k): 
    ele = tuple([x for x in input().split()])
    seed.append(ele)
    for j in range(len(ele)):
        modes_used[i].append([(ele[j])])
prevcluster=[]
ass_clust=[]
cnt=0
while(True):
    print('\n\niteration',cnt:=cnt+1, '\n')
    distances=[]
    clusters=[]
    for i in range(0,k):
        temp=[]
        for j in range(n):
            dist = find_dist(seed[i], points[j])
            temp.append(dist)
        clusters.append(temp)
    prevcluster=list(ass_clust)
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
    
    if prevcluster==ass_clust:
        break

    for j in range(k):
        new_seed=[]
        for x in range(len(points[0])):
            temp=[]
            for a in range(n):
                if(j+1==rows[a][-1]):
                    temp.append(rows[a][x])
            while(mode(temp) in modes_used[j][x]):
                temp2=list(temp)
                temp2.remove(mode(temp))
                flag=False
                for z in temp2:
                    if(find_freq(temp2, mode(temp2)) == find_freq(temp2,z) and mode(temp2)!=z):
                        flag=True
                if(flag or mode(temp)==mode(temp2)):
                    break
                temp.remove(mode(temp))
            new_seed.append(mode(temp))
            modes_used[j][x].append(mode(temp))
        seed[j]=tuple(new_seed)
    print("new seeds: ")
    for j in range(k):
        print(seed[j])

print('therefore clusters are same we end iterations')


"""
aa bb ab aa ab ab
ab bb ab aa ab bb
aa ab aa ab aa ab
bb aa bb ab aa bb
ab aa ab bb bb bb
aa ab bb aa ab bb
bb bb aa ab aa ab
ab ab aa ab bb ab

aa bb ab aa ab ab
ab aa ab bb bb bb

"""