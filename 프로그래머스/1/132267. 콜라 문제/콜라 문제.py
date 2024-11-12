def solution(a, b, n):
    # a = 콜라를 받기 위해 주어야 하는 병 수,
    # b = a개를 가져다 주면 마트가 주는 콜라 병 수
    # n = 빈 병의 개수
    # 받을 수 있는 콜라 병 수를 return 해라 리턴 받는 값을 리턴해라
    
    # (n // a) * b # 처음 리턴 받는 병 수
    # n2 = (n % a) + (리턴 받는 병 수)
    answer = 0
    while n >= a:
        return_bottle = (n // a) * b
        answer += return_bottle
        n = return_bottle + (n % a)

    return answer