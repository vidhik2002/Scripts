import math as m
import numpy as np


table = []
choice = int(input("Do you want to run on built in input(1) as per given in the question or give your own input(2). Enter 1 or 2:"))
if choice == 1:
    n = 14

    #Table headers
    heads = [
        "Outlook",
        "Temp",
        "Humidity",
        "Wind"
    ]
    # Each row in the table represents one column in the 
    table = [
        ['D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'D10', 'D11', 'D12', 'D13', 'D14'], 
        ['Sunny', 'Sunny', 'Overcast', 'Rain', 'Rain', 'Rain', 'Overcast', 'Sunny', 'Sunny', 'Rain', 'Sunny', 'Overcast', 'Overcast', 'Rain'], 
        ['Hot', 'Hot', 'Hot', 'Mild', 'Cool', 'Cool', 'Cool', 'Mild', 'Cool', 'Mild', 'Mild', 'Mild', 'Hot', 'Mild'], 
        ['High', 'High', 'High', 'High', 'Normal', 'Normal', 'Normal', 'High', 'Normal', 'Normal', 'Normal', 'High', 'Normal', 'High'], 
        ['Weak', 'Strong', 'Weak', 'Weak', 'Weak', 'Strong', 'Strong', 'Weak', 'Weak', 'Weak', 'Strong', 'Strong', 'Weak', 'Strong'], 
        ['n', 'n', 'y', 'y', 'y', 'n', 'y', 'n', 'y', 'y', 'y', 'y', 'y', 'n']
    ]
elif choice == 2:
    n = int(input("Enter number of rows: "))
    heads = input("Enter space separated column headers except index column and final label column: ").split(" ")
    print(f"Now enter {len(heads) + 2} columns. FIrst column is index and last is the label")
    for i in range(len(heads) + 2):
        table.append(input(f"Enter space separated column number {i}:\n").split(" "))


treefinal = {}

def SolveID3(table, attrs, n, level = 0, root = "top node"):
    E_full = calc_E(table[-1])
    print(f"=------------=\tFor current rows at level {level}: Child of {root}")
    print(f"=------------=\t{' '.join(table[0])}")
    print(f"=------------=\tEntropy Overall: {E_full:.3f}\n")
    if E_full==0:
        print("Hence this is a leaf node")
        print("===================================================================\n\n")
        return
    gains = []

    for attr,col in zip(attrs, table[1:-1]):
        print(f"For attribute {attr}:")
        checklist = list(zip(col, table[-1]))
        subattrs = list(set(col))
        attrEs = []
        for x in subattrs:
            E_subat = calc_E([i[1] for i in checklist if i[0]==x])
            print(f"{x}: {E_subat:.3f}")
            attrEs.append([E_subat, len([i[1] for i in checklist if i[0]==x])])
        print(f"Gain for attribute {attr} = {E_full - sum(i[0]*i[1]/n for i in attrEs):.4f}\n")
        gains.append([attr, E_full - sum(i[0]*i[1]/n for i in attrEs)])
        print()
    parting_attr = sorted(gains, key = lambda x: x[1])[-1]
    print(f"Dividing Attribute is '{parting_attr[0]}' with gain {parting_attr[1]:.3f}")
    print("===================================================================\n\n")

    subatrs = list(set(table[attrs.index(parting_attr[0]) + 1]))
    for atr in subatrs:    
        newtable = []
        for i in table[:attrs.index(parting_attr[0]) + 1] + table[attrs.index(parting_attr[0]) + 2:]:
            temp = []
            for j in range(n):
                if table[attrs.index(parting_attr[0]) + 1][j] == atr:
                    temp.append(i[j])
            newtable.append(temp)
        SolveID3(newtable, [a for a in attrs if a != parting_attr[0]], len(newtable[0]), level + 1, root = parting_attr[0] + f"({atr})")
        


def calc_E(list):
    pos = list.count("y")
    neg = list.count("n")
    tot = pos + neg
    if (pos*neg==0):
        return 0
    return -(pos/tot)*m.log2(pos/tot) - (neg/tot)*m.log2(neg/tot)

SolveID3(table, heads, n)