from collections import defaultdict
def solution(id_list, report, k):
    users = defaultdict(set) # {신고된 사람: 신고한 사람}
    mail_cnt = defaultdict(int) # 각 유저별 받을 결과 메일 수
    
    for rep in report:
        a,b = rep.split()
        users[b].add(a)
    
    for u in users:
        if len(users[u]) >= k: # k번이상 신고받은 유저
            for i in users[u]: # 신고받은 유저를 신고한 유저 대상 메일 송부
                mail_cnt[i] += 1
                
    answer = []
    for id in id_list:
        answer.append(mail_cnt[id])
    return answer
            
    
