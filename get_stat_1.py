def getDict(xs):
    dc = {}
    for x in xs:
        if dc.get(x) != None:
            dc[x] += 1
        else:
            dc[x] = 1
    return dc

with open("/home/egorlevkin/Downloads/dataset_3363_3.txt") as inf:
    dc = getDict(sorted([x.lower() for x in inf.read().strip().split()]))
    mv=0
    md={}
    for k in dc.keys():
        if dc[k] > mv:
            mv=dc[k]
            md={k:dc[k]}
    for k in md.keys():
    
            print(k+" "+str(md[k]))
    