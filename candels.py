a = 4
b = 2

def get_rest(a, b):
    if a < b:
        return a
    elif a == b:
        return a + 1
    else:
        return a + get_rest(a//b, b)
    
print(get_rest(a, b))