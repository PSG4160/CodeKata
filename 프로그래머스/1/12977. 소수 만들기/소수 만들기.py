from itertools import combinations

def solution(nums):
    answer = 0    
    # nums 리스트에서 3개의 숫자를 골라 합 리스트 생성
    three = [a + b + c for a, b, c in combinations(nums, 3)]
    
    for i in three:  # 각 합에 대해 소수 판별
        for j in range(2, int(i ** 0.5) + 1):  # 2부터 제곱근까지 확인
            if i % j == 0:  # 나누어떨어지면 소수가 아님
                break  # 더 이상 검사하지 않고 중단
        else:  # for 루프가 break 없이 끝났다면 소수
            answer += 1  # 소수의 개수를 증가

    return answer