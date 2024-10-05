from cell import PlayerCell, AiCell
from random import randint, choice
from customtkinter import CTkFrame, CTkLabel
from typing import Any
from config import player_map, ai_map, SHIPS, CHARACTERS

class Area(CTkFrame):
    def __init__(self, master: Any, **kwargs):
        super().__init__(master, **kwargs)

        for _ in range(10): self.columnconfigure(index=_, weight=1)
        for _ in range(10): self.rowconfigure(index=_, weight=1)

        self.point_collect = {}

    def create_area(self):
        """ Function for override subclass"""
        return NotImplemented


class UserArea(Area):
    def __init__(self, master: Any, user: object ,  **kwargs):
        super().__init__(master, **kwargs)

        self.label = CTkLabel(self, text=user.name).grid(columnspan=11)

    def create_area(self):
        for column in enumerate(player_map.keys()):
            for row in range(len(player_map[column[1]])):
                title = column[1]
                self.point_collect[f'{column[1]}:{row}'] = PlayerCell(self, view=title,
                                                                      column=column[1],
                                                                      row=player_map[column[1]][row],
                                                                      unique_id=row)
                self.point_collect[f'{column[1]}:{row}'].grid(column=column[0] + 1, row=row + 1, padx=1, pady=1)
    #     self.automatic_check()
    #
    # def automatic_check(self):
    #     """
    #     Checks if the player's move has been completed
    #     :return: None
    #     """
    #     if handler.automatic_step is False:
    #         ...
    #     else:
    #         random_column , random_row = handler.shoot()
    #         self.point_collect[f'{random_column}:{random_row}'].set_color()
    #         handler.automatic_step = False
    #     self.after(2000, self.automatic_check)


class AiArea(Area):
    def __init__(self, master: Any, **kwargs):
        super().__init__(master, **kwargs)

        self.label = CTkLabel(self, text='AI').grid(columnspan=11)

    def create_area(self):
        self.auto_plases_ship()
        for column in enumerate(ai_map.keys()):
            for row in range(len(ai_map[column[1]])):
                title = column[1] if row == 0 else ""
                self.point_collect[f'{column[1]}:{row}'] = AiCell(self, view=title,
                                                                  column=column[1], row=ai_map[column[1]][row],
                                                                  unique_id=row)
                self.point_collect[f'{column[1]}:{row}'].grid(column=column[0] + 1, row=row + 1, padx=1, pady=1)

    def auto_plases_ship(self):
        """
        Automatic insert into Ai maps ship on vertical positions.
        :return: None
        """

        ship_number = 0

        while len(SHIPS) != ship_number:
            try:
                for ship in SHIPS:
                    random_number = randint(1, 11)
                    random_field = choice(CHARACTERS)
                    for j in range(len(ship)):
                        ai_map[random_field][random_number + j] = 'x'
                    ship_number += 1
            finally:
                continue
