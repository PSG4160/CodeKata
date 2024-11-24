def solution(X, Y):
    # 0~9 숫자의 빈도를 저장하는 배열
    count_x = [0] * 10
    count_y = [0] * 10

    # X와 Y의 각 숫자 빈도를 계산
    for i in X:
        count_x[int(i)] += 1
    for i in Y:
        count_y[int(i)] += 1

    # 공통 숫자와 최소 빈도로 결과 생성
    result = []
    for i in range(9, -1, -1):  # 9부터 0까지 역순으로 확인
        common_count = min(count_x[i], count_y[i])
        result.extend([str(i)] * common_count)

    # 결과 처리
    if not result:  # 공통 숫자가 없으면
        return '-1'
    if result[0] == '0':  # 공통 숫자가 0만 있으면
        return '0'

    return ''.join(result)
