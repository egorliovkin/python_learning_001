def listGen(xs):
    if len(xs) == 0:
        return set([])
    elif len(xs) == 1:
        return set(xs)
    elif len(xs) == 2:
        return set([xs,xs[::-1]])
    else:
        res = set([])
        for i in range(len(xs)):
            bs = xs[:i] + xs[i+1:]
            [res.add(x) for x in [xs[i] + x for x in listGen(bs)]]
        return res

print(sorted(listGen('ABAB')))