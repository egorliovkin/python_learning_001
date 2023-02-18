xs = [23,23,21]

_max = max(xs)
_min = min(xs)
xs.remove(_min)
xs.remove(_max)

print(_max)
print(_min)
print(xs[0])