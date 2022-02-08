import math, random

Data = []
# Heads = input("Enter headings space sep:\n").split()
# n = int(input("Enter number of rows"))
Heads = ["x1", "x2", "x3", "Y"]
n = 6
Data = [
    ["t", "t", "f", "t"],
    ["t", "t", "f", "f"],
    ["t", "f", "f", "t"],
    ["t", "t", "t", "f"],
    ["f", "t", "f", "f"],
    ["t", "f", "f", "t"],
]

# for i in range(n):
#     Data.append(input(f"Row {i} space sep(t or f):"))

for i in range(len(Data)):
    Data[i].append(1/n)

def pdata(h, data, n):
    print("|-------"*len(h) + "|")
    print("|" + "\t|".join([i[:7] if len(i) > 7 else i for i in h]) + "\t|")
    print("|-------"*len(h) + "|")
    for i in range(n):
        print("|" + "\t|".join([str(x) for x in data[i]]))
    print("|-------"*len(h) + "|")
    print("\n")


def gini(h, data, n, attex = "n"):
    pdata(h, data, n)
    mingin = 1
    minatt = ""
    for i in range(len(h) - 1):
        print(f"=== gini index for {h[i]}:")
        tcount = [a[i] for a in data].count("t")
        fcount = n - tcount
        print(f"Total True : {tcount}")
        print(f"Total False: {fcount}\n")
        ttc = [a[len(h) - 1] for a in data if a[i] == "t"].count("t")
        tfc = [a[len(h) - 1] for a in data if a[i] == "t"].count("f")
        ftc = [a[len(h) - 1] for a in data if a[i] == "f"].count("t")
        ffc = [a[len(h) - 1] for a in data if a[i] == "f"].count("f")
        print(f"True({h[i]}) | True  : {ttc}")
        print(f"True({h[i]}) | False : {tfc}")
        if ttc*tfc == 0:
            gt = 0
        else:
            gt = 1 - ((ttc/tcount)**2 + (tfc/tcount)**2)
        print(f"Gini true: 1 - (({ttc}/{tcount})^2 + ({tfc}/{tcount})^2) = {gt}\n")
        print(f"False({h[i]}) | True : {ftc}")
        print(f"False({h[i]}) | False: {ffc}")
        if ftc*ffc == 0:
            gf = 0
        else:
            gf = 1 - ((ftc/fcount)**2 + (ffc/fcount)**2)
        print(f"Gini true: 1 - (({ftc}/{fcount})^2 + ({ffc}/{fcount})^2) = {gf}\n")
        gin = (tcount/n)*gt + (fcount/n)*gf
        print(f"Gini index = ({tcount}/{n})*({gt}) + ({fcount}/{n})*({gf}) = {gin}")
        if gin < mingin:
            mingin = gin
            minatt = i
    if attex != "n":
        minatt = attex
    print(f"----Minimum gini index = {mingin} | Attribute = {h[minatt]}\n")
    ttc = [a[len(h) - 1] for a in data if a[minatt] == "t"].count("t")
    tfc = [a[len(h) - 1] for a in data if a[minatt] == "t"].count("f")
    ftc = [a[len(h) - 1] for a in data if a[minatt] == "f"].count("t")
    ffc = [a[len(h) - 1] for a in data if a[minatt] == "f"].count("f")
    if (ttc < tfc) or (ffc < ftc):
        comb = "tf"
        errors = ffc + ttc
    else:
        comb = "tt"
        errors = tfc + ftc
    
    if errors == 0:
        say = 1
    else:
        say = 0.5*math.log10((1 - (errors/n))/ (errors/n))
    print(f"Say = 0.5*log10((1 - ({errors}/{n})) / ({errors}/{n}))")
    print("Amount of say = ", say)
    print(comb)
    for i in range(n):
        if comb == "tt":
            if (data[i][minatt] == "t" and data[i][len(h) - 1] == "t") or (data[i][minatt] == "f" and data[i][len(h) - 1] == "f"):
                data[i][-1] *= math.e**(-say)
            else:
                data[i][-1] *= math.e**(say)
        else:
            if (data[i][minatt] == "t" and data[i][len(h) - 1] == "f") or (data[i][minatt] == "f" and data[i][len(h) - 1] == "t"):
                data[i][-1] *= math.e**(-say)
            else:
                data[i][-1] *= math.e**(say)
    print("Recalculate weights: ")
    pdata(h, data, n)
    print("Normalizing weights: ")
    samsum = sum([i[-1] for i in data])
    for i in range(n):
        data[i][-1] /= samsum
    pdata(h, data, n)
    
    d2 = []

    for i in range(n):
        print("=====")
        ch = random.random()
        print(ch)
        c = 0
        for j in data:
            c += 1
            ch = ch - j[-1]
            if ch < 0:
                d2.append(j[:-1] + [1/n,])
                break

    return d2

while True:
    Data = gini(Heads, Data, n)
    cont = input("Do you want to do another cycle?(y/n)\n")
    if cont != "y":
        break

# Data = gini(Heads, Data, n, 0)
# Data = gini(Heads, Data, n, 1)
# Data = gini(Heads, Data, n, 2)