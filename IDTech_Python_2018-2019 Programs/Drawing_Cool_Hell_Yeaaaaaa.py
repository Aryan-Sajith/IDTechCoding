import pygame, sys

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
yellow = (255, 255, 0)

gameDisplay = pygame.display.set_mode((800, 600))
gameDisplay.fill(black)
#pygame.draw.line()
pygame.draw.circle(gameDisplay, yellow, (400, 200), 50)
pygame.draw.line(gameDisplay,white,(400,250),(400,400),2)#body
pygame.draw.line(gameDisplay,blue,(400,400),(370,550),2)
pygame.draw.line(gameDisplay,blue,(400,400),(430,550),2)
pygame.draw.line(gameDisplay,green,(400,325),(330,250),2)
pygame.draw.line(gameDisplay,green,(400,325),(470,250),2)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    pygame.display.update()
