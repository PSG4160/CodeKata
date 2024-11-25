def solution(n, lost, reserve):
    # 여벌 체육복을 가지고 있지만 도난당한 학생 처리
    reserve_set = set(reserve) - set(lost)
    lost_set = set(lost) - set(reserve)
    
    # 체육복 대여
    for r in sorted(reserve_set):  # 여벌 체육복을 가진 학생
        if r - 1 in lost_set:  # 앞 번호 학생이 체육복을 도난당했으면 빌려줌
            lost_set.remove(r - 1)
        elif r + 1 in lost_set:  # 뒷 번호 학생이 체육복을 도난당했으면 빌려줌
            lost_set.remove(r + 1)
    
    # 전체 학생 수에서 도난당한 학생 중 체육복을 못 받은 학생 수를 뺌
    return n - len(lost_set)
