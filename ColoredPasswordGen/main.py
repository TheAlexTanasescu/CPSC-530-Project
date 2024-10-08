import pygame
from settings import *
from graphics import *


pygame.init()
class PasswordGen:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()

        self.buttons = [
            Button(150, 50, YELLOW),
            Button(260, 50, BLUE),
            Button(370, 50, ORANGE),
            Button(150, 160, PURPLE),
            Button(260, 160, PINK),
            Button(370, 160, GOLD),
            Button(150, 270, RED),
            Button(260, 270, GREEN),
            Button(370, 270, BROWN),
            Button(260, 490, WHITE)
            
        ]
        self.colorLookup = {"YELLOW": (255, 255, 0), "RED": (255, 0, 0), "GREEN": (0, 255, 0), "BLUE": (0, 0, 255), "ORANGE": (252, 102, 0), "PURPLE" : (160, 32, 240), "PINK" : (255,190,200), "GOLD" : (255, 215, 0), "BROWN" : (125, 56, 2), "WHITE": (255, 255, 255)}
       
        self.pattern = []
        self.currentStep = 0

    def get_keys_from_value(self, d, val):
        return [k for k, v in d.items() if v == val]       
        

    def run(self):
        self.playing = True
        while(self.playing):
            #self.clock.tick(FPS)
            self.clicked_button = None
            self.events()
            
            self.draw()
            self.update()
   

    def update(self):
        
    
        #if(self.clicked_button):
        if (self.get_keys_from_value(self.colorLookup, self.clicked_button) == ["RED"]) or (self.get_keys_from_value(self.colorLookup, self.clicked_button) == ["GREEN"]) or (self.get_keys_from_value(self.colorLookup, self.clicked_button) == ["YELLOW"]) or (self.get_keys_from_value(self.colorLookup, self.clicked_button) == ["BLUE"]) or (self.get_keys_from_value(self.colorLookup, self.clicked_button) == ["ORANGE"]) or (self.get_keys_from_value(self.colorLookup, self.clicked_button) == ["PURPLE"]) or (self.get_keys_from_value(self.colorLookup, self.clicked_button) == ["PINK"]) or (self.get_keys_from_value(self.colorLookup, self.clicked_button) == ["GOLD"]) or (self.get_keys_from_value(self.colorLookup, self.clicked_button) == ["BROWN"]):  
            self.pattern.append([k for k, v in self.colorLookup.items() if v == self.clicked_button])
            self.currentStep += 1
       
        elif(self.get_keys_from_value(self.colorLookup, self.clicked_button) == ["WHITE"]):    
            password = (self.pattern, str(len(self.pattern)))
            pwdStr = ""
            for item in password:
                pwdStr += str(item)            
            with open("MattColorPasswords.txt", "a") as file:
                file.write(pwdStr)
                file.write("\n")
            self.pattern = []
            self.currentStep = 0
            self.run()
    def draw(self):
        self.screen.fill(BGCOLOR)
        for button in self.buttons[:-1]:
            button.draw(self.screen)
        

        self.buttons[-1].draw_done(self.screen)
        myfont = pygame.font.SysFont('Comic Sans MS', 20)
        self.text = myfont.render('Done', False, (0, 0, 0))
        self.screen.blit(self.text, (290, 500))
        
        pygame.display.update()
    def events(self):
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                pygame.quit()
                quit(0)

            if (event.type == pygame.MOUSEBUTTONDOWN):
                mouseX, mouseY = pygame.mouse.get_pos()
                for button in self.buttons:
                    if (button.clicked(mouseX, mouseY)):
                        self.clicked_button = button.colour

gen = PasswordGen()
while True:
    gen.run()





