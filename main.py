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
playerX_change = 0

def player(x, y):
    screen.blit(playerImg, (x, y))

#Game loop
running = True
while running:

    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.1
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    playerX += playerX_change
    player(playerX, playerY)
    pygame.display.update()