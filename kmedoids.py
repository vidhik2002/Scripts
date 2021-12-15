import math
import matplotlib.pyplot as plt

from tabulate import tabulate


print("---------------------------------------------------")
n=int(input("enter number of elements: "))

k=int(input("enter value of k: "))
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

print("enter initial medoid points: \nX Y")
initial_medoids=[tuple([float(x) for x in input().split(' ')]) for _ in range(k)]
print(initial_medoids)

points = list(zip(X, Y)) 
print(points)

plt.scatter(X,Y,color='g')
plt.grid(True)
plt.show(block=False)

for i in initial_medoids:
    if i not in points:
        exit()



def get_table(medoids):
    table = dict()
    table['X'] = X
    table['Y'] = Y
    for i in range(k):
        temp=[]
        for j in points:
            temp.append(dist(j, medoids[i]))
        table[f'dist_cluster{i+1}']=temp

    table["cluster"]=[]
    table["cost"]=[]
    for i in range(n):
        Min = float('inf')
        cluster =0
        for j in range(k):
            if table[f'dist_cluster{j+1}'][i] < Min:
                Min=table[f'dist_cluster{j+1}'][i]
                cluster = j+1
        table["cluster"].append(cluster)
        table["cost"].append(table[f'dist_cluster{cluster}'][i])
        
    print(tabulate(table, headers='keys'))
    return table


table = get_table(initial_medoids)
cost = sum(table["cost"])
print("\n\n total cost: ", cost)

final_medoids = initial_medoids.copy()

while True:
    print("-------------------------------------------------------------------------------------")
    print("enter new medoids: ")
    medoids = [tuple([float(x) for x in input().split(' ')]) for _ in range(k)]
    table = get_table(medoids)
    new_cost = sum(table["cost"])
    print("cost: ",new_cost)
    print(f"cost for swapping = {new_cost} - {cost} = {new_cost - cost}")
    if new_cost < cost:
        print("medoids swapped:")
        cost = new_cost
        final_medoids = medoids.copy()
    else:
        print(f"undo swap\nmedoids remain {final_medoids}")
    
    if input("enter e to exit or press enter to continue: "):
        break

print(f"\n\nfinal cost: {cost}\nfinal medoids: {str(final_medoids).strip('[]')}")