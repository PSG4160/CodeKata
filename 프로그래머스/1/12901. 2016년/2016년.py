def solution(a, b):
    day_of_week = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
    days_in_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    month_start_index = [5, 1, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]  # 각 월의 1일이 시작되는 요일의 인덱스

    # 입력한 월의 시작 요일 인덱스 가져오기
    start_day_index = month_start_index[a - 1]
    
    # 해당 월의 날짜에 따라 요일 계산
    c = (start_day_index + (b - 1)) % 7
    return day_of_week[c]



