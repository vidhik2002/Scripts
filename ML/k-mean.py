import math

n = int(input("Enter number of rows: "))
k = int(input("Enter k: "))

points = []
for i in range(n):
    points.append(list(map(float, input("Enter point space separated:\n").split())))
# points = [
#     [2.0, 10.0],
#     [2.0, 5.0],
#     [8.0, 4.0],
#     [5.0, 8.0],
#     [7.0, 5.0],
#     [6.0, 4.0],
#     [1.0, 2.0],
#     [4.0, 9.0]
#     ]

# mean = [[2.0, 10.0], [5.0, 8.0], [1.0, 2.0]]
mean = []
for i in range(k):
    mean.append(list(map(float, input("Enter means space separated:\n").split())))

d = int(input("Power of distance: "))

def dist(a, b):
    return round(((math.fabs(a[0] - b[0])**d) + (math.fabs(a[1] - b[1])**d)) ** (1/d), 2)

def printtable():
    clusters = [[] for _ in range(k)]
    print(f"""For means {' '.join(f"{i}" for i in mean)}""")
    print()
    print("Points\t\t" + "cluster\t"*k)
    for i in range(len(points)):
        print(points[i], end = "\t")
        cv, cl = 999, 0
        for j in range(k):
            dis = dist(points[i], mean[j])
            if dis < cv:
                cv, cl = dis, j
            print(dis, end = "\t")
        clusters[cl].append(i)
        print(cl, end = "\t")
        print()
    
    print("\nClusters:")
    sv = -1
    for i in clusters:
        print(f"Cluster[{(sv := sv + 1)}] => " + ", ".join(f"({j})" + str(points[j]) for j in i))
    return clusters

def computeMean(cdata):
    mean = []
    for i in cdata:
        x1, y1 = 0, 0
        for j in i:
            x1 += points[j][0]
            y1 += points[j][1]
        mean.append([round(x1/len(i), 2), round(y1/len(i), 2)])
    print(f"""\nNew means {' '.join(f"{i}" for i in mean)}""")
    return mean

cprev, ccur = [], printtable()
while cprev != ccur:
    mean = computeMean(ccur)
    cprev = ccur
    ccur = printtable()
else:
    print("We have obtained final clusters")