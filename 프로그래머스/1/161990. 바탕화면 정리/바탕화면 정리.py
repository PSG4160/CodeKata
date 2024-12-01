def solution(wallpaper):
    # lux = 리스트에서 맨 처음 "#"이 나오는 리스트 인덱스
    # luy = 리스트 문자열들 중에서  "#"이 제일 앞에 있는 문자열의 인덱스
    # rdx = 리스트에서 마지막으로 "#"이 나오는 리스트 인덱스 +1
    # rdy = 리스트 문자열들 중에서  "#"이 제일 마지막에 있는 문자열의 인덱스 +1   
    for index, char in enumerate(wallpaper):
        if "#" in char:
            lux = index
            break
    for index, char in enumerate(wallpaper):
        if "#" in char:
            rdx = index + 1      
        
    min_index = float('inf') # 초기값 무한대
    for index, char in enumerate(wallpaper):
        if "#" in char:
            char_index = char.index("#")
            if char_index < min_index:
                min_index = char_index
    luy = min_index
    
    max_index = 0
    for index, char in enumerate(wallpaper):
        if "#" in char:
            char_index = char.rindex("#") # char.rindex('#') 여러 #이 있으면 마지막 #의 인덱스 찾기
            if char_index > max_index:
                max_index = char_index
    rdy = max_index +1
    
    answer = [lux, luy, rdx, rdy]
    
    return answer