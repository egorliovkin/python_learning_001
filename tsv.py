d = {}
for x in range(1,12):
    d[x] = []
with open("/home/egorliovkin/Downloads/dataset_3380_5.txt") as tsv:
    for line in tsv.read().strip().split('\n'):
        class_n, fio, higth = line.split('\t')
        d[int(class_n)] += [int(higth)]
for k in d.keys():
    x = sum(d[k])
    y = len(d[k])
    if y == 0:
        print(f"{k} -")
    else:
        print(f"{k} {x/y}")