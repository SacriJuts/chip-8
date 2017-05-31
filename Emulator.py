import Display
import pygame, sys
from pygame.locals import *

display = Display.Window()

RAM = [0]*4096                  # RAM
V = [0]*16                      # registers
I = 0                           # special register
PC = 0                          # PC = Program Counter | addresse de l'instruction à executer
SP = 0                          # SP = Stack Pointer | redirige vers le plus haut niveau du stack
Stack = [0]*16                  # Stack, 16 valeurs de 16 bits => max 65532 valeurs

def cls():
    display.clear()

progress = True

while progress:
    for event in pygame.event.get():
        if event.type == QUIT:
            progress = False

pygame.quit()
