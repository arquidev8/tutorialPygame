import pygame

pygame.init()

screen = pygame.display.set_mode(( 800, 600 ))


#Title and icon
pygame.display.set_caption("My game")
icon = pygame.image.load('joystick.png')
pygame.display.set_icon(icon)

#player
playerImg = pygame.image.load('spaceship.png')
playerX = 400
playerY = 300

def player(x, y):
    screen.blit(playerImg, (x, y))

#Game loop
running = True
while running:

    screen.fill((0, 0, 0))
    playerX += 0.2
    print(playerX)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player(playerX, playerY)
    pygame.display.update()