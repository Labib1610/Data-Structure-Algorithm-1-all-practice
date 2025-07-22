# Iterative Method
def binary_search(lst, key):
    low = 0
    high = len(lst)-1

    while low<=high:
        mid = (low + high) // 2
        if lst[mid] == key:
            return ("FOUND", mid)
        elif key>lst[mid]:
            low = mid + 1
        else:
            high = mid - 1
    
    return ("NOT FOUND", None)

# Recursive Method
def binary_search(lst, key, low, high):
    if low > high:
        return ("NOT FOUND", None)
    mid = (low + high) // 2
    if lst[mid] == key:
        return ("FOUND", mid)
    elif key>lst[mid]:
        return binary_search(lst, key, mid+1, high)
    else:
        return binary_search(lst, key, low, mid-1)

# Driver Codes
lst = [5, 7, 9, 12, 25, 27]

res = binary_search(lst, 12)

if res[1] != None:
    print(f"{res[0]} at Index {res[1]}")
else:
    print(f"{res[0]}")