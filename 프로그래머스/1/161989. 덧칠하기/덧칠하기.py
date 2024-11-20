def solution(n, m, section):
    # 최소 페인트칠 횟수
    answer = 0
    # 현재 칠하지 않은 구역의 시작점
    current = 0

    for s in section:
        if s > current:  # 현재 롤러가 덮지 못하는 구역이라면
            answer += 1  # 롤러로 새로 칠하기
            current = s + m - 1  # 롤러로 칠한 끝 구역 업데이트

    return answer
