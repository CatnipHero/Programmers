def solution(my_string):
    answer = ''
    for i in my_string:
        if i == "a" or i == "e" or i == "i" or i == "u" or i == "o":
            answer += ""
        else:
            answer += i
            
    return answer