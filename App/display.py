from typing import Any
from customtkinter import (CTk, CTkFrame, CTkButton)
from game_area import UserArea, AiArea
from User.player import Player

class MainRoot(CTk):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.test = GameFrame(self)
        self.test.pack(expand=True, fill = 'x')


class GameFrame(CTkFrame):
    def __init__(self, master: Any, **kwargs):
        super().__init__(master, **kwargs)

        for i in range(2): self.columnconfigure(index=i, weight=i)


        self.__player_area = UserArea(self)
        self.__player_area.pack(side = 'left', padx = 30, expand = True, pady = 30)
        self.__player_area.create_area()

        self.__ai_area = AiArea(self)
        self.__ai_area.pack(side = 'right', padx = 30, expand = True, pady = 30)
        self.__ai_area.create_area()


if __name__ == '__main__':
    root = MainRoot()
    root.geometry('800x800+0+0')
    root.mainloop()
