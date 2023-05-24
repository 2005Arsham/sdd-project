# import the pygame module
import random 
import math
import pygame, sys, os
import classes

def colidet(ship,object):
    colisionline= False
    colisionbub= False
    colisionend=False
    if ship.x==object.x+ship.width+ ship.y == object.y:
        colision= True
    return colision
def movement(Ship):
#wraparound mechanic, up and down movement, front to back movement 

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run= False
        key=pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            x-=vel
        if key[pygame.K_RIGHT]:
            x+=vel
        if key [pygame.K_DOWN]:
            y+=vel
        if key [pygame.K_UP]:
            y-=vel  
    #border wrap around mechanic 
        if Ship.x>=499 :
            Ship.x=2
        elif Ship.x<=0 :
            Ship.x=499
        elif Ship.y<=0 :
            Ship.y=499
        elif Ship.y>499 :
            Ship.y=0
        
    return Ship
def  RANDOMIZE_BUB(bubble):
        a =random.randint(1,600) 
        b =random.randint(1,600)
        bubble[x]=a
        bubble[y]=b
        
        return bubble
def colision (Ship, object):
#Ccollison detection Ship with line, Ship with colour bubbles,change colours, account for width and height
    colisionline= False
    colisionbub= False
    colisionend=False
    if Ship.x==object.x+Ship.width + Ship.y == object.y:
        colision= True
    
    return colision
def COLLISION_RESULT(bubble,colisionend,line): #what happens when colision is detected
    if colision(Ship, bubble)== True:
        Ship.colour=bubble.colour
    elif colisionend == True :
        run=False
    elif colision(Ship, line) == True :
        if Ship.colour==line.colour:
            line.pop(0)
        else: 
            run=False






right=pygame.image.load('right.png.png')
left=pygame.image.load('left.png.png')
idle=pygame.image.load('idle.png.png')
jump=pygame.image.load('jump.png.png')

class Ship():
    def __init__(self, x,y,width,height, colour):
        #self.image= pygame.image.load('right.png.png')
        self.image= idle
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.colour=colour
        self.rect=pygame.Rect(x,y,32,32)
        self.xspeed=0
        self.yspeed=0
        self.left_pressed= False
        self.right_pressed= False
        self.space_pressed= False
        
        self.speed=4
        self.upspeed=-10
        self.gravity=2
    def drawShip(self, win):
        image = pygame.transform.scale(self.image, (160, 160))
        image_rect = image.get_rect()
        image_rect.center = (self.x, self.y)
        image_rect.top = self.y - self.height
        win.blit(image, image_rect)
        
    def update(self):
        self.xspeed=0
        self.yspeed=0
        if  self.left_pressed and not self.right_pressed:
            self.xspeed = -self.speed
            self.image=left
            self.y-=10
            image = pygame.transform.scale(self.image, (250, 250))
        if  self.right_pressed and not self.left_pressed:
            self.xspeed = self.speed
            self.image= right
        if  self.space_pressed:
            self.yspeed = self.upspeed
            self.image= jump
            
        self.x+=self.xspeed
        self.y+=self.yspeed
        if self.y <= 865: # bottom end of screen
            
            self.gravity += 0.105  # change gravity strength
            self.y += self.gravity
            
        else:
            self.gravity =0
            self.y = 865
        
            #self.image= pygame.image.load('idle.png.png') 
        self.rect=pygame.Rect(self.x,self.y,32,32)


class Line():
    def __init__(self, x, width, height, colour):
        self.x = x
        self.width = width
        self.height = height 
        self.colour = colour
        self.end_pos = x + 10  # initialize end_pos with x+300
    def drawLine(self, win):
         pygame.draw.line(win, self.colour, (self.x, self.height), (self.end_pos, self.height), self.width)

class Enemy():
    def __init__(self, x,y,width,height, colour):
        #self.image= pygame.image.load('right.png.png')
        self.image= pygame.image.load('calm.png.png')
        self.x=x
        self.y=y
    
        self.width=width
        self.height=height
        self.colour=colour
        self.rect=pygame.Rect(x,y,32,32)
        self.xspeed=0
        self.yspeed=0
        self.left_pressed= False
        self.right_pressed= False
        self.space_pressed= False
        self.distance_above_player = 100 
        self.speed=1
        self.upspeed=-10
        self.gravity=2
       
    def drawenemy(self, win):
        image = pygame.transform.scale(self.image, (160, 160))
        image_rect = image.get_rect()
        image_rect.center = (self.x, self.y)
        image_rect.top = self.y - self.height
        win.blit(image, image_rect)
    def updateenemy(self,win):
        
        d= math.sqrt( ((enemy.x-spaceship.x)**2)+((enemy.y-spaceship.y)**2) )
        
        try:
            x = (spaceship.x - self.rect.x) / d
            y = ((spaceship.y - self.distance_above_player)  - self.rect.y) / d
        except ZeroDivisionError: 
            return False
         
        self.x += x * self.speed
        self.y += y * self.speed
        self.rect = pygame.Rect(self.x, self.y, 32, 32)





















pygame.init()

agro=pygame.image.load('agro.png.png')
calm=pygame.image.load('calm.png.png')

font = pygame.font.Font(None, 24)
def screen_info():
    screen_info = pygame.display.Info()
    screen_width = screen_info.current_w
    screen_height = screen_info.current_h
    return screen_width, screen_height
screen_width, screen_height = screen_info()
#classes.setEnvironment(screen_width,screen_height)
win=pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
#raywin=pygame.Surface((500, 500), pygame.SRCALPHA)
#raywin.fill((0, 0, 0, 128))
#fg= pygame.image.load("foreground.png")
#bg = pygame.image.load("background.webp")
#fg = pygame.transform.scale(fg, (screen_width,screen_height *0.04))
x=50
y=50


run= True
spaceship = Ship(x,y,20,20,(250,120,220))
#enemy = Enemy(x, y, 20, 20, (120, 150, 225))
enemies=[]
for i in range(5):
    x=random.randint(0, screen_width)
    y=random.randint(0, screen_height)
    enemy = Enemy(x, y, 20, 20, (120, 150, 225))
    enemies.append(enemy)

FPS= 60
clock= pygame.time.Clock()
while run is True: 
    #win.blit(fg, (0,490))
    clock.tick(FPS)
    keys = pygame.key.get_pressed()
    d= math.sqrt( ((enemy.x-spaceship.x)**2)+((enemy.y-spaceship.y)**2) )
    print(d)
    distance_text = font.render("Distance: {:.2f}".format(d), True, (255, 255, 255)) 
    if d<=105:
        enemy.image= agro
    else:
        enemy.image= calm
        
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run= False
        if event.type== pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                spaceship.left_pressed=True
            if event.key==pygame.K_RIGHT:
                spaceship.right_pressed=True
            if event.key==pygame.K_SPACE:
                spaceship.space_pressed=True
        if event.type== pygame.KEYUP:
            if event.key==pygame.K_LEFT:
                spaceship.left_pressed=False
            if event.key==pygame.K_RIGHT:
                spaceship.right_pressed=False  
            if event.key==pygame.K_SPACE:
                spaceship.image= pygame.image.load('idle.png.png')
               
                spaceship.space_pressed=False
        
       
    pygame.display.update()
    win.fill((220,220,220))
    spaceship.drawShip(win)
    spaceship.update()
    for enemy in enemies:
        enemy.drawenemy(win)
        enemy.updateenemy(win)
    win.blit(distance_text, (200,500))
    #gameline.drawLine(win)
    # pygame.display.update()
   
    if spaceship.x >= screen_width:
        spaceship.x = 0
    elif spaceship.x <= 0:
        spaceship.x = screen_width - 1
    #elif spaceship.y <= 0:
        #spaceship.y = screen_height - 1
    elif spaceship.y >= screen_height:
        spaceship.y = 0
pygame.quit()
