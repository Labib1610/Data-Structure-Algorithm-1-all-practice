def factorial(n):
    if n==0 or n==1:
        return n
    else:
        friend = factorial(n-1)
        result = friend * n
        return result

print(factorial(50))