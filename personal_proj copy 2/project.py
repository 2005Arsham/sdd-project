
import csv 
import random 
import math
import pygame, sys, os
def start_surf():
    start=True
    while  start:

                            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                start = False
        overlay_surface = pygame.Surface((800, 770))  
        overlay_surface.set_alpha(225)  
        overlay_surface.fill((0, 0, 0)) 
        win.blit(overlay_surface, (0, 0)) 

        font = pygame.font.Font(None, 36)
        text = font.render("press any key to start", True, (255, 255, 255)) 
        text_rect = text.get_rect(center=(400, 385)) 
        win.blit(text, text_rect)
        pygame.display.flip()
            
def winning():
        overlay_surface = pygame.Surface((800, 770))  
        overlay_surface.set_alpha(225)  
        overlay_surface.fill((0, 0, 0)) 
        win.blit(overlay_surface, (0, 0)) 

        font = pygame.font.Font(None, 36)
        text = font.render("You won!", True, (255, 255, 255)) 
        text_rect = text.get_rect(center=(400, 385)) 
        win.blit(text, text_rect)
def losing():
        overlay_surface = pygame.Surface((800, 770))  
        overlay_surface.set_alpha(225)  
        overlay_surface.fill((0, 0, 0)) 
        win.blit(overlay_surface, (0, 0)) 

        font = pygame.font.Font(None, 36)
        text = font.render("You lost!", True, (255, 255, 255)) 
        text_rect = text.get_rect(center=(400, 385)) 
        win.blit(text, text_rect)

def collisions (spaceship,tiles):
    collide=[]
    for tile in tiles:
        if spaceship.rect.colliderect(tile):
            collide.append(tile)
            return collide
class Ship():
    def __init__(self, x,y,width,height, colour):
        #self.image= pygame.image.load('right.png.png')
       
        self.allow_vertical_movement=True
        self.image= idle
        self.x=int(x)
        self.y=int(y)
        self.width=width
        self.height=height
        self.colour=colour
        self.rect=pygame.Rect(x,y,32,32)
        self.xspeed=0
        self.yspeed=0
        self.left_pressed= False
        self.right_pressed= False
        self.space_pressed= False
        offset_x = self.x - 1000
        offset_y = self.y + 10
        offset_width = self.width - 300
        offset_height = self.height +1
        self.offset_rect = pygame.Rect(offset_x, offset_y, offset_width, offset_height)
        self.speed=4
        self.upspeed=-5
        self.gravity=5
    def drawShip(self, win):
        image = pygame.transform.scale(self.image, (160, 160))
        image_rect = image.get_rect()
        image_rect.center = (self.x, self.y)
        image_rect.top = self.y - self.height
        #pygame.draw.rect(win, (255, 0, 0), self.offset_rect, 2)
        win.blit(image, image_rect)

        
    def update(self): 
        self.xspeed=0
        self.yspeed=0
        
        if  self.left_pressed and not self.right_pressed:
            self.xspeed =-self.speed
            self.image=left
            
            image = pygame.transform.scale(self.image, (250, 250))
        if  self.right_pressed and not self.left_pressed:
            self.xspeed = self.speed
            self.image= right
        

        if self.y >= 734:  # Check if ship hits the ground
            self.y = 734  # Set ship's y-coordinate to ground level
            self.gravity = 0  # Stop applying gravity
        if self.space_pressed:
                self.yspeed = self.upspeed
                self.image = jump
       
            
        self.x+=self.xspeed
        self.y+=self.yspeed
        if self.y <= 734 and self.allow_vertical_movement:  # Allow vertical movement if True
            self.gravity += 0.105  # change gravity strength
            self.y += self.gravity
        else:
            self.gravity = 0
        
            
        self.offset_rect = pygame.Rect(self.x - 11, self.y + 17, 30, 16)
        self.rect=pygame.Rect(self.x,self.y,32,32)
    def collisions(self, tiles):
        collide = []
        for tile in tiles:
            if isinstance(tile, Tile) and self.rect.colliderect(tile.rect):
                collide.append(tile)
        return collide
    
    def collisions__(self):
        for row in tile_map.tiles:
            for tile in row:
                self.colliding_(tile)
                self.end_game(tile)
                self.game_over(tile)
        self.rect.x = self.x

        self.rect.x = self.x

    def end_game(self,tile):
        if tile.end and tile.rect.colliderect(self.offset_rect):
            if self.colour=="red":
                win.fill((0, 0, 0))  # Fill the surface with black color
                font = pygame.font.Font(None, 36)
                text = font.render("You lost!", True, (255, 255, 255))  # Render the text
                text_rect = text.get_rect(center=(400, 385))  # Set the text's position
                global lights
                lights=True
    def game_over(self,tile):
        global run
        if tile.death and tile.rect.colliderect(self.offset_rect):
            run=False

        
            
    def colliding_(self,tile):#collision detection function
        if self.colour=="blue":
            if tile.collidable and tile.rect.colliderect(self.offset_rect) and spaceship.left_pressed:
                self.speed = 2

            else:
                self.speed=3
            if tile.collidable and tile.rect.colliderect(self.offset_rect) and spaceship.right_pressed:
                self.speed = 2
            else:
                self.speed=3
            
            if tile.collidable and tile.rect.colliderect(self.offset_rect) and spaceship.gravity > 0:
                self.gravity = 0
                self.yspeed = 0
                #spaceship.y = tile.rect.top - spaceship.rect.height
        


right=pygame.image.load('right.png.png')
left=pygame.image.load('left.png.png')
idle=pygame.image.load('idle.png.png')
jump=pygame.image.load('jump.png.png')
class Wheel:
    def __init__(self,x,y):
        self.image=pygame.image.load("wheel.png.png")
        self.x=x
        self.y=y
        self.shift_pressed=False
        
        #self.radius=radius
        #self.colour=colour
    def drawwheel(self,playerx,playery):
        if self.shift_pressed:
            wheel_x = playerx - self.image.get_width() // 2
            wheel_y = playery - self.image.get_height() // 2
            win.blit(self.image, (wheel_x, wheel_y))


class Tile(pygame.sprite.Sprite):
    def __init__(self, image, x, y, collidable= False,death=False, end=False):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = int(x), int(y)
        self.collidable = collidable
        self.end=end
        self.death=death

    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))

class TileMap:
    def __init__(self, filename):
        self.tile_size = 32
        self.tiles = self.load_tiles(filename)
        self.map_w = len(self.tiles[0]) * self.tile_size
        self.map_h = len(self.tiles) * self.tile_size
        self.tile_group = pygame.sprite.Group()
    def load_tiles(self, filename):
        tiles = []
        with open(filename, 'r') as file:
            #reader = csv.reader(file)
            for line in file:
                row_tiles = []
                row = line.split(',')
                for tile in row:
                    if tile == '2':
                        row_tiles.append(Tile('dark_tile.png', len(row_tiles) * self.tile_size, len(tiles) * self.tile_size, collidable=True ,end=True))
                   
                    if tile == '-1':
                        row_tiles.append(Tile('empty.png', len(row_tiles) * self.tile_size, len(tiles) * self.tile_size))
                    elif tile == '1':
                        row_tiles.append(Tile('lava.png', len(row_tiles) * self.tile_size, len(tiles) * self.tile_size, collidable=True,death=True ))
                    else:
                        row_tiles.append(Tile('brick.png', len(row_tiles) * self.tile_size, len(tiles) * self.tile_size, collidable=True))
                tiles.append(row_tiles)
        return tiles

    def draw_map(self, surface):
        for row in self.tiles:
            for tile in row:
                tile.draw(surface)







#mapp=Map.map_reader("map1.csv")







class Enemy(): #class for the enemies within the game, used for implimenting object that move around the map, chasing the player 
    def __init__(self, x,y,width,height, colour):
        #self.image= pygame.image.load('agro.png.png')
        self.image= pygame.image.load('calm.png.png')
        self.x=x
        self.y=y
    
        self.width=width
        self.height=height
        self.colour=colour
        self.rect=pygame.Rect(x,y,32,32)
       
       
        self.distance_above_player =1
        self.speed=3
        self.upspeed=-10
        self.gravity=2
    def col(self):
        global lost
        global enemies
   
        
        enemies_to_remove = []
        for enemy in enemies:
            if not lights:
                enemy.updateenemy(tile_map.tiles, win)  # Pass tile_map.tiles instead of tiles

        for enemy in enemies:
            enemy.drawenemy(win)
            collision = pygame.sprite.collide_rect(enemy, spaceship)
            if collision:
                if spaceship.colour=="yellow":
                    enemies_to_remove.append(enemy)
                else:
                    
                    lost=True        
             
            

        for enemy in enemies_to_remove:
            enemies.remove(enemy)
           
      
    def drawenemy(self, win):#draws the enemy onto the surface
        image = pygame.transform.scale(self.image, (160, 160))
        image_rect = image.get_rect()
        image_rect.center = (self.x, self.y)
        image_rect.top = self.y - self.height
        win.blit(image, image_rect)
    def updateenemy(self,tiles,win):
        lava_tiles = [tile for tile in tile_map.tile_group if tile.end]  # Access tile_map.tile_group instead of tiles.tile_group

        if pygame.sprite.spritecollideany(self, lava_tiles):
         self.speed = 0
        if not pygame.sprite.spritecollideany(self, lava_tiles):
            self.speed = 1
        d= math.sqrt( ((enemy.x-spaceship.x)**2)+((enemy.y-spaceship.y)**2) )#distance formula to calculate the distance between enemy and player to help enemy AI chase player
        
        try:
            x = (spaceship.x - self.rect.x) / d
            y = ((spaceship.y - self.distance_above_player)  - self.rect.y) / d
        except ZeroDivisionError: 
            return False
         
        self.x += x * self.speed
        self.y += y * self.speed
        self.rect = pygame.Rect(self.x, self.y, 32, 32)

















x=50
y=700
spaceship = Ship(x,y,20,20,(250,120,220))#instance of ship class/player object


lights=False
enemycount=0
pygame.init()
win=pygame.display.set_mode((800,770))#creating the surface for the gamr
agro=pygame.image.load('agro.png.png')
calm=pygame.image.load('calm.png.png')

font = pygame.font.Font(None, 24)
def screen_info():#function that grabs the infromation of the screen such as width and height to help with dynamic screen size game calculations
    screen_info = pygame.display.Info()
    screen_width = screen_info.current_w
    screen_height = screen_info.current_h
    return screen_width, screen_height
screen_width, screen_height = screen_info()


wheel =Wheel(x, y,)
tile_map = TileMap('map1.csv')#instance of TileMap class
run= True

enemies=[]
for i in range(10):#loop tgat creates enemies at different random locations, then appends them to an array
    x=random.randint(0, screen_width)
    y=random.randint(0, screen_height)
    enemy = Enemy(x, y, 200, 200, (120, 150, 225))
    enemies.append(enemy)

      
        


lost=False
FPS= 60
clock= pygame.time.Clock()
start_surf()
while run is True: 
    
    
    clock.tick(FPS)
    keys = pygame.key.get_pressed()
    for enemy in enemies:
        d= math.sqrt( ((enemy.x-spaceship.x)**2)+((enemy.y-spaceship.y)**2) )
        captured=False
        if d<400 and not captured:
            enemy.image= agro
        
        else:
            enemy.image= calm
        if d<=5:
            captured=True
        if captured:
            winning()
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run= False
        if event.type== pygame.KEYDOWN:
            if event.key==pygame.K_LSHIFT:
                
                wheel.shift_pressed=True
                
            if event.key==pygame.K_LEFT:
                spaceship.left_pressed=True
            if event.key==pygame.K_RIGHT:
                spaceship.right_pressed=True
            if event.key==pygame.K_SPACE:
                spaceship.space_pressed=True
        if event.type== pygame.KEYUP:
            if event.key==pygame.K_LSHIFT:
                
                wheel.shift_pressed=False
            if event.key==pygame.K_LEFT:
                spaceship.left_pressed=False
            if event.key==pygame.K_RIGHT:
                spaceship.right_pressed=False  
            if event.key==pygame.K_SPACE:
                spaceship.image= pygame.image.load('idle.png.png')
               
                spaceship.space_pressed=False
        if event.type == pygame.MOUSEMOTION:
                if wheel.shift_pressed:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    angle = math.atan2(mouse_y - spaceship.y, mouse_x - spaceship.x)
                    angle_deg = math.degrees(angle) % 360
                    if angle_deg >=30 and angle_deg < 140:
                        spaceship.colour="yellow"
                        wheel.image = pygame.image.load("yellow.png")  # Change image for first 120 degrees
                    elif angle_deg >= 140 and angle_deg < 260:
                         spaceship.colour="blue"
                         wheel.image = pygame.image.load("blue.png")  # Change image for second 120 degrees
                    else:
                         spaceship.colour="red"
                         wheel.image = pygame.image.load("red.png")  # Change image for third 120 degrees
                #pygame.mouse.get_pos()
        
       
    pygame.display.update()
    win.fill((220,220,220)) 
    
    tile_map.draw_map(win)
    spaceship.drawShip(win)
    spaceship.update()
    spaceship.collisions__()
    wheel.drawwheel(spaceship.x, spaceship.y)
    enemy.col()
   
        
  
    if  len(enemies) == 0:
        win.fill((0,0,0))
        winning()
    if lost:
        win.fill((0,0,0))
        losing()
    if spaceship.x >= screen_width:
        spaceship.x = 0
    elif spaceship.x <= 0:
        spaceship.x = screen_width - 1
    elif spaceship.y >= 734: 
        spaceship.y=734

pygame.quit()
