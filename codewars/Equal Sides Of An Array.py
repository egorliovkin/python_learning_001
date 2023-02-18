def find_even_index(arr):
    # fs = lambda xs: [n for n in range(len(xs)) if (sum(xs[:n]) == sum(xs[n+1:]))]
    xs = [n for n in range(len(arr)) if (sum(arr[:n]) == sum(arr[n+1:]))]
    return -1 if xs == [] else xs[0]

print(find_even_index([1,2,3,4,3,2,1]),3)
print(find_even_index([1,100,50,-51,1,1]),1,)
print(find_even_index([1,2,3,4,5,6]),-1)
print(find_even_index([20,10,30,10,10,15,35]),3)
print(find_even_index([20,10,-80,10,10,15,35]),0)
print(find_even_index([10,-80,10,10,15,35,20]),6)
print(find_even_index(list(range(1,100))),-1)
print(find_even_index([0,0,0,0,0]),0,"Should pick the first index if more cases are valid")
print(find_even_index([-1,-2,-3,-4,-3,-2,-1]),3)
print(find_even_index(list(range(-100,-1))),-1)
