'''
복잡도 계산 실패
def solution(number, limit, power):
    answer = 0 # 철의 무게 합들
    
    for i in range(1,number+1): # 1번부터 number번 기사
    # 약수의 개수 구하기
        k = 0   # 약수의 개수 = 공격력
        for j in range(1,i+1):
            if i % j  == 0:
                k += 1
        if k > limit:
            answer += power
        else:
            answer += k
    return answer
'''
def solution(number, limit, power):
    # 약수 개수 저장 리스트
    divisors = [0] * (number + 1)

    # 약수 개수 계산
    for i in range(1, number + 1):
        for j in range(i, number + 1, i):
            divisors[j] += 1

    # 약수 개수를 기반으로 무게 계산
    answer = 0
    for k in range(1, number + 1):
        if divisors[k] > limit:
            answer += power
        else:
            answer += divisors[k]

    return answer
