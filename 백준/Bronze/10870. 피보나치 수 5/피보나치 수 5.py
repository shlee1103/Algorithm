def fibonacci(n):
    if n <= 1:
        return n 
    
    result = fibonacci(n-1) + fibonacci(n-2)

    return result

num = int(input())
result = fibonacci(num)
print(result)