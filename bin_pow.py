# import math

# b = math.log(a := int(input()),2)
# if math.pow(2, int(b)) == a:
#     print(int(b))
# else:
#     print("НЕТ")

xs = bin(int(input()))[3:]
if sum([int(x) for x in xs]) == 0:
    print(len(xs))
else:
    print("НЕТ")