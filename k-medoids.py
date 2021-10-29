import math
lst = [ ] 
n = int(input("Enter number of elements : ")) 
print("enter data points separated by space")
for i in range(0, n): 
    x, y = [float(x) for x in input().split()]  
    ele = [x,y]
    lst.append(ele) 
print(lst)

it = int(input("Enter number of iterations : ")) 

for i in range(it):
    lst2=[]
    mediods = []
    k = int(input("Enter k: ")) 
    print("enter mediod points separated by space")
    for i in range(0, k): 
        a, b = [float(a) for a in input().split()]  
        ele = [a,b]
        mediods.append(ele) 
    print(mediods)

    d = input("Enter type of distance e/m: ")


    if d == "m":
        for i in range(0,k):
            #Manhattan Distance 
            print("cluster ", i+1)
            for j in range(n):
                print(abs(mediods[i][0] - lst[j][0])+abs(mediods[i][1] - lst[j][1]))
                lst2.append(abs(mediods[i][0] - lst[j][0])+abs(mediods[i][1] - lst[j][1]))
    if d == "e":
            for i in range(0,k):
                print("cluster ", i+1)
                for j in range(n):
                    print(round(math.sqrt(math.pow(abs(mediods[i][0] - lst[j][0]),2) + math.pow(abs(mediods[i][1] - lst[j][1]),2)), 2))
                    lst2.append(round(math.sqrt(math.pow(abs(mediods[i][0] - lst[j][0]),2) + math.pow(abs(mediods[i][1] - lst[j][1]),2)), 2))

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
    print("minimum distances",minimum)
    print("cluster number they belong to",ind)
    for i in range(len(minimum)):
        cost += minimum[i]
    print("cost",cost)
