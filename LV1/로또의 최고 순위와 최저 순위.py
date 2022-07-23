def solution(lottos, win_nums):
    correct = 0
    rank = [6,6,5,4,3,2,1]
    zeros = lottos.count(0) # 내 로또 속 0의 갯수
    for lotto in lottos:
        for win_num in win_nums:
            if lotto == win_num:
                correct += 1 # 맞힌 갯수
    return [rank[correct+zeros],rank[correct]]
