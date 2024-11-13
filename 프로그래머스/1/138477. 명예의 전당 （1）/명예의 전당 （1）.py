def solution(k, score):  # k 번째 까지 제일 작은 값 return하기,  k번째 이후는 k번째로 큰 값 return
    answer = []
    for i in range(len(score)):
        if i < k:
            m = sorted(score[:i+1])
            answer.append(m[0])
        else:
            M = sorted(score[:i+1]) 
            answer.append(M[-k])

    return answer