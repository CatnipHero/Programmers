def solution(my_string):
    answer = ''
    for i in my_string:
        if i not in answer:
            answer += i
        elif i in answer:
            pass
    return answer