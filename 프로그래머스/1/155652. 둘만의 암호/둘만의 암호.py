def solution(s, skip, index):
    # 알파벳 리스트에서 skip 문자를 제외
    alp = list("abcdefghijklmnopqrstuvwxyz")
    # 'a'부터 'z'까지 알파벳
    alp = [char for char in alp if char not in skip]
    
    # 결과를 저장할 리스트
    answer = []
    
    # 각 문자에 대해 변환 작업 수행
    for char in s:
        # 현재 문자의 인덱스 찾기
        current_index = alp.index(char)
        
        # 새로운 위치 계산 (순환 처리)
        new_index = (current_index + index) % len(alp)
        
        # 변환된 문자 추가
        answer.append(alp[new_index])
    
    # 리스트를 문자열로 변환하여 반환
    return ''.join(answer)
