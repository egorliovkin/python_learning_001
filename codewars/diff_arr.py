def array_diff(a, b):
    #your code here
    return [x for x in a if not x in b]

print(array_diff([1,2],[1]) == [2])
print(array_diff([1,2,2,2,3],[2]) == [1,3])