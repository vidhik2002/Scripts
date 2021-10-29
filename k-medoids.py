import math
lst = [ ] 
lst2 = [ ]
n = int(input("Enter number of elements : ")) 
print("enter data points separated by space")
for i in range(0, n): 
    x, y = [float(x) for x in input().split()]  
    ele = [x,y]
    lst.append(ele) 
print(lst)

it = int(input("Enter number of iterations : ")) 

for i in range(it):
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
    for i in range(len(lst2)):
        if i < len(lst2)/2:
            lst3.append(lst2[i])
        else:
            lst4.append(lst2[i])
    

    c1 = [ ]
    c2 = [ ]
    cost = 0
    for i in range(len(lst3)):
        if(lst3[i]<lst4[i]):
            cost += int(lst3[i])
            c1.append(i+1)
        else:
            cost += int(lst4[i])
            c2.append(i+1)

    print("Cost: "+ str(cost))

    print("Cluster1: "+ str(c1))
    print("Cluster2:" + str(c2))