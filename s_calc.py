# put your python code here
import math
f = input()
if (f == "треугольник"):
    a = int(input())
    b = int(input())
    c = int(input())
    p = ((a + b + c )/ 2)
    s = math.sqrt(p*(p-a)*(p-b)*(p-c))
elif (f == "прямоугольник"):
    a = float(input())
    b = float(input())
    s = a*b
elif (f == "круг"):
    r = float(input())
    s = r**2 * 3.14
print(s)