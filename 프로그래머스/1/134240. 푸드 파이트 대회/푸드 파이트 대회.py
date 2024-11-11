"""# 1. 0을 기준으로 앞 숫자 작성 후 0과 역순을 더하기
def solution(food):  
    answer = ''
    for i in range(1,len(food)):
        k = int(food[i]) // 2
        for j in range(k):
            answer += str(i)
    
    re = answer[::-1]
    answer += '0'
    answer += re
    return answer
"""
# 2 역순으로 두개씩 중앙(0)에서부터 배치하기

def solution(food):
    answer ="0"
    for i in range(len(food)-1, 0,-1):
        c = int(food[i]/2)
        while c>0:
            answer = str(i) + answer + str(i)
            c -= 1
    return answer