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
    mediods = []
    k = int(input("Enter no. of seed points: ")) 
    print("enter seed points separated by space")
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
    if d == "e":
        for i in range(0,k):
            print("cluster ", i+1)
            for j in range(n):
                print(round(math.sqrt(math.pow(abs(mediods[i][0] - lst[j][0]),2) + math.pow(abs(mediods[i][1] - lst[j][1]),2)), 2))

