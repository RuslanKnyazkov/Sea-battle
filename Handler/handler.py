from typing import Callable
from random import randint, choice
from App.config import player_map, CHARACTERS , SHIPS


class Handler:
    """
    ppp
    """
    def __init__(self):

        self.automatic_step = False



    def shoot(self):
        return choice(CHARACTERS), randint(1, 10)

    def block_user_step(self, funk: Callable):
        """
        The decorator blocks the repeated call of the player's function until another function is worked out.
        :param funk: Callable object default using in class Cell.refactor_value_cell
        :return: None
        """
        def wrapper(*args, **kwargs):
            if self.automatic_step:
                ...
            else:
                funk(*args, **kwargs)
                self.automatic_step = True
        return wrapper

    def set_position_ships(self, funk: Callable):
        def wrapper(*args, **kwargs):
            ...

