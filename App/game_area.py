from customtkinter import CTkFrame, CTkLabel
from typing import Any
from config import player_map, ai_map, winner
from Handler.handler import Handler

handler = Handler()

class Point(CTkFrame):
    def __init__(self, master: Any, view, column: str,
                 unique_id: int, row: str | int):
        super().__init__(master)

        self.column = column
        self.row = row
        self.view = view
        self.unique = unique_id

        self.color = CTkLabel(self, text=self.view if self.row == 1 else '', fg_color='blue',
                              height=25, width=25)
        self.color.pack()
        self.color.bind('<Button-1>', command=lambda event: self.refactor_value_cell(event))

    def set_color(self):
        """
        After pushing button on mouse start processing check совпадения символов.
        :param event: Mouse button
        """
        if self.row == 'x':
            self.color.configure(fg_color='red', text='X')
        elif self.row != 'x' and self.row != 1:
            self.color.configure(fg_color='white', text='O')

    @handler.block_handler
    def refactor_value_cell(self, event):
        """
        Change values cell on symbol 'o' .
        :param obj: Instance Point
        :param array: Map
        :return: None
        """
        if str(self.__getattribute__('master')) == '.!gameframe.!aiarea':
            self.set_color()
            ai_map[self.column][self.unique] = 'o'
        handler.automatic_step = True



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
    def __init__(self, master: Any, **kwargs):
        super().__init__(master, **kwargs)

        self.label = CTkLabel(self, text='Player').grid(columnspan=11)
        self.automatick_check()


    def create_area(self):
        for column in enumerate(player_map.keys()):
            for row in range(len(player_map[column[1]])):
                title = column[1]
                self.point_collect[f'{column[1]}:{row}'] = Point(self, view=title,
                                                                 column=column[1], row=player_map[column[1]][row],
                                                                 unique_id=row)
                self.point_collect[f'{column[1]}:{row}'].grid(column=column[0] + 1, row=row + 1, padx=1, pady=1)

    def automatick_check(self):
        if handler.automatic_step is False:
            print('True')
        else:
            random_cell = handler.shoot()
            self.point_collect[f'{random_cell[0]}:{random_cell[1]}'].set_color()
            handler.automatic_step = False
        self.after(2000, self.automatick_check)



class AiArea(Area):
    def __init__(self, master: Any, **kwargs):
        super().__init__(master, **kwargs)

        self.label = CTkLabel(self, text='AI').grid(columnspan=11)

    def create_area(self):
        for column in enumerate(ai_map.keys()):
            for row in range(len(ai_map[column[1]])):

                if column[1] == '':
                    title = row
                else:
                    title = column[1] if row == 0 else ""

                self.point_collect[f'{column[1]}:{row}'] = Point(self, view=title,
                                                                 column=column[1], row=ai_map[column[1]][row],
                                                                 unique_id=row)
                self.point_collect[f'{column[1]}:{row}'].grid(column=column[0] + 1, row=row + 1, padx=1, pady=1)
