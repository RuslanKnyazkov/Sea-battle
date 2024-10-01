import time
from random import choice, randint

player_map = {
    '0': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
    'A': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
    'B': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
    'C': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
    'D': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
    'E': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
    'F': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
    'G': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
    'H': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
    'I': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
    'J': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
}

ai_map = {
    '0': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
    'A': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
    'B': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
    'C': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
    'D': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
    'E': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
    'F': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
    'G': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
    'H': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
    'I': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
    'J': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
}

SHIPS = [['x', 'x', 'x', 'x', 'x'],
         ['x', 'x', 'x'],
         ['x', 'x', 'x'],
         ['x', 'x'],
         ['x'],
         ['x'],
         ['x']]

CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']


def test_insert_the_maps():
    """
    Automatic insert into Ai maps ship on vertical positions.
    :return: None
    """

    ship_number = 0
    while len(SHIPS) != ship_number:
        try:
            random_number = randint(1, 11)
            for ship in SHIPS:
                random_field = choice(CHARACTERS)
                for j in range(len(ship)):
                    ai_map[random_field][random_number + j] = 'x'
                ship_number += 1
        finally:
            continue


def winner():
    for value in ai_map.values():
        if 'x' not in value:
            ...
        else:
            return False
    return True
