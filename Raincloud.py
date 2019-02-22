import pygame
import random
from pygame.locals import *
#initialisation, on all pygames
pygame.init()
pygame.display.set_caption("My first PyGame program")
screen = pygame.display.set_mode((640,480))
pressed_key = pygame.key.get_pressed()

cloud_image = pygame.image.load("cloud.jpg").convert()
human_image = pygame.image.load("human.png").convert_alpha()

# xpos = 5
# ypos = 5
xpos = 0
ypos = 0
clock = pygame.time.Clock()
rainList = []
hxpos = 0

class Raindrop:


    def __init__(self):
        self.x = random.randint(xpos,xpos+239)
        self.y = random.randint(211,212)
        self.speed = random.randint(3,8)
        self.size = random.randint(0,10)
        # self.rect = self.image.get_rect()

    def draw(self):
        pygame.draw.circle(screen, (169, 162, 160), (self.x, self.y), self.size, self.size)

    def move(self):
        self.y = self.y + self.speed



while 1:
    clock.tick(60)
    screen.fill((88,78,76))
    screen.blit(cloud_image, (xpos,0))
    screen.blit(human_image, (hxpos,433))
    pressed_key = pygame.key.get_pressed()

    if pressed_key[K_RIGHT] and hxpos <= 640:
        hxpos += 2
    if pressed_key[K_LEFT]and hxpos >= 0:
        hxpos -= 2
    ## important##

    xpos+=1

    if xpos > 640:
        xpos = -239

    rainList.append(Raindrop())
    for i in rainList:
        i.draw()
        i.move()
        if i.y > 480:
            rainList.remove(i)





    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    pygame.display.update()