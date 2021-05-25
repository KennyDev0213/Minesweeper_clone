import pygame

pygame.init()
pygame.display.set_mode((250,250))
x = pygame.mouse.get_pressed()
while 1:
    if x[1]:
        print(x)