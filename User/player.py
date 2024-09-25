from App.config import maps
class Player:
    def __init__(self, name, colunm, row):
        self.name = name
        self.col = colunm
        self.r = int(row)
        self.choose_shoot()

    def choose_shoot(self):
        maps[self.col][self.r] = 'x'
        print(maps)


p = Player('rus', 'A', 3)
