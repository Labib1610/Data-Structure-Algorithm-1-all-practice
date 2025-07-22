def linear_search(lst, key):
    for i in range(len(lst)):
        if lst[i] == key:
           return ("FOUND", i)
        
    return ("NOT FOUND", None) 

lst = [8, 9, 2, 5, 4, 6, 1]
print(linear_search(lst, 11))
