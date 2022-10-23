def nazi_hunter(arr):
    n = len(arr)+1
    tot = sum(arr)
    missing = (n * (n+1))/2 - tot
    return missing


arr = [1, 2, 3, 4, 5, 6, 8]
print(nazi_hunter(arr))