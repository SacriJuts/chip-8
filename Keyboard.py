from pygame.locals import *

class Keyboard:

    def __init__(self):
        self.map = [
            [K_0, '0'],
            [K_1, '1'],
            [K_2, '2'],
            [K_3, '3'],
            [K_4, '4'],
            [K_5, '5'],
            [K_6, '6'],
            [K_7, '7'],
            [K_8, '8'],
            [K_9, '9'],
            [K_a, 'a'],
            [K_b, 'b'],
            [K_c, 'c'],
            [K_d, 'd'],
            [K_e, 'e'],
            [K_f, 'f'],
        ]

    # maps an input of the keyboard to the virtual keyboard (1 to 9, a to f)
    def map(self, pygameConstChar, softChar):
        chars = [self.map[i][1] for i in range(16)]
        consts = [self.map[i][0] for i in range(16)]
