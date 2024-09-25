from typing import Any

from customtkinter import (CTk, CTkFrame, CTkButton,
                           CTkLabel, CTkEntry)
from User.player import Player
from config import  maps


class Root(CTk):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.frame = GameFrame(self)
        self.frame.pack(expand = True)



class GameFrame(CTkFrame):
    def __init__(self, master: Any, **kwargs):
        super().__init__(master, **kwargs)

        self.t = Area(self)
        self.t.create_area()
        self.t.grid( column = 1, row = 1, padx = 20)

        self.g = Area(self)
        self.g.create_area()
        self.g.grid( column = 2, row = 1, padx = 20)

        self.entry_column = EntryPoints(self, holder_text='Please choice column')
        self.entry_column.grid(column = 1, row = 2, padx = 20)

        self.entry_row = EntryPoints(self, holder_text='Please choice row')
        self.entry_row.grid(column = 1, row = 3, padx = 20)

        self.btn_confirm = CTkButton(self, text='Confirm', command= self.test_foo)
        self.btn_confirm.grid(column = 2, row = 2)

    def test_foo(self):
        #Player('Ruslan',self.entry_column.get(), int(self.entry_row.get()) - 1)
        maps[self.entry_column.get()][int(self.entry_row.get())] = 'x'
        self.update_area()

    def update_area(self):
        if self.t is not None:
            self.t.destroy()
        self.t = Area(self)
        self.t.grid( column = 1, row = 1, padx = 20)


class Area(CTkFrame):
    def __init__(self, master: Any, **kwargs):
        super().__init__(master, **kwargs)

        for _ in range(10): self.columnconfigure(index=_, weight=1)
        for _ in range(10): self.rowconfigure(index=_, weight=1)
        self.create_area()

    def create_area(self, user: bool = False, ai: bool = False,
                    map: dict = maps):

        for column in enumerate(map.keys()):
            for row in range(len(maps[column[1]])):
                title = column[1] if row == 0 else ""
                Point(self, column=title, row=maps[column[1]][row]).grid(column=column[0],
                row=row, padx=1, pady=1)


class Point(CTkFrame):
    def __init__(self, master: Any, column: str = "",
                 row: str | int = None,):
        super().__init__(master)

        self.column = column
        self.row = row

        self.test = CTkLabel(self, text=self.column,fg_color= 'blue' if self.row != 'x' else 'red',
                 height=25, width=25).pack()



class EntryPoints(CTkEntry):
    def __init__(self, master, holder_text):
        super().__init__(master, placeholder_text=holder_text)


if __name__ == '__main__':
    root = Root()
    root.geometry('700x700+0+0')
    root.mainloop()
