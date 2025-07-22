def print_number(n):
    if n == 1:
        print(1)
    else:
        print_number(n-1)
        print(n)

print_number(5)