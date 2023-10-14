import os
import sys
import random

try:
    import pygame

except: 
    os.system("pip3 install pygame --upgrade")

pygame.init()

X = 800
Y = 800

lastX = X
lastY = Y

sqx = random.randint(0, X)
sqy = random.randint(0, Y)

mx = pygame.mouse.get_pos()[0]
my = pygame.mouse.get_pos()[1]

version = "1.0.0"

pygame.display.set_caption(f"Kliker - {version}")

window = pygame.display.set_mode((800, 800), pygame.RESIZABLE)

def keyPress():
    if (pygame.key.get_pressed()[pygame.K_ESCAPE]):
        pygame.quit()
        sys.exit(0)

def clickFunc():
    global sqx, sqy, mx, my

    if any(pygame.mouse.get_pressed()):
        if (mx >= sqx and mx <= sqx + 50 and my >= sqy and my <= sqy + 50):
            sqx = random.randint(0, X)
            sqy = random.randint(0, Y)

def main():
    pygame.draw.rect(window, (0, 0, 0), (sqx, sqy, 50, 50))

    keyPress()
    clickFunc()

def mainUpdate():
    global mx, my, X, Y

    pygame.display.update()

    window.fill((255, 255, 255))

    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            pygame.quit()
            sys.exit(0)

    X = window.get_size()[0]
    Y = window.get_size()[1]

    mx = pygame.mouse.get_pos()[0]
    my = pygame.mouse.get_pos()[1]

if __name__ == "__main__":
    while 1:
        mainUpdate()
        main()

