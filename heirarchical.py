import math
lst = [ ] 
lst2 = [ ]
n = int(input("Enter number of elements : ")) 
print("enter data points separated by space")
for i in range(0, n): 
    x, y = [float(x) for x in input().split()]  
    ele = [x,y]
    lst.append(ele) 


for i in range(len(lst)):
    for j in range(len(lst)):
        print("distance of {} and {} = {}".format(i, j, round(math.sqrt(math.pow(abs(lst[i][0] - lst[j][0]),2) + math.pow(abs(lst[i][1] - lst[j][1]),2)), 2)))
    print("\n")