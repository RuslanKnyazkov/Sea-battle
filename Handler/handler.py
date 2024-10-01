from typing import Callable
from random import randint, choice
from App.config import player_map, CHARACTERS


class Handler:

    automatic_step = False

    def shoot(self):
        return choice(CHARACTERS), randint(1,10)

    def block_handler(self, funk):
        """
        Decorator for block clicked mouse before выстрела бота.
        :param funk:
        :return:
        """
        def wrapper(*args, **kwargs):
            if self.automatic_step:
                ...
            else:
                funk(*args, **kwargs)
        return wrapper
