def solution(lottos, win_nums):
    #인덱스를 이용해서 로또 당첨 순위 계산
    answer = [6,6,5,4,3,2,1]
    #lottos와 win_nums 리스트들의 중복 값 확인
    #교집합을 통해 중복 갯수 확인
    common_elements = set(lottos) & set(win_nums)
    k = len(common_elements)
    #lottos안의 0갯수 확인
    zero_count = 0
    for i in lottos:
        if i==0:
            zero_count += 1
    first = answer[k+zero_count]
    fail = answer[k]
    return [first,fail]
    
