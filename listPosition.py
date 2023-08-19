def listGen(xs):
    if len(xs) == 0:
        return set([])
    elif len(xs) == 1:
        return set(xs)
    elif len(xs) == 2:
        return set(sorted([xs,xs[::-1]]))
    else:
        res = set([])
        for i in range(len(xs)):
            bs = xs[:i] + xs[i+1:]
            # [res.add(x) for x in [xs[i] + x for x in listGen(bs)]]
            res.update([xs[i] + x for x in sorted(listGen(bs))])
            # res = set(sorted(res))
        return res

def listPosition(x):
    return sorted(listGen(x)).index(x) + 1
    # return list(listGen(x)).index(x) + 1

print(listPosition('ABAB'))
# print(listPosition('AAAB'))
# print(listPosition('BAAA'))
# print(listPosition('QUESTION'))
# print(listPosition('BOOKKEEPER'))

# print(list(listGen('ABAB')))
# print(set(sorted(listGen('ABAB'))))
# print(listGen(''.join(sorted('QUESTION'))))
# print(listGen(''.join(sorted('BOOKKEEPER'))))