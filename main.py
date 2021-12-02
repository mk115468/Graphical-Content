#EXERCISE 1

import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
pygame.display.set_mode(size=(0, 0), flags=0, depth=0, display=0)
scn_width = 640
scn_height = 480
screen = pygame.display.set_mode((scn_width, scn_height))
screen.fill(BLUE)
pygame.draw.rect(screen, WHITE, (250,300,200,150)) #HOME
pygame.draw.rect(screen, BLACK, (320,375,50,75)) #DOOR
pygame.draw.polygon(screen,WHITE,((200,300),(400,200),(500,300))) #ROOF
pygame.draw.circle(screen, BLACK, [345, 330], 25) #WINDOW
pygame.display.flip()

#EXERCISE 2

import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
pygame.display.set_mode(size=(0, 0), flags=0, depth=0, display=0)
scn_width = 800
scn_height = 500
screen = pygame.display.set_mode((scn_width, scn_height))
screen.fill(WHITE)
for x in range(30):
  pygame.draw.ellipse(screen, BLACK,[x*25,200,35,10],2)
pygame.display.flip()

#EXERCISE 3

import pygame

pygame.init()
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
pygame.display.set_mode(size=(0, 0), flags=0, depth=0, display=0)
scn_width = 800
scn_height = 500
screen = pygame.display.set_mode((scn_width, scn_height))
screen.fill(WHITE)
print(pygame.font.get_fonts())
font=pygame.font.SysFont("dejavusans",65)
text=font.render("Game Time!",True,BLACK)
tw = text.get_width()
th = text.get_height()
screen_width = screen.get_width()
screen_height = screen.get_height()
screen.blit(text, [0, 0])
screen.blit(text, [screen_width / 2 -tw / 2, screen_height / 2 -th / 2])
screen.blit(text, [screen_width -tw, screen_height -th])
pygame.display.flip()
