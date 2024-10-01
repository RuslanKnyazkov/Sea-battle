from App.config import player_map
import json

class Player:
    def __init__(self, name):
        self._name = name
        self.step = 1
        self.process = {'User': self._name,
                        'Step': []}

    def record_game(self):
        with open('..\\save' + f'{self._name}_save.json', mode='w') as record_file:
            #self.process['Step'].append(dict(step = self.step, column = self.column, row =self.row))
            json.dump(self.process, record_file, indent=4)
