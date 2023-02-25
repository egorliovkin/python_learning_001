xs = "a aa abC aa ac abc bcd a".split(" ")
# xs = input().split(" ")
d ={}
for x in xs:
    if d.get(x.lower()) != None:
        d[x.lower()] += 1
    else:
        d[x.lower()] = 1


for k in d:
    print(k, d[k])
