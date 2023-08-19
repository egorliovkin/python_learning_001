from math import floor
# n, m = map(int, input().split())
n = 2
m = 2
a = 0
while n > 0:
    a += 1
    n -= 1    
    if a % m == 0:
        n += 1
    if n == 0:
        break
print(a)