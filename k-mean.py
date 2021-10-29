import math
lst = [ ] 
# n = int(input("Enter number of elements : ")) 
# print("enter data points separated by space")
# for i in range(0, n): 
#     x, y = [float(x) for x in input().split()]  
#     ele = [x,y]
#     lst.append(ele) 
# print(lst)
lst2 =[ ]

it = int(input("Enter number of iterations : ")) 

# seed = []
# k = int(input("Enter no. of seed points: ")) 
# print("enter seed points separated by space")
# for i in range(0, k): 
#     a, b = [float(a) for a in input().split()]  
#     ele = [a,b]
#     seed.append(ele) 
# print(seed)
lst = [[2.0, 4.0], [2.0, 6.0], [5.0, 6.0], [4.0, 7.0], [8.0, 3.0], [6.0, 6.0], [5.0, 2.0], [5.0, 7.0], [6.0, 3.0], [4.0, 4.0]]
seed = [[1.0, 5.0], [4.0, 1.0], [8.0, 4.0]]
n = 10
k = 3

for i in range(it):
    lst2 = []
    d = input("Enter type of distance e/m: ")

    if d == "m":
        for i in range(0,k):
            #Manhattan Distance 
            print("cluster ", i+1)
            for j in range(n):
                print(abs(seed[i][0] - lst[j][0])+abs(seed[i][1] - lst[j][1]))
                lst2.append(abs(seed[i][0] - lst[j][0])+abs(seed[i][1] - lst[j][1]))
            
    if d == "e":
        for i in range(0,k):
            print("cluster ", i+1)
            for j in range(n):
                print(round(math.sqrt(math.pow(abs(seed[i][0] - lst[j][0]),2) + math.pow(abs(seed[i][1] - lst[j][1]),2)), 2))
                lst2.append(round(math.sqrt(math.pow(abs(seed[i][0] - lst[j][0]),2) + math.pow(abs(seed[i][1] - lst[j][1]),2)), 2))

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
    cost = 0.0
    for i in range(len(lst5)):
        minimum.append(min(lst5[i]))
        ind.append(int(lst5[i].index(min(lst5[i])))+1)
    print("list of points",lst)
    print("seed",seed)
    print("minimum distances",minimum)
    print("cluster number they belong to",ind)
    
    seed = [] 
    centroid = [ ]
    sumx = 0.0
    sumy = 0.0
    for i in range(1,k+1):
        for j in range(len(ind)):
            if ind[j] == i :
                centroid.append(lst[j])
        print(centroid)
        for l in range(len(centroid)):
            sumx += int(centroid[l][0])
            sumy += int(centroid[l][1])
        
        sumx=sumx/len(centroid)
        sumy=sumy/len(centroid)
        seed.append([sumx,sumy])
        sumx = 0.0
        sumy = 0.0
        centroid = []   
    print(seed)