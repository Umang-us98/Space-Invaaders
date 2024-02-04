import pygame
import random
from pygame.locals import *
import time
pygame.init()
screen = pygame.display.set_mode((800,800))
pygame.display.set_caption("Space Invador")
Clock =pygame.time.Clock()
class Character:
    def __init__(self,x,y,color,width,length):
        self.x = x
        self.y = y
        self.length = length
        self.width = width
        self.color = color
    def draw(self):
        return pygame.draw.rect(screen, self.color, (self.x,self.y,self.width,self.length))
class Alien(Character):
    def move_Alien(self,flag,speed):
        if flag==True:
            self.y+=10
        self.x+=speed
class PlayerShip(Alien):
    def move(self,direction):
        if direction=="Left" and self.x>=0:
            self.x-=10
        elif direction=="Right" and self.x+self.width<=800:
            self.x+=10
class Bullet(Alien):
    def move(self,b):
        self.y-=10
        if self.y<=0:
            bullet.remove(b)
    def check(self,b,r,i):
        if b.colliderect(r):
            rectobj.remove(r)
            l.pop(i)
            return 1
            
        pass
        
bullet = []
player = PlayerShip(400,700,(255,0,0),150,50)
l = []
x = 0
y = 0
flag = False
direction = None
flag_move = False
speed = 10
for k in range(5):
    for j in range(10):
        l.append(Alien(x,y,(random.randint(0,250),random.randint(0,250),random.randint(0,250)),50,50))
        x=x+60
    y=y+60
    x=0
print(l)
while True :
    rectobj = []
    pygame.display.update()
    screen.fill((0,0,0))
    player.draw()
    if flag_move==True:
        player.move(direction)
    for x in l:
        rectobj.append(x.draw())
        if x.x+50>=800:
            speed = -10
            flag=True
        if x.x<=0:
            speed = 10
            flag=True
    for x in l:
        x.move_Alien(flag,speed)
    flag = False
    for b in bullet:
        t = b.draw()
        for i in range(len(rectobj)):
            if b.check(t,rectobj[i],i)==1:
                break
            
        b.move(b)
        
        
        
    Clock.tick(20)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                direction = "Left"
                flag_move = True
            if event.key == pygame.K_RIGHT:
                direction = "Right"
                flag_move = True
            if event.key==pygame.K_SPACE:
                temp = Bullet(player.x+70,player.y,(255,255,0),10,10)
                bullet.append(temp)
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                direction = None
                flag_move = False
            if event.key == pygame.K_RIGHT:
                direction = None
                flag_move = False
            
        if event.type == QUIT:
            pygame.quit()
            exit()
