# import the pygame module


import pygame, sys, os
from classes import Ship, Line 
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




pygame.init()
win=pygame.display.set_mode((500,500))
#raywin=pygame.Surface((500, 500), pygame.SRCALPHA)
#raywin.fill((0, 0, 0, 128))
x=50
y=50

vel=1
width =60
height=50
run= True
spaceship = Ship(x,y,20,20,(255,0,0))

while run is True: 
    spaceship.drawShip(win)
    gameline= Line(x,20,400,[225,0,0])
    gameline.drawLine(win)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run= False
    key=pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
       spaceship.x-=vel
    if key[pygame.K_RIGHT]:
        spaceship.x+=vel
    if key [pygame.K_DOWN]:
        spaceship.y+=vel
    if key [pygame.K_UP]:
        spaceship.y-=vel
  
    
   
    FPS= 60
    clock= pygame.time.Clock()
    pygame.display.update()
    win.fill((0,0,0))
    if x>=499:

        x=2
    elif x<=0:
        x=499
    elif y<=0:
        y=499
    elif y>499:

        y=1
        
pygame.quit()
