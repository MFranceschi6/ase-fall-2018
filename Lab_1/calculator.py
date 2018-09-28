#calculator.py

def sum(n, m):
    result = m
    if n < 0:
        for i in range(-n):
            result -= 1
    else:
        for i in range(n):
            result += 1
    return result
        

def divide(m, n):
    result = 0
    if n == 0:
        raise ZeroDivisionError
    negativeResult = m > 0 and n < 0 or m < 0 and n > 0
    n = abs(n) 
    m = abs(m)

    while (m - n >= 0):
        m -= n
        result += 1

    result = -result if negativeResult else result
    
    return result
        