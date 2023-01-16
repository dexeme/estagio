def linear_fibonacci(num):
    if num < 0:
        return 'Invalid number'
    a = 0
    b = 1
    for i in range(num):
        a, b = b, a + b
    return a


print(linear_fibonacci(5))
