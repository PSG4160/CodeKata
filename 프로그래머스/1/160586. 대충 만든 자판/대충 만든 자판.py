from collections import defaultdict

def solution(keymap, targets):
    # 각 문자의 최소 입력값을 저장
    key_map_lst = defaultdict(lambda: float('inf'))
    
    # keymap으로 최소 입력값 설정
    for string in keymap:
        for idx, char in enumerate(string):
            key_map_lst[char] = min(key_map_lst[char], idx + 1)
    
    answer = []
    for string in targets:
        result = 0
        for char in string:
            # 해당 문자가 keymap에 없으면 -1 처리
            if key_map_lst[char] == float('inf'):
                result = -1
                break
            result += key_map_lst[char]
        answer.append(result)
    
    return answer