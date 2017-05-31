import pygame, sys
from pygame.locals import *

HeightPixels = 32
WidthPixels = 64

class Window :

    def __init__(self, scale=10, bcol=(0, 0, 0), col=(255, 255, 255)):
        self.PixelScale = scale
        self.Width = scale * WidthPixels
        self.Height = scale * HeightPixels
        self.BackgroundColor = bcol
        self.Color = col
        self.Pixels = [[0 for i in range(HeightPixels)] for j in range(WidthPixels)]
        self.ShowedPixels = [[0 for i in range(HeightPixels)] for j in range(WidthPixels)]
        self.Surface = pygame.display.set_mode((self.Width, self.Height))

    def show(self):
        for i in range(WidthPixels):
            for j in range(HeightPixels):
                if self.ShowedPixels[i][j]:
                    pygame.draw.rect(self.Surface, self.Color, (i*self.PixelScale, j*self.PixelScale, self.PixelScale, self.PixelScale))
        pygame.display.update()

    def update(self):
        self.ShowedPixels = self.Pixels



pygame.init()
myWindow = Window()

myWindow.show()

tab = []

for i in range(64):
    bweh = []
    for j in range(32):
        if (i+j)%2 == 0:
            bweh.append(True)
        else:
            bweh.append(False)
    tab.append(bweh)

myWindow.Pixels = tab

myWindow.update()
myWindow.show()

progress = True

while progress:
    for event in pygame.event.get():
        if event.type == QUIT:
            progress = False

pygame.quit()
