def solution(ingredient):
    # 1 빵 2 야채 3 고기 1231 이 하나의 포장상태
    # ingredient 는 123들의 리스트
    stack = ''
    count = 0
    
    for item in ingredient:
        stack += str(item)
        if len(stack) >= 4 and stack[-1] == '1' and stack[-4:] == '1231':
            count += 1
            stack = stack[:-4]
    
    return count

            
