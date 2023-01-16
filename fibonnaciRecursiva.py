def fibonnaci_recursiva(num):
    if num < 0:
        return 'Invalid number'
    elif num == 0 or num == 1:
        return num
    else:
        return fibonnaci_recursiva(num-1) + fibonnaci_recursiva(num-2)


print(fibonnaci_recursiva(5))
