def solution(answers):
    '''
    1번 : [1,2,3,4,5] 5개
    2번 : [2,1,2,3,2,4,2,5] 8개
    3번 : [3,3,1,1,2,2,4,4,5,5] 10개
    answers는 리스트
    인덱스별로 비교해서 같은 숫자들의 개수의 합
    제일 큰것
    오름차순
    '''
    student1 =[1,2,3,4,5]
    student2 = [2,1,2,3,2,4,2,5]
    student3 = [3,3,1,1,2,2,4,4,5,5]
    score1 = 0
    score2 = 0
    score3 = 0
    for i in range(len(answers)):
        if answers[i] == student1[i % len(student1)]:
            score1 += 1
        if answers[i] == student2[i % len(student2)]:
            score2 += 1
        if answers[i] == student3[i % len(student3)]:
            score3 += 1
    scores = [score1, score2, score3]  
    max_score = max(scores)
    

    result = [i + 1 for i in range(len(scores)) if scores[i] == max_score]
    
    return result
    