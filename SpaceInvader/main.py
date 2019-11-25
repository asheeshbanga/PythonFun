import pygame
import random

# Initialization
pygame.init()

# Create the screen
screen = pygame.display.set_mode( (800,600) )

# Title and icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("c:/Users/abanga/Documents/Python/SpaceInvader/spaceinvaders.png")
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load("c:/Users/abanga/Documents/Python/SpaceInvader/player.png")
playerX = 370
playerY = 480
px = 0

# Enemy
enemyImg = pygame.image.load("c:/Users/abanga/Documents/Python/SpaceInvader/enemy.png")
enemyX = random.randint(0,736)
enemyY = random.randint(50,150)
ex = 0

def player(x, y):
  screen.blit(playerImg, (x, y))

def enemy(x, y):
  screen.blit(enemyImg, (x, y))

# Game Loop

# RGB = Red, Green, Blue
screen.fill( (0, 0, 0) )

running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

    # if keystroke is pressed 
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_LEFT:
        px = -0.2
      if event.key == pygame.K_RIGHT:
        px = 0.2
    if event.type == pygame.KEYUP:
      if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
        px = 0

  playerX += px

  if playerX <=0:
    playerX = 0
  elif playerX >= 736:
    playerX = 736

  player(playerX, playerY)
  enemy(enemyX, enemyY)
  pygame.display.update()