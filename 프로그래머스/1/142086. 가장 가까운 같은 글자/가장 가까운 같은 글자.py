#  for문 이용해서, 인덱스 앞에와 같지 않으면 -1 반환하고 같은것이 있다면 인덱스의 차를 이용해 거리를 구해보자
# 1
'''
def solution(s):
    answer = []
    for i in range(len(s)):
        # 현재 문자 이전에 같은 문자가 있는지 확인
        if s[i] not in s[:i]:  # `s[:i]`는 `0`부터 `i-1`까지 슬라이싱
            answer.append(-1)
        else:
            # 가장 가까운 위치의 인덱스 차이를 계산
            last_index = s[:i].rfind(s[i])  # `s[i]`가 마지막으로 등장한 위치 찾기
            distance = i - last_index       # 거리 계산
            answer.append(distance)
    return answer
'''
# 2 rfind()함수를 사용하지 않고 구하기

def solution(s):
    answer = []
    for i in range(len(s)):
        # 현재 문자가 이전에 등장했는지 확인
        found = False
        for j in range(i - 1, -1, -1):  # 현재 인덱스 `i`의 바로 앞부터 역순으로 순회
            if s[j] == s[i]:  # 같은 문자를 찾으면
                answer.append(i - j)  # 현재 위치 `i`와 이전 위치 `j`의 차이를 추가
                found = True
                break  # 가장 가까운 위치를 찾았으므로 반복 종료
        if not found:
            answer.append(-1)  # 이전에 같은 문자가 없으면 -1 추가
    return answer