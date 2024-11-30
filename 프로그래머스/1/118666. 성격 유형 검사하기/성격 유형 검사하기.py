def solution(survey, choices):
    personality_scores = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}
    score_map = {1: 3, 2: 2, 3: 1, 4: 0, 5: 1, 6: 2, 7: 3}
    
    for s, c in zip(survey, choices):
        if c < 4:
            personality_scores[s[0]] += score_map[c]
        elif c > 4:
            personality_scores[s[1]] += score_map[c]
    
    result = ''
    result += 'R' if personality_scores['R'] >= personality_scores['T'] else 'T'
    result += 'C' if personality_scores['C'] >= personality_scores['F'] else 'F'
    result += 'J' if personality_scores['J'] >= personality_scores['M'] else 'M'
    result += 'A' if personality_scores['A'] >= personality_scores['N'] else 'N'
    
    return result