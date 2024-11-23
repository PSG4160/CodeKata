def solution(babbling):
    patterns = ["aya", "ye", "woo", "ma"]  # 발음 가능한 단어들
    answer = 0

    for word in babbling:  # 각 단어를 검사
        valid = True  # 유효성 플래그
        prev_pattern = ""  # 이전 패턴 저장

        while word:  # 단어가 남아 있는 동안 반복
            matched = False  # 패턴 매칭 여부 초기화
            for pattern in patterns:
                # 단어가 특정 패턴으로 시작하고, 이전 패턴과 다를 경우
                if word.startswith(pattern) and pattern != prev_pattern:
                    word = word[len(pattern):]  # 패턴 제거
                    prev_pattern = pattern  # 현재 패턴을 이전 패턴으로 저장
                    matched = True  # 매칭 성공
                    break  # 현재 패턴을 처리했으므로 루프 종료
            if not matched:  # 어떤 패턴에도 매칭되지 않으면 무효
                valid = False
                break
        
        if valid and not word:  # 모든 조건을 만족하면 유효한 발음
            answer += 1

    return answer
