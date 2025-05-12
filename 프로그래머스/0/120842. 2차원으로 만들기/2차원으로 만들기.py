def solution(num_list, n):
    vertical = len(num_list) // n #세로길이 = vertical, 가로길이 = n
    answer = [[0 for _ in range(n)] for _ in range(vertical)]  
    
    for i in range(len(num_list)):
        row = i // n
        col = i % n
        answer[row][col] = num_list[i]
        
    return answer