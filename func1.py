def f(x):
    # 1−(x+2)**2 при x≤−2
    # −x/2 при −2<x≤2
    # (x - 2) ** 2 + 1 при 2 < x​
    if x <= -2:
        return 1 - (x+2) ** 2
    elif (-2 < x) & (x <= 2):
        return -x / 2
    else:
        return (x - 2) ** 2 + 1

print(f(4.5))
print(f(-4.5))
print(f(1))