def array_diff(a, b):
    #your code here
    return [x for x in a if (lambda x,xs: list(filter(lambda y: x == y, xs)) == [])(x,b)]