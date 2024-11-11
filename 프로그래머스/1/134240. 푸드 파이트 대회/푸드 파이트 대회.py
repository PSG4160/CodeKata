def solution(food): # 0을 기준으로 앞 숫자 작성 후 0과 역순을 더하기
    answer = ''
    for i in range(1,len(food)):
        k = int(food[i]) // 2
        for j in range(k):
            answer += str(i)
    
    re = answer[::-1]
    answer += '0'
    answer += re
    return answer