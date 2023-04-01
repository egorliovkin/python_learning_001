d = int(input())
checker = {}
while d > 0:
    w = input().lower()
    if checker.get(w) == None:
        checker[w] = 1
    d -= 1
l = int(input())
test = {}
while l > 0:
    for w in input().lower().split():
        if test.get(w) == None:
            test[w] = 1
    l -= 1
for w in test.keys():
    if checker.get(w) == None:
        print(w)