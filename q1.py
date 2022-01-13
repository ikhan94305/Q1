def solution(lottos, win_nums):
    zero = 0
    match = 0
    for i in lottos:
        if i == 0:
            zero += 1
            match += 1
        elif i in win_nums:
            match += 1
    if zero == 6:
        return [1,6]
    return [7-match, 7-match+zero]

lottos = [31,10,45,1,6,19]
win_nums = [31, 10, 45, 1, 6, 19]
answer = solution(lottos, win_nums)
print(answer)
