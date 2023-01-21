xs = [1,0,1]
fs = [(lambda a, n: lambda x : a*pow(x,n))(xs[n],n) for n in range(len(xs))]

ffs = lambda x : sum([f(x) for f in fs])

print(ffs(2))