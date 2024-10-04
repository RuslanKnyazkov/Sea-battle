from typing import Callable
from random import randint, choice
from App.config import player_map, CHARACTERS


class Handler:
    """
    ppp
    """

    automatic_step = False

    def shoot(self):
        return choice(CHARACTERS), randint(1, 10)

    def block_handler(self, funk: Callable):
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
