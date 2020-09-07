

def is_swap(player_score, opponent_score):
    swaptotal = player_score + opponent_score
    excitement = pow(3, swaptotal)
    last_digit = excitement % 10
    while excitement > 0:
        first_dig = excitement % 10
        excitement = excitement // 10
    if first_dig == last_dig:
        return True
    else:
        return False