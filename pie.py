from math import log

def pie_counter(a: int):
    if a == 1:
        return 0
    elif ( a % 2 == 0 ):
        return a //2
    else:
        return a

print(pie_counter(1))
print(pie_counter(2))
print(pie_counter(3))
print(pie_counter(4))
print(pie_counter(5))
print(pie_counter(6))
print(pie_counter(7))
print(pie_counter(8))
print(pie_counter(9))
print(pie_counter(12))
