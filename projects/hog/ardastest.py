def test():
    score0 = 0 
    score1 = 0 
    score1_2 = 0
    while score0 < 100 and score1 < 100:
        score0 = score0 + 100
        if score0 >= 100:

    return score0, score1


    def play(strategy0, strategy1, score0=0, score1=0, dice=six_sided,
         goal=GOAL_SCORE, say=silence, feral_hogs=True):
    """Simulate a game and return the final scores of both players, with Player
    0's score first, and Player 1's score second.

    A strategy is a function that takes two total scores as arguments (the
    current player's score, and the opponent's score), and returns a number of
    dice that the current player will roll this turn.

    strategy0:  The strategy function for Player 0, who plays first.
    strategy1:  The strategy function for Player 1, who plays second.
    score0:     Starting score for Player 0
    score1:     Starting score for Player 1
    dice:       A function of zero arguments that simulates a dice roll.
    goal:       The game ends and someone wins when this score is reached.
    say:        The commentary function to call at the end of the first turn.
    feral_hogs: A boolean indicating whether the feral hogs rule should be active.
    """
    who = 0  # Who is about to take a turn, 0 (first) or 1 (second)
    # BEGIN PROBLEM 5
    strat0 = strategy0(score0, score1)
    strat1 = strategy1(score1, score0)
    while score0 < goal and score1 < goal:
        if strat0 >= 1:
            score0 = roll_dice(strat0, dice) + score0
        else:
            score0 = free_bacon(score1) + score0

        if score0 >= goal:
            score1 = score1
        elif strat1 >=1:
            score1 = roll_dice(strat1, dice) + score1
        else:
            score1 = free_bacon(score0) + score1

        while score0 < goal and score1 < goal:
            if is_swap(score0, score1):
                score0 = score1
                score 

    # END PROBLEM 5
    # (note that the indentation for the problem 6 prompt (***YOUR CODE HERE***) might be misleading)
    # BEGIN PROBLEM 6
    # END PROBLEM 6
    return score0, score1

    def take_turn(num_rolls, opponent_score, dice=six_sided):
    """Simulate a turn rolling NUM_ROLLS dice, which may be 0 (Free Bacon).
    Return the points scored for the turn by the current player.

    num_rolls:       The number of dice rolls that will be made.
    opponent_score:  The total score of the opponent.
    dice:            A function that simulates a single dice roll outcome.
    """
    # Leave these assert statements here; they help check for errors.
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls >= 0, 'Cannot roll a negative number of dice in take_turn.'
    assert num_rolls <= 10, 'Cannot roll more than 10 dice.'
    assert opponent_score < 100, 'The game should be over.'
    # BEGIN PROBLEM 3
    if num_rolls == 0:
        return free_bacon(opponent_score)
    else:
        return roll_dice(num_rolls, dice)
    # END PROBLEM 3

def is_swap(player_score, opponent_score):
    """
    Return whether the two scores should be swapped
    """
    # BEGIN PROBLEM 4
    swaptotal = player_score + opponent_score
    excitement  = 3 ** swaptotal
    last_dig = excitement % 10 
    while excitement>0:
        first_dig = excitement % 10 
        excitement = excitement // 10
    if first_dig == last_dig:
        return True 
    else:
        return False
    # END PROBLEM 4






