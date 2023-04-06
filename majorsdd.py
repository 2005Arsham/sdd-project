# import the pygame module
from classes import ship 
import random
import pygame, sys, os
pygame.init()
def colidet(ship,object):
    colisionline= False
    colisionbub= False
    colisionend=False
    if ship.x==object.x+ship.width+ ship.y == object.y:
        colision= True
    return colision
def movement():
#wraparound mechanic, up and down movement, front to back movement 
    vel=1
    run= True   
    while run is True: 
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
        if ship.x>=499 :
            ship.x=2
        elif ship.x<=0 :
            ship.x=499
        elif ship.y<=0 :
            ship.y=499
        elif ship.y>499 :
            ship.y=0
        
    return ship
def  RANDOMIZE_BUB(bubble):
        a =random.randint(1,600) 
        b =random.randint(1,600)
        bubble[x]=a
        bubble[y]=b
        
        return bubble
def colision (ship, object):
#Ccollison detection ship with line, ship with colour bubbles,change colours, account for width and height
    colisionline= False
    colisionbub= False
    colisionend=False
    if ship.x==object.x+ship.width + ship.y == object.y:
        colision= True
    
    return colision
def COLLISION_RESULT(bubble,colisionend,line): #what happens when colision is detected
    if colision(ship, bubble)== True:
        ship.colour=bubble.colour
    elif colisionend == True :
        run=False
    elif colision(ship, line) == True :
        if ship.colour==line.colour:
            linearray.pop(0)
        else: 
            run=False

win=pygame.display.set_mode((500,500))
x=50
y=50
vel=1
width =60
height=50

 spaceship = Ship(x,y,20,20,(255,0,0))
spaceship.drawShip(win)
    gameline= Line(x,20,400,[225,0,0])
    gameline.drawLine(win)
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
