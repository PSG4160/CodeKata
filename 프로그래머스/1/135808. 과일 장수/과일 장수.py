def solution(k, m, score):
    # 점수 제일 높은 것들 기준으로 같이 m개 묶어서 k*m = score1 ... 2 ... 3 m개 묶을 수 있을때까지 구분 후 합계 계산하기
    sorted_score = sorted(score, reverse = True) # 역순 정렬하기
    #[4,4,4,4,4,4,2,2,2,2,1,1] m개로 묶기 m=3 k=4 len = 12
    a = 0
    for i in range(len(score)//m): # i = 0 1 2 3
        a += sorted_score[(i+1)*m-1]*m 
    return a
        
    