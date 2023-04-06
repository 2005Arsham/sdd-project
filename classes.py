import pygame
class Ship():
    def __init__(self, x,y,width,height, colour):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.colour=colour
        
      
        
    def drawShip(self, win):
        pygame.draw.rect(win,self.colour, (self.x, self.y, self.width, self.height))

class Line():
    def __init__(self, x, width, height, colour):
        self.x = x
        self.width = width
        self.height = height 
        self.colour = colour
        self.end_pos = x + 10  # initialize end_pos with x+300
    def drawLine(self, win):
         pygame.draw.line(win, self.colour, (self.x, self.height), (self.end_pos, self.height), self.width)