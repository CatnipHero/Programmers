def solution(before, after):
    before_list = sorted(before)
    after_list = sorted(after)
    if before_list == after_list:
        return 1
    return 0