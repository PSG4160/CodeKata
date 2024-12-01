from datetime import datetime

def solution(today, terms, privacies):
    answer = []
    # 오늘 날짜를 정수로 변환 (YYYYMMDD 형태)
    year, month, day = map(int, today.split("."))
    today_int = year * 12 * 28 + month * 28 + day  # 28일 기준으로 변환
    
    # 약관 종류와 유효 기간(일수)을 딕셔너리로 변환
    terms_dict = {}
    for term in terms:
        key, value = term.split()
        terms_dict[key] = int(value) * 28  # 개월 수를 일수로 변환
    
    # 개인정보 유효성 검사
    for index, privacy in enumerate(privacies):
        p_date_str, term_type = privacy.split()
        p_year, p_month, p_day = map(int, p_date_str.split("."))
        
        # 개인정보 날짜를 정수로 변환
        p_date_int = p_year * 12 * 28 + p_month * 28 + p_day
        
        # 유효 날짜 계산
        validity_int = p_date_int + terms_dict[term_type]
        
        # 유효 기간 초과 여부 확인
        if validity_int <= today_int:
            answer.append(index + 1)
    
    return answer
