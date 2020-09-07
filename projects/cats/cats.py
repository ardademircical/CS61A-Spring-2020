"""Typing test implementation"""

from utils import *
from ucb import main, interact, trace
from datetime import datetime


###########
# Phase 1 #
###########


def choose(paragraphs, select, k):
    """Return the Kth paragraph from PARAGRAPHS for which SELECT called on the
    paragraph returns true. If there are fewer than K such paragraphs, return
    the empty string.
    """
    # BEGIN PROBLEM 1
    loc_list = []
    for x in paragraphs:
        if select(x):
            loc_list += [x]
    if len(loc_list) >= k+1:
        return loc_list[k]
    else:
        return ''
    # END PROBLEM 1


def about(topic):
    """Return a select function that returns whether a paragraph contains one
    of the words in TOPIC.

    >>> about_dogs = about(['dog', 'dogs', 'pup', 'puppy'])
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup!'], about_dogs, 0)
    'Cute Dog!'
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup.'], about_dogs, 1)
    'Nice pup.'
    """
    assert all([lower(x) == x for x in topic]), 'topics should be lowercase.'
    # BEGIN PROBLEM 2

    def inabout(paragraphs):
        editx = split(remove_punctuation(lower(paragraphs)))
        list2 = [word in editx for word in topic]
        if True in list2:
            return True
        else:
            return False

    return inabout
    # END PROBLEM 2

def accuracy(typed, reference):
    """Return the accuracy (percentage of words typed correctly) of TYPED
    when compared to the prefix of REFERENCE that was typed.

    >>> accuracy('Cute Dog!', 'Cute Dog.')
    50.0
    >>> accuracy('A Cute Dog!', 'Cute Dog.')
    0.0
    >>> accuracy('cute Dog.', 'Cute Dog.')
    50.0
    >>> accuracy('Cute Dog. I say!', 'Cute Dog.')
    50.0
    >>> accuracy('Cute', 'Cute Dog.')
    100.0
    >>> accuracy('', 'Cute Dog.')
    0.0
    """
    typed_words = split(typed)
    reference_words = split(reference)
    # BEGIN PROBLEM 3
    # list3 = [word in reference_words for word in typed_words]
    accur = 0

    if len(typed_words) == 0:
        return 0.0

    elif len(typed_words) <= len(reference_words):
        typed_len = len(typed_words) 
    else:
        typed_len = len(typed_words) 
        reference_words += [''] * (len(typed_words)-len(reference_words))
    

    for curr_char in range(typed_len):
        if typed_words[curr_char] == reference_words[curr_char]:
            accur += 1 

    return accur / typed_len * 100

    # END PROBLEM 3


def wpm(typed, elapsed):
    """Return the words-per-minute (WPM) of the TYPED string."""
    assert elapsed > 0, 'Elapsed time must be positive'
    # BEGIN PROBLEM 4
    return (len(typed)/5)/(elapsed/60)
    # END PROBLEM 4


def autocorrect(user_word, valid_words, diff_function, limit):
    """Returns the element of VALID_WORDS that has the smallest difference
    from USER_WORD. Instead returns USER_WORD if that difference is greater
    than LIMIT.
    """
    # BEGIN PROBLEM 5
    if user_word in valid_words:
        return user_word
    else:
        endlist = []
        diff_list = []
        for curr_word in valid_words:
            difference = diff_function(user_word, curr_word, limit)
            if difference not in diff_list:
                diff_list += [diff_function(user_word, curr_word, limit)]
                endlist += [(diff_function(user_word, curr_word, limit), curr_word)]

        dict4 = dict(endlist)
        if (min(dict4)) > limit:
            return user_word
        else:
            return dict4[min(dict4)]
    # END PROBLEM 5


def sphinx_swap(start, goal, limit):
    """A diff function for autocorrect that determines how many letters
    in START need to be substituted to create GOAL, then adds the difference in
    their lengths.
    """
    # BEGIN PROBLEM 6
    
    total = 0

    if start == goal:
        return total

    else:
        if start[0] != goal[0]:
            total += 1
            if total > limit:
                return total
            else:
                if len(start) > 1 and len(goal) > 1:
                    return total + sphinx_swap(start[1:], goal[1:], limit-1)
                elif len(start) <= 1 or len(goal) <=1:
                    if len(goal) != len(start):
                        sgdiff = abs(len(goal) - len(start))
                        total += sgdiff
                        return total
                    else:
                        return total
        else:
            if total > limit:
                return total
            else:
                if len(start) > 1 and len(goal) > 1:
                    return total + sphinx_swap(start[1:], goal[1:], limit)
                elif len(start) <= 1 or len(goal) <=1:
                    if len(goal) != len(start):
                        sgdiff = abs(len(goal) - len(start))
                        total += sgdiff
                        return total
                    else:
                        return total         

    # END PROBLEM 6


def feline_fixes(start, goal, limit):
    """A diff function that computes the edit distance from START to GOAL."""
    total = 0

    if start == goal or limit < 0: # Fill in the condition
        # BEGIN
        return total 
        # END

    elif len(start) == 0 or len(goal) == 0: # Feel free to remove or add additional cases
        # BEGIN
        total = abs(len(goal) - len(start))
        return total

    elif goal[0] == start[0]:
        return feline_fixes(start[1:], goal[1:], limit)
        # END

    else:
        total = 1 
        add_diff = total + feline_fixes(goal[0]+start, goal, limit - 1) 
        remove_diff = total + feline_fixes(start[1:], goal, limit - 1) 
        substitute_diff = total + feline_fixes(goal[0] + start[1:], goal, limit - 1) 
        # BEGIN
        return min(add_diff, substitute_diff, remove_diff)
        # END


def final_diff(start, goal, limit):
    """A diff function. If you implement this function, it will be used."""
    assert False, 'Remove this line to use your final_diff function'


###########
# Phase 3 #
###########


def report_progress(typed, prompt, id, send):
    """Send a report of your id and progress so far to the multiplayer server."""
    # BEGIN PROBLEM 8

    list8 = typed + [0] * (len(prompt) - len(typed))
    prog = 0 
    
    for k in range(len(list8)):
        if list8[k] == prompt[k]:
            prog += 1
        else:
            break 


    sendprog = prog / len(prompt)

    senddic = {'id': id, 'progress': sendprog}

    send(senddic), print(sendprog)

    # END PROBLEM 8


def fastest_words_report(times_per_player, words):
    """Return a text description of the fastest words typed by each player."""
    game = time_per_word(times_per_player, words)
    fastest = fastest_words(game)
    report = ''
    for i in range(len(fastest)):
        words = ','.join(fastest[i])
        report += 'Player {} typed these fastest: {}\n'.format(i + 1, words)
    return report


def time_per_word(times_per_player, words):
    """Given timing data, return a game data abstraction, which contains a list
    of words and the amount of time each player took to type each word.

    Arguments:
        times_per_player: A list of lists of timestamps including the time
                          the player started typing, followed by the time
                          the player finished typing each word.
        words: a list of words, in the order they are typed.
    """
    # BEGIN PROBLEM 9

    gtf = []
    gt = []

    for k in times_per_player:

        gt = []

        for i in range(len(k)):
            if i < len(k)-1:
                gt += [k[i+1] - k[i]]
            else:
                break
        gtf += [gt]

    return game(words, gtf)


    # END PROBLEM 9


def fastest_words(game):
    """Return a list of lists of which words each player typed fastest.

    Arguments:
        game: a game data abstraction as returned by time_per_word.
    Returns:
        a list of lists containing which words each player typed fastest
    """
    players = range(len(all_times(game)))  # An index for each player
    words = range(len(all_words(game)))    # An index for each word
    # BEGIN PROBLEM 10
    
    ps = all_times(game)
    ws = all_words(game)

    fastest_words_list = [[] for x in players]
    for word in words:
        min_time = 10000
        for player in players:
            if ps[player][word] < min_time:
                min_player = player
                min_time = ps[player][word]

        fastest_words_list[min_player].append(ws[word])

    return fastest_words_list

    # END PROBLEM 10


def game(words, times):
    """A data abstraction containing all words typed and their times."""
    assert all([type(w) == str for w in words]), 'words should be a list of strings'
    assert all([type(t) == list for t in times]), 'times should be a list of lists'
    assert all([isinstance(i, (int, float)) for t in times for i in t]), 'times lists should contain numbers'
    assert all([len(t) == len(words) for t in times]), 'There should be one word per time.'
    return [words, times]


def word_at(game, word_index):
    """A selector function that gets the word with index word_index"""
    assert 0 <= word_index < len(game[0]), "word_index out of range of words"
    return game[0][word_index]


def all_words(game):
    """A selector function for all the words in the game"""
    return game[0]


def all_times(game):
    """A selector function for all typing times for all players"""
    return game[1]


def time(game, player_num, word_index):
    """A selector function for the time it took player_num to type the word at word_index"""
    assert word_index < len(game[0]), "word_index out of range of words"
    assert player_num < len(game[1]), "player_num out of range of players"
    return game[1][player_num][word_index]


def game_string(game):
    """A helper function that takes in a game object and returns a string representation of it"""
    return "game(%s, %s)" % (game[0], game[1])

enable_multiplayer = False  # Change to True when you


##########################
# Command Line Interface #
##########################


def run_typing_test(topics):
    """Measure typing speed and accuracy on the command line."""
    paragraphs = lines_from_file('data/sample_paragraphs.txt')
    select = lambda p: True
    if topics:
        select = about(topics)
    i = 0
    while True:
        reference = choose(paragraphs, select, i)
        if not reference:
            print('No more paragraphs about', topics, 'are available.')
            return
        print('Type the following paragraph and then press enter/return.')
        print('If you only type part of it, you will be scored only on that part.\n')
        print(reference)
        print()

        start = datetime.now()
        typed = input()
        if not typed:
            print('Goodbye.')
            return
        print()

        elapsed = (datetime.now() - start).total_seconds()
        print("Nice work!")
        print('Words per minute:', wpm(typed, elapsed))
        print('Accuracy:        ', accuracy(typed, reference))

        print('\nPress enter/return for the next paragraph or type q to quit.')
        if input().strip() == 'q':
            return
        i += 1


@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions."""
    import argparse
    parser = argparse.ArgumentParser(description="Typing Test")
    parser.add_argument('topic', help="Topic word", nargs='*')
    parser.add_argument('-t', help="Run typing test", action='store_true')

    args = parser.parse_args()
    if args.t:
        run_typing_test(args.topic)