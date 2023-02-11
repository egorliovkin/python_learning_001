import functools
import operator
xs = input()
foldl = lambda func, acc, xs: functools.reduce(func, xs, acc)
a = foldl(operator.add, 0, [int(x) for x in xs[:3]])
b = foldl(operator.add, 0, [int(x) for x in xs[3:]])
if a == b:
    print("Счастливый")
else:
    print("Обычный")