import pygame
from pygame import mixer
import random
import math

# Initialization
pygame.init()

# Create the screen
screen = pygame.display.set_mode( (800,600) )

# Background
background = pygame.image.load("c:/Users/abanga/Documents/Python/SpaceInvader/space.jpg")

# Background sound
mixer.music.load("c:/Users/abanga/Documents/Python/SpaceInvader/imperial_march.wav")
mixer.music.set_volume(0.25)
mixer.music.play(-1)

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
enemyImg = []
enemyX = []
enemyY = []
ex = []
ey = []

num_of_enemies = 5

for i in range(num_of_enemies):
  enemyImg.append(pygame.image.load("c:/Users/abanga/Documents/Python/SpaceInvader/enemy2.png"))
  enemyX.append(random.randint(0,735))
  enemyY.append(random.randint(50,150))
  ex.append(3)
  ey.append(50)

# Bullet

# Ready - You cannot see the bullet on the screen
# Fire - The bullet is currently moving
bulletImg = pygame.image.load("c:/Users/abanga/Documents/Python/SpaceInvader/bullet.png")
bulletX = 0
bulletY = 480
bx = 0
by = 10
b_state = "ready"

# Score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 24)
textX = 370
textY = 10

# Game over text
over_font = pygame.font.Font('freesansbold.ttf', 64)

def show_score(x, y):
  score = font.render("Score: " + str(score_value), True, (255,255,255))
  screen.blit(score, (x, y))

def game_over_text():
  over_text = over_font.render("GAME OVER", True, (255,255,255))
  screen.blit(over_text, (200, 250))

def player(x, y):
  screen.blit(playerImg, (x, y))

def enemy(x, y, i):
  screen.blit(enemyImg[i], (x, y))

def fire_bullet(x, y):
  global b_state
  b_state = "fire"
  screen.blit(bulletImg, (x + 16, y + 10))

def isCollision(enemyX, enemyY, bulletX, bulletY):
  distance = math.sqrt(math.pow(enemyX-bulletX, 2) + math.pow(enemyY-bulletY, 2))
  if distance < 27:
    return True
  else:
    return False

# Game Loop

running = True
while running:

  # RGB = Red, Green, Blue
  screen.fill( (0, 0, 0) )
  # Background image
  screen.blit(background, (0,0))

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

    # if keystroke is pressed 
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_LEFT:
        px = -2
      if event.key == pygame.K_RIGHT:
        px = 2
      if event.key == pygame.K_SPACE:
        if b_state is "ready":
          b_sound = mixer.Sound("c:/Users/abanga/Documents/Python/SpaceInvader/gun_sound.wav")
          b_sound.set_volume(0.4)
          b_sound.play()
          # Get the x-coordinate of the spaceship to fire the bullet from
          bulletX = playerX
          fire_bullet(bulletX, bulletY)

    if event.type == pygame.KEYUP:
      if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
        px = 0

  # Checking for boundary of spaceship
  playerX += px

  if playerX <=0: 
    playerX = 0
  elif playerX >= 736:
    playerX = 736

  # Enemy movement
  for i in range(num_of_enemies):
    
    if enemyY[i] > 440 and ((enemyX[i] < playerX+32 and ex[i] == -2) or (enemyX[i] > playerX-32 and ex[i] == 2) ):
      for j in range(num_of_enemies):
        enemyY[j] = 2000
      game_over_text()
      break
    
    enemyX[i] += ex[i]

    if enemyX[i] <=0:
      ex[i] = 2
      enemyY[i] += ey[i]
    elif enemyX[i] >= 736:
      ex[i] = -2
      enemyY[i] += ey[i]

    # Collision
    collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
    if collision:
      c_sound = mixer.Sound("c:/Users/abanga/Documents/Python/SpaceInvader/collision_sound.wav")
      c_sound.set_volume(0.4)
      c_sound.play()
      bulletY = 480
      b_state = "ready"
      score_value += 1
      enemyX[i] = random.randint(0,735)
      enemyY[i] = random.randint(50,150)
    
    enemy(enemyX[i], enemyY[i], i)

  # Bullet Movement
  if bulletY <=0:
    bulletY = 480
    b_state = "ready"

  if b_state is "fire":
    fire_bullet(bulletX, bulletY)
    bulletY -= by

  player(playerX, playerY)
  show_score(textX, textY)
  pygame.display.update()