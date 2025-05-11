def solution(slice, n):
    i = 2
    while slice < n:
        slice = slice*i/(i-1)
        i += 1
        
    return i-1