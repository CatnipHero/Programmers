def solution(numer1, denom1, numer2, denom2):
    num1 = (numer1 * denom2) + (numer2 * denom1)
    num2 = denom1 * denom2
    
    a = num1
    b = num2
    while b:
        a, b = b, a % b
    
    num1, num2 = num1 // a, num2 // a
    return [num1, num2]