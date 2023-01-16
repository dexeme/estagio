def primos_recursiva(num):
    if num < 0:
        return 'Invalid number'
    if num == 0 or num == 1:
        return []
    if num == 2:
        return [2]
    primos = primos_recursiva(num - 1)
    for i in primos:
        if num % i == 0:
            return primos
    primos.append(num)
    return primos


print(primos_recursiva(20))
