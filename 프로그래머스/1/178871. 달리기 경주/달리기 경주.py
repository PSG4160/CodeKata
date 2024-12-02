def solution(players, callings):
    # 딕셔너리로 플레이어의 현재 위치를 관리
    player_positions = {player: i for i, player in enumerate(players)}

    for char in callings:
        # 호출된 플레이어의 현재 위치
        current_index = player_positions[char]

        # 첫 번째 위치인 경우 스킵
        if current_index == 0:
            continue

        # 스왑할 플레이어와 위치 갱신
        previous_player = players[current_index - 1]
        players[current_index], players[current_index - 1] = (
            players[current_index - 1],
            players[current_index],
        )
        player_positions[char] -= 1
        player_positions[previous_player] += 1

    return players
