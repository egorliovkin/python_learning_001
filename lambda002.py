# def mul2(a):
#     return a * 2
# def mul4(a):
#     return a * 4
# def mul8(a):
#     return a * 8
# def mul16(a):
#     return a * 16
def mapper(xs, f):
    return [f(x) for x in xs]
d = [1,2,3,0,9,8]
# print(mapper(d, mul2))
# print(mapper(d, mul4))
# print(mapper(d, mul8))
# print(mapper(d, mul16))
# print(mapper(d, lambda x: x* 2))
# print(mapper([1,2,3,0,9,8], lambda x: x* 2))
print(mapper(['a','b','c'], lambda x: chr(ord(x) + 2)))