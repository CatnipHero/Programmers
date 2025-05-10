def solution(n):
    array = [[0] * n for _ in range(n)] 
    num = 1 
    row, col = 0, 0 
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0] 
    direction = 0 

    while num <= n * n:
        array[row][col] = num
        num += 1 
        next_row = row + dr[direction]
        next_col = col + dc[direction]

        if 0 <= next_row < n and 0 <= next_col < n and array[next_row][next_col] == 0:
            row, col = next_row, next_col
        else:
            direction = (direction + 1) % 4 
            row += dr[direction] 
            col += dc[direction] 

    return array