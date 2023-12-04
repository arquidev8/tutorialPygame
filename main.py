import math

import pygame
import random

pygame.init()

screen = pygame.display.set_mode(( 800, 600 ))


#Title and icon
pygame.display.set_caption("My game")
icon = pygame.image.load('joystick.png')
pygame.display.set_icon(icon)

#player
playerImg = pygame.image.load('spaceship.png')
playerX = 400
playerY = 500
playerX_change = 0

#enemy
enemyImg = pygame.image.load('alien.png')
enemyX = random.randint(0, 735)
enemyY = random.randint(50, 150)
enemyX_change = 0.3
enemyY_change = 40

#gun
gunImg = pygame.image.load('gun.png')
gunX = 0
gunY = 500
gunX_change = 0
gunY_change = 1
gun_state = "ready"

#background
background = pygame.image.load('background.png')

score = 0

def player(x, y):
    screen.blit(playerImg, (x, y))

def enemy(x, y):
    screen.blit(enemyImg, (x, y))

def fire_gun(x,y):
    global gun_state
    gun_state = "fire"
    screen.blit(gunImg,(x +16 ,y + 10))


def isCollision(enemyX, enemyY, gunX, gunY):
    distance = math.sqrt((math.pow(enemyX-gunX,2)) + (math.pow(enemyY-gunY,2)))
    if distance < 27:
        return True
    else:
        return False

#Game loop
running = True
while running:

    screen.fill((0, 0, 0))

    screen.blit(background, (0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.4
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.4
            if event.key == pygame.K_SPACE:
                if gun_state == "ready":
                    gunX = playerX
                    fire_gun(playerX, gunY)


        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    #player windows limits
    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    #move enemy
    enemyX += enemyX_change

    if enemyX <= 0:
        enemyX_change = 0.3
        enemyY += enemyY_change
    elif enemyX >= 736:
        enemyX_change = -0.4
        enemyY += enemyY_change


    #gun movement
    if gunY <= 0:
        gunY = 500
        gun_state = "ready"

    if gun_state == "fire":
        fire_gun(gunX, gunY)
        gunY -= gunY_change


    collision = isCollision(enemyX, enemyY, gunX, gunY)
    if collision:
        gunY = 480
        gun_state = "ready"
        score += 1
        print(score)
        enemyX = random.randint(0, 735)
        enemyY = random.randint(50, 150)

    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()