# # 1
# def solution(numbers): # 두 수들의 합들 리스트 만들고, 오름차순 정렬 후 중복 삭제
#     answer = []
#     for i in range(len(numbers)-1): # 전체 리스트 number에서 마지막 하나를 제외한 반복
#         for j in range(i+1,len(numbers)): # i다음 인덱스 부터 마지막 인덱스 까지 반복
#             k = numbers[i] + numbers[j]  # k = 두 수들의 합
#             answer.append(k)            # k를 append 해줌 
#     answer.sort()                         # answer 정렬함
#     unique_lst = []
#     for num in answer:
#         if num not in unique_lst:
#             unique_lst.append(num)
        
#     return unique_lst

# 2
from itertools import combinations

def solution(numbers):
    # 모든 두 수의 합을 구하고 중복 없이 저장
    answer = {a + b for a, b in combinations(numbers, 2)}
    # 정렬하여 리스트로 반환
    return sorted(answer)