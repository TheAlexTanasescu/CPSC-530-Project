import pygame
from settings import *
from graphics import *

class PasswordGen:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()

        self.buttons = [
            Button(110, 50, YELLOW),
            Button(330, 50, BLUE),
            Button(110, 270, RED),
            Button(330, 270, GREEN),
        ]

    def new(self):
        pass

    def run(self):
        self.playing = True
        while(self.playing):
            self.clock.tick(FPS)
            self.events()
            self.draw()
            self.update()

    def update(self):
        pass

    def draw(self):
        self.screen.fill(BGCOLOR)
        for button in self.buttons:
            button.draw(self.screen)
        pygame.display.update()
    def events(self):
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                pygame.quit()
                quit(0)

gen = PasswordGen()
while True:
    gen.new()
    gen.run()



