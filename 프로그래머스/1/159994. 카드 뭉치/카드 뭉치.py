def solution(cards1, cards2, goal):
    nested_list = [cards1, cards2]
    goal_met = True  # 목표가 충족되었는지 추적

    for k in goal:
        found = False  # 현재 k가 제거되었는지 추적
        for sublist in nested_list:
            if sublist and sublist[0] == k:
                sublist.pop(0)  # 첫 번째 요소 제거
                found = True  # k를 찾았음을 표시
                break  # 다른 리스트를 검사할 필요 없음
        if not found:  # k를 제거할 수 없었다면 목표 실패
            goal_met = False
            break

    if goal_met:
        return "Yes" # 모든 k를 제거한 경우
    else:
       return "No" # 제거하지 못한 경우