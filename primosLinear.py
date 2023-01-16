def primos_linear(num):
    if num < 0:
        return 'Invalid number'
    primos = []
    for i in range(2, num + 1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            primos.append(i)
    return primos


print(primos_linear(20))
