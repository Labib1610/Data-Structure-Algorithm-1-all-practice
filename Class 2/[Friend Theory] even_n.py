def even_n(n):
    if n<=1:
        return
    else:
        even_n(n-1)
        if n%2 == 0:
            print(n)

even_n(13)