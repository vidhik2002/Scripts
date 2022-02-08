m = 0
heads = {}
n = int(input("Number of rows: "))
for i in input("Enter table headings separated by space:\n").split(" "):
# for i in ["Days", "Season", "Fog", "Rain", "Class"]:
    heads.update({i: []})


table = []
for i in range(n):
    table.append(input(f"Enter table row {i}:\n").split(" "))


# pred = ["Weekday", "Winter", "High", "Heavy"]
pred = input("Enter your prediction tuple:\n").split(" ")

# table = [
# ["Weekday", "Spring", "None", "None", "OT"],
# ["Weekday", "Winter", "None", "Slight", "OT"],
# ["Weekday", "Winter", "None", "None", "OT"],
# ["Holiday", "Winter", "High", "Slight", "LT"],
# ["Saturday", "Summer", "Normal", "None", "OT"],
# ["Weekday", "Autumn", "Normal", "None", "VL"],
# ["Holiday", "Summer", "High", "Slight", "OT"],
# ["Sunday", "Summer", "Normal", "None", "OT"],
# ["Weekday", "Winter", "High", "Heavy", "VL"],
# ["Weekday", "Summer", "None", "Slight", "OT"],
# ["Saturday", "Spring", "High", "Heavy", "CA"],
# ["Weekday", "Summer", "High", "Slight", "OT"],
# ["Weekday", "Winter", "Normal", "None", "LT"],
# ["Weekday", "Summer", "High", "None", "OT"],
# ["Weekday", "Winter", "Normal", "Heavy", "VL"],
# ["Saturday", "Autumn", "High", "Slight", "OT"],
# ["Weekday", "Autumn", "None", "Heavy", "OT"],
# ["Holiday", "Spring", "Normal", "Slight", "OT"],
# ["Weekday", "Spring", "Normal", "None", "OT"],
# ["Weekday", "Spring", "Normal", "Heavy", "OT"],
# ]

# Get all unique values in each column
for i in range(len(heads)):
    L = set([a[i] for a in table])
    if i != len(heads) - 1:
        m += len(L)
    heads[list(heads.keys())[i]] = list(L)

#setup
cols = heads[list(heads.keys())[-1]]
Final = [["" for _ in range(2 + len(heads[list(heads.keys())[-1]]))] for _2 in range(m + 2)]
Final[0][1] = "Attrs"
Final[-1][1] = "Prior"
for i in range(len(heads[list(heads.keys())[-1]])):
    Final[0][2+i] = heads[list(heads.keys())[-1]][i]

for i in range(2, len(Final[0])):
    val = [a[-1] for a in table].count(Final[0][i]) / n
    Final[-1][i] = float(f"{val:.2f}")


index = 0
for i in range(len(heads.keys()) - 1):                      # Categories
    for j in range(len( heads[list(heads.keys())[i]] )):    # SUbcategories
        mcat = list(heads.keys())[i]
        scat = heads[list(heads.keys())[i]][j]
        L = [mcat, scat]
        for k in range(2, len(Final[0])):
            colhead = Final[0][k]
            temp = [a[i] for a in table if a[-1] == colhead]
            colhcount = [a[-1] for a in table].count(colhead)
            scount = temp.count(scat)
            val = scount / colhcount
            L.append(float(f"{val:.2f}"))
        index += 1
        Final[index] = L

print("In this database, there are four attributes:")
print("\tA = " + " ".join(list(heads.keys())[:-1]))
print(f"With {n} tuples\n")

print("The categories of classes are:")
print("\tC = " + " ".join(heads[list(heads.keys())[-1]]))
print()


print("-----\t"*len(Final[0]))
print("\t".join(
    str(x)[:5] if len(str(x)) > 5 else str(x) for x in Final[0]
    ))
print("-----\t"*len(Final[0]))
for i in Final[1:]:
    print("\t".join(
        str(x)[:5] if len(str(x)) > 5 else str(x) for x in i
        ))
print("-----\t"*len(Final[0]))

print()
ix = 0
for i in cols:
    print(f"Pnb({i}) = P({i}) * " + " * ".join(f"P({x}|{i})" for x in pred) + " :")
    ans = Final[-1][ix+2]

    print(f"         = ", end = "")
    print(ans, end = "")
    
    for j in pred:
        index = [f[1] for f in Final].index(j)
        print(" *", Final[index][ix+2], end = "")
        ans *= Final[index][ix+2]
    print(" =", f"{ans:.4f}")
    print()
    ix += 1

"""
Heads:
Days Season Fog Rain Class

Weekday Spring None None OT
Weekday Winter None Slight OT
Weekday Winter None None OT
Holiday Winter High Slight LT
Saturday Summer Normal None OT
Weekday Autumn Normal None VL
Holiday Summer High Slight OT
Sunday Summer Normal None OT
Weekday Winter High Heavy VL
Weekday Summer None Slight OT
Saturday Spring High Heavy CA
Weekday Summer High Slight OT
Weekday Winter Normal None LT
Weekday Summer High None OT
Weekday Winter Normal Heavy VL
Saturday Autumn High Slight OT
Weekday Autumn None Heavy OT
Holiday Spring Normal Slight OT
Weekday Spring Normal None OT
Weekday Spring Normal Heavy OT
"""
"""
["Days", "Season", "Fog", "Rain", "Class"]

[
["Weekday", "Spring", "None", "None", "OT"],
["Weekday", "Winter", "None", "Slight", "OT"],
["Weekday", "Winter", "None", "None", "OT"],
["Holiday", "Winter", "High", "Slight", "LT"],
["Saturday", "Summer", "Normal", "None", "OT"],
["Weekday", "Autumn", "Normal", "None", "VL"],
["Holiday", "Summer", "High", "Slight", "OT"],
["Sunday", "Summer", "Normal", "None", "OT"],
["Weekday", "Winter", "High", "Heavy", "VL"],
["Weekday", "Summer", "None", "Slight", "OT"],
["Saturday", "Spring", "High", "Heavy", "CA"],
["Weekday", "Summer", "High", "Slight", "OT"],
["Weekday", "Winter", "Normal", "None", "LT"],
["Weekday", "Summer", "High", "None", "OT"],
["Weekday", "Winter", "Normal", "Heavy", "VL"],
["Saturday", "Autumn", "High", "Slight", "OT"],
["Weekday", "Autumn", "None", "Heavy", "OT"],
["Holiday", "Spring", "Normal", "Slight", "OT"],
["Weekday", "Spring", "Normal", "None", "OT"],
["Weekday", "Spring", "Normal", "Heavy", "OT"],
]
"""