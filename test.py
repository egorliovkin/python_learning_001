import math

a = int(input())
b = int(input())
c = int(input())
D1 = b**2 - 4*a*c
if D1>0:
    x1 = (-b+math.sqrt(D1))/(2*a)
    x2 = (-b-math.sqrt(D1))/(2*a)
    print(f"Корень x1 == {x1}")
    print(f"Корень x2 == {x2}")
elif D1==0:
    x = -b/(-2*a)
    print(x)
else:
    print("нет корня")
    