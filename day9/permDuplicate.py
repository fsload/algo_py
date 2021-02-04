from itertools import product


arr = [1,2,3,4,5,6]
for i in product(arr, repeat=2):
    print(i, end=' ')