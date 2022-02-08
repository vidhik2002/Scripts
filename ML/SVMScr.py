import math
import matplotlib.pyplot as plt

lst1 = [ ]
lst2 = [ ]
lst3 = [ ]

positive_x = []
positive_y = []
negative_x = []
negative_y = []
consts = []

np = int(input("Enter number of positive elements: ")) 
print("Enter positive data points separated by space")
for i in range(0, np): 
    x, y = [float(x) for x in input().split()]  
    ele = [x,y]
    lst1.append(ele) 
    positive_x.append(x)
    positive_y.append(y)
print(f"+ve data points: {lst1}")

nn = int(input("Enter number of negative elements: ")) 
print("Enter negative data points separated by space")
for i in range(0, nn): 
    x, y = [float(x) for x in input().split()]  
    ele = [x,y]
    lst2.append(ele)
    negative_x.append(x)
    negative_y.append(y)
print(f"-ve data points: {lst2}")

plt.scatter(positive_x,positive_y,color='g')
plt.scatter(negative_x,negative_y,color='r')
plt.grid(True)
plt.show(block=False)

sv = int(input("Enter number of support elements: ")) 
print("Enter support data points separated by space")
for i in range(0, sv): 
    x, y = [float(x) for x in input().split()]  
    ele = [x,y]
    lst3.append(ele) 
print(lst3)


au = float(input("Enter number to be augmented to support elements: ")) 
for i in range(0, sv): 
    lst3[i].append(au)
print(f"{lst3}\n")

for i in lst3:
    for j in lst3:
        temp = 0
        for k in range(0,len(lst3[0])):
            temp += i[k]*j[k]
        print(temp, end=" ")
    if(i[0:-1] in lst1):
        print(" = 1")
    else:
        print(" = -1")

print("Enter constants line by line:")
for i in range(0, len(lst3)): 
    c = float(input())
    consts.append(c) 
print(f"Entered Constants: {consts}")

interim = [0 for i in range(len(lst3))]
for i in range(0, len(lst3)):
    interim[i] = [consts[i]*x for x in lst3[i]]

print(interim)

final = []
for j in range(0,len(interim[0])):
    temp = 0
    for i in interim:
        temp += i[j]
    final.append(temp)
    
print(f"Answer: {final}")