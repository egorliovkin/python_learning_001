# n1, n2 = map(int, input().split())
n1, n2 = 11, 2
# xs1 = [int(x) for x in input().split()]
xs1 = [int(x) for x in "1 1 1 3 4 5 6 7 8 8 10".split()]
# xs2 = [int(x) for x in input().split()]
xs2 = [int(x) for x in "4 9".split()]

i = 0
xs = xs1 + xs2
res = []
while i < len(xs):
    res += [min(xs)]
    xs.remove(min(xs))
print(*res)