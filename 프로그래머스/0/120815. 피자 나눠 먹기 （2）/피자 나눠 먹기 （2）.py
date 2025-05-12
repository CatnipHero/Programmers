def solution(n):
    a = n
    while True:
        if n % 6 == 0:
            return n // 6
        else:
            n += a