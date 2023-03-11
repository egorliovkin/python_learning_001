xss = []
with open("/home/egorlevkin/Downloads/dataset_3363_4.txt") as inf:
    xss = [(x[0],[int(x[1]),int(x[2]),int(x[3])]) for x in [x.split(';') for x in inf.read().strip().split()]]
xs = [sum(x[1])/3 for x in xss]
dc = {'v1': 0, 'v2': 0, 'v3': 0,'n1': 0, 'n2': 0, 'n3': 0}
for x in xss:
    name = x[0]
    value_list = x[1]
    dc['v1'] += value_list[0]
    dc['n1'] += 1
    dc['v2'] += value_list[1]
    dc['n2'] += 1
    dc['v3'] += value_list[2]
    dc['n3'] += 1
with open("/home/egorlevkin/Downloads/dataset_3363_4_out.txt","w") as inf:
    for x in xs:
        inf.write(str(round(x, 9)))
        inf.write("\n")
    avg_1 = dc['v1']/dc['n1']
    avg_2 = dc['v2']/dc['n2']
    avg_3 = dc['v3']/dc['n3']
    inf.write(str(round(avg_1, 9)) + " " + str(round(avg_2, 9)) + " " + str(round(avg_3, 9)))
    inf.write("\n")