import math
polinom = lambda xs: lambda x : sum([xs[n] * pow(x, n) for n in list(range(len(xs)))])
ffs = lambda x,a,b,f: (a+b)/2 if (abs(f((a+b)/2) - x) < 0.0000000000000005) else ffs(x,a,(a+b)/2,f) if (f((a+b)/2) > x) else ffs(x,(a+b)/2,b,f)
print(ffs(2,1,2,polinom([0,0,1])))
print(math.sqrt(2))