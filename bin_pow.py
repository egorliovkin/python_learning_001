import math

b = math.log(a := int(input()),2)
if math.pow(2, int(b)) == a:
    print(int(b))
else:
    print("НЕТ")