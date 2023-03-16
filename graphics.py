import pygame
from settings import *


class Button:
    def __init__(self, x, y, colour):
        self.x, self.y = x,y
        self.colour = colour
    
    def draw(self, screen):
        pygame.draw.rect(screen, self.colour, (self.x, self.y, BUTTONSIZE, BUTTONSIZE))
    
    def clicked(self, mouseX, mouseY):
        return self.x <= mouseX <= self.x + BUTTONSIZE and self.y <= mouseY <= self.y + BUTTONSIZE