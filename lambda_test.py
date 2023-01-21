xs = [1,0,1]

# f1 = lambda x : [xs[0]*pow(x,0), xs[1]*pow(x,1)]
# f2 = lambda x : [xs[0]*pow(x,0), xs[1]*pow(x,1), xs[2]*pow(x,2)]
# f3 = lambda x : [xs[0]*pow(x,0), xs[1]*pow(x,2), xs[2]*pow(x,2), xs[3]*pow(x,3)]

# ffs = lambda xs : [(lambda a, n: lambda x : a*pow(x,n))(xs[n],n) for n in range(len(xs))]
# polinom = lambda x, xs : sum([f(x) for f in ffs(xs)])
# polinom = lambda x, xs : sum([f(x) for f in (lambda xs : [(lambda a, n: lambda x : a*pow(x,n))(xs[n],n) for n in range(len(xs))])(xs)])
polinom = lambda xs : lambda x : sum([f(x) for f in (lambda xs : [(lambda a, n: lambda x : a*pow(x,n))(xs[n],n) for n in range(len(xs))])(xs)])

print(polinom(xs)(2) == 5)
# print(f1(2))
# print(f2(2))
# print(f3(2))
# print(sum([f(2) for f in ffs(xs)]))
print(polinom(xs)(2))