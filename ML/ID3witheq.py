import math as m
from tabulate import tabulate
import numpy as np


# n = int(input("Enter number of examples: "))

# table = []
# print("Enter the attr names:")
# attrs = list(input().split())

# for i in range(1+len(attrs)):
#     attribute_data = (input(f'Enter column {i+1}: (space seperated) ')).split(" ")
#     table.append(attribute_data)
# table.append((input(f'Enter Class/Label: (space seperated y/n) ')).split(" "))
table = [['D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'D10', 'D11', 'D12', 'D13', 'D14'], ['Sunny', 'Sunny', 'Overcast', 'Rain', 'Rain', 'Rain', 'Overcast', 'Sunny', 'Sunny', 'Rain', 'Sunny', 'Overcast', 'Overcast', 'Rain'], ['Hot', 'Hot', 'Hot', 'Mild', 'Cool', 'Cool', 'Cool', 'Mild', 'Cool', 'Mild', 'Mild', 'Mild', 'Hot', 'Mild'], ['High', 'High', 'High', 'High', 'nrmal', 'nrmal', 'nrmal', 'High', 'nrmal', 'nrmal', 'nrmal', 'High', 'nrmal', 'High'], ['Weak', 'Strong', 'Weak', 'Weak', 'Weak', 'Strong', 'Strong', 'Weak', 'Weak', 'Weak', 'Strong', 'Strong', 'Weak', 'Strong'], ['n', 'n', 'y', 'y', 'y', 'n', 'y', 'n', 'y', 'y', 'y', 'y', 'y', 'n']]
attrs = ["out", "temp", "humid", "wind"]
n = 14


def SolveID3(table, attrs, n):
    tabs = tabulate(np.transpose(table), ["index"] + attrs + ["label"])
    print(tabs)

    E_full = calc_E(table[-1])
    if E_full==0:
        print("Found final decision")
        print("--------------------------------------")
        return
    print(f"Entropy Overall: {E_full:.3f}\n\n")
    gains = []

    for attr,col in zip(attrs, table[1:-1]):
        print(f"Attribute: {attr} -->")
        checklist = list(zip(col, table[-1]))
        subattrs = list(set(col))
        attrEs = []
        for x in subattrs:
            E_subat = calc_E([i[1] for i in checklist if i[0]==x])
            print(f"{x}: {E_subat:.3f}")
            attrEs.append([E_subat, len([i[1] for i in checklist if i[0]==x])])
        tamasha = '-'.join([ str(round(i[0], 3)) + "*(" + str(i[1]) + "/" + str(n) + ")" for i in attrEs ])
        print(f"\n---\nGain formula:\n{E_full:.3f} - {tamasha}")
        print(f"Gain for attribute {attr} = {E_full - sum(i[0]*i[1]/n for i in attrEs):.4f}\n---")
        gains.append([attr, E_full - sum(i[0]*i[1]/n for i in attrEs)])
        print()
    parting_attr = sorted(gains, key = lambda x: x[1])[-1]
    print(f"Dividing Attribute is '{parting_attr[0]}' with gain {parting_attr[1]:.3f}")
    print("----o----o----o----o----o----o----o----o----o----o----o----\n\n")

    subatrs = list(set(table[attrs.index(parting_attr[0]) + 1]))
    for atr in subatrs:    
        newtable = []
        for i in table[:attrs.index(parting_attr[0]) + 1] + table[attrs.index(parting_attr[0]) + 2:]:
            temp = []
            for j in range(n):
                if table[attrs.index(parting_attr[0]) + 1][j] == atr:
                    temp.append(i[j])
            newtable.append(temp)
        SolveID3(newtable, [a for a in attrs if a != parting_attr[0]], len(newtable[0]))
        


def calc_E(list):
    pos = list.count("y")
    neg = list.count("n")
    tot = pos + neg
    print(f"\nCalculate E for list {' '.join(list)}:")
    print(f"-({pos}/{tot})log2({pos}/{tot}) - ({neg}/{tot})log2({neg}/{tot})")
    if (pos*neg==0):
        return 0
    return -(pos/tot)*m.log2(pos/tot) - (neg/tot)*m.log2(neg/tot)

SolveID3(table, attrs, n)
