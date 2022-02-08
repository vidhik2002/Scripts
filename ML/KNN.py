import math

rows = int(input('enter the no. of rows: '))
choice = int(input('enter distance method euclidian [1] manhattan [2]: '))

titles = [x for x in input('enter titles seperated by "," : ').replace(", ", ",").split(sep=",")]
print(titles)
cols = len(titles)

values=[]

for i in range(rows):
    values.append([x for x in input(f'enter values for row {i+1} seperated by ",": ').replace(", ", ",").split(sep=",")])

predict = tuple([x for x in input(f'enter values for prediction seperated by ",": ').replace(", ", ",").split(sep=",")])

def dist(choice, p1, p2):
    if choice == 1:
        return (math.sqrt(sum(tuple(map(lambda i, j: (float(i) - float(j))**2, p1, p2)))))
    else:
        return (sum(tuple(map(lambda i, j: abs(float(i) - float(j)), p1, p2))))

distances=dict()
for i in range(rows):
    d = dist(choice, predict, tuple(values[i][:-1]))
    distances[i]=d

sort_dist = dict(sorted(distances.items(), key=lambda item: item[1]))
sort_rows = list(sort_dist.keys())

titles.append("dist")
titles.append("rank")

for i in titles:
    print(i, end="\t")
print()
for i in range(rows):
    # print(values[i], distances[i], (sort_rows.index(i)+1), sep = "\t")
    values[i].append(round(distances[i], 3))
    values[i].append(sort_rows.index(i)+1)
    for j in values[i]:
        print(j, end="\t")
    print()
