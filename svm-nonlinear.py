import math
lst1 = [ ] 
lst2 = [ ]
lst3 = [ ]

np = int(input("Enter number of positive elements : ")) 
print("enter positive data points separated by space")
for i in range(0, np): 
    x, y = [float(x) for x in input().split()] 
    if round(math.sqrt(math.pow(x,2) + math.pow(y, 2))) > 2 :
        a = 4-y + abs(x-y)
        b = 4-x + abs(x-y)
        ele = [a,b]
    else:
        ele = [x,y]
    lst1.append(ele) 
print(lst1)

nn = int(input("Enter number of negative elements : ")) 
print("enter negative data points separated by space")
for i in range(0, nn): 
    x, y = [float(x) for x in input().split()]  
    if round(math.sqrt(math.pow(x,2) + math.pow(y, 2))) > 2 :
        a = 4-y + abs(x-y)
        b = 4-x + abs(x-y)
        ele = [a,b]
    else:
        ele = [x,y]
    lst2.append(ele) 
print(lst2)

sv = int(input("Enter number of support elements : ")) 
print("enter support data points separated by space")
for i in range(0, sv): 
    x, y = [float(x) for x in input().split()]  
    ele = [x,y]
    lst3.append(ele) 
print(lst3)


au = float(input("Enter number to be augmented to support elements : ")) 
for i in range(0, sv): 
    lst3[i].append(au)
print(lst3)

lst4 = [ ]
for i in range(sv):
    for j in range(sv):
        lst4.append(float(lst3[i][0]*lst3[j][0]+lst3[i][1]*lst3[j][1]+lst3[i][2]*lst3[j][2]))
print(lst4)