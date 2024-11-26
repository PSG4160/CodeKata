def solution(s):
    count = 0   
    x_count = 0 # x 개수
    other_count = 0 # x가 아닌 수의 개수
    x = None
    
    for char in s:
        if x is None:
            x = char
            x_count = 1
        elif char == x:
            x_count += 1
        else:
            other_count += 1
        
        if x_count == other_count:
            count += 1
            x = None
            x_count = 0
            other_count = 0
    
    if x is not None:
        count += 1
    
    return count
            
            
        
    
