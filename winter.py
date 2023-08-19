def bursa(a, b):
    if a == 1:
        return b
    elif (c := b * a) > 1000000000:
        return b
    else:
        xs = str(c)
        return bursa(int(xs[:1]),int(xs))

xs = input()
print(bursa(int(xs[:1]),int(xs)))