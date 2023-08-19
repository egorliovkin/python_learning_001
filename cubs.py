limit = int(input())
xs = [sum(range(1,x+1)) for x in range(1,39+1)]
n = 0
while (c := limit - xs[n]) >= 0:
    limit = c
    n += 1
print(n)