xss = []
with open("/home/egorlevkin/Downloads/dataset_3363_4.txt") as inf:
    xss = [(x[0],[int(x[1]),int(x[2]),int(x[3])]) for x in [x.split(';') for x in inf.read().strip().split()]]
xs = [sum(x[1])/3 for x in xss]
dc_value = {'1': 0, '2': 0, '3': 0}
dc_num = {'1': 0, '2': 0, '3': 0}
for x in xss:
    name = x[0]
    value_list = x[1]
    dc_value['1'] += value_list[0]
    dc_num['1'] += 1
    dc_value['2'] += value_list[1]
    dc_num['2'] += 1
    dc_value['3'] += value_list[2]
    dc_num['3'] += 1
with open("/home/egorlevkin/Downloads/dataset_3363_4_out.txt","w") as inf:
    for x in xs:
        inf.write(str(round(x, 9)))
        inf.write("\n")
    avg_1 = dc_value['1']/dc_num['1']
    avg_2 = dc_value['2']/dc_num['2']
    avg_3 = dc_value['3']/dc_num['3']
    inf.write(str(round(avg_1, 9)) + " " + str(round(avg_2, 9)) + " " + str(round(avg_3, 9)))
    inf.write("\n")