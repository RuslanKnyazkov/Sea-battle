from typing import Any
from customtkinter import CTkFrame, CTkLabel
from App.config import ai_map, player_map
from Handler.handler import Handler

hand = Handler()
class Cell(CTkFrame):
    def __init__(self, master: Any, view, column: str | int,
                 unique_id: int, row: str | int):
        super().__init__(master)

        self.column = column
        self.row = row
        self.view = view
        self.unique = unique_id

        self.color = CTkLabel(self, text=self.row - 1 if self.column == '0' else self.view if self.row == 1 else '',
                              fg_color='blue',
                              height=25, width=25)
        self.color.pack()

    def set_color(self):
        """
        Setting color cell.
        """
        if self.row == 'x':
            self.color.configure(fg_color='red', text='X')
        elif self.row != 'x' and self.row != 1 and self.column != '0':
            self.color.configure(fg_color='white', text='O')


    def refactor_value_cell(self, event):
        """
        Change values cell on symbol 'o'.
        """
        raise NotImplemented


class PlayerCell(Cell):
    def __init__(self, master: Any, view,
                 column: str | int,
                 unique_id: int,
                 row: str | int):
        super().__init__(master, view, column, unique_id, row)

        self.color.bind('<Button-1>', command=lambda event: self.refactor_value_cell(event))

    @hand.set_position_ships
    def refactor_value_cell(self, event):
        player_map[self.column][self.unique] = 'x'
        self.row = 'x'
        self.set_color()


class AiCell(Cell):
    def __init__(self, master: Any,
                 view, column: str | int,
                 unique_id: int,
                 row: str | int):
        super().__init__(master, view, column, unique_id, row)

        self.color.bind('<Button-1>', command=lambda event: self.refactor_value_cell(event))

    @hand.block_user_step
    def refactor_value_cell(self, event):
        self.set_color()
        ai_map[self.column][self.unique] = 'o'

