def solution(n):
    for i in range(1,1001):
        if n / i**2 == 1:
            return 1
    return 2