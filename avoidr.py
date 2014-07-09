# import libraries
import pygame
import os, time, math, random
from random import randint

# import the obstacle class, for obstacles that the player must avoid
from obstacle import Obstacle

# obs = obstacle(1000,600)

# initializing pygame/pygame modules
pygame.init()

# imports ogg sound file
pygame.mixer.music.load(os.path.join('audio','epica.v1.wav'))

# initialize the display
pygame.display.init()
# get information about the display
# we only really care about the size of the display
displayInfo = pygame.display.Info()
# put the width and height of the user's screen in variables
width = displayInfo.current_w
height = displayInfo.current_h

# create a new window
screen = pygame.display.set_mode((width, height),pygame.FULLSCREEN)
# set the window caption
pygame.display.set_caption('avoidr.v0.08')

pygame.mouse.set_visible(False)

# the menu screen
# initialize font; must be called after 'pygame.init()' to avoid 'Font not Initialized' error
logoFont = pygame.font.SysFont("monospace", 100)
instrFont = pygame.font.SysFont("monospace", 27)
timerFont = pygame.font.SysFont("Arial", 100, bold=True)

# render text
logoText = logoFont.render("AVOIDR", 1, (255,255,255))
screen.blit(logoText, (100, 60))
instrText = instrFont.render("press spacebar to start", 1, (255,255,255))
screen.blit(instrText, (100, 170))
pygame.display.flip()

gameStart = True
gameRunning = True

# create the initial random background color
bgR, bgG, bgB = randint(0,255), randint(0,255), randint(0,255)

menuClock = pygame.time.Clock()

# game loop for start screen
while gameStart:
	# lock the loop at 5 fps
	menuClock.tick(5)
	# handle input
	for event in pygame.event.get():
		#  start the game if spacebar is pressed
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				gameStart = False
			# exit if ESC key is pushed
			if event.key == pygame.K_ESCAPE:
				gameStart = False
				gameRunning = False
	# create three random r,g,b values
	bgR, bgG, bgB = randint(0,255), randint(0,255), randint(0,255)
	screen.fill((bgR,bgG,bgB))
	screen.blit(logoText, (100, 60))
	screen.blit(instrText, (100, 170))
	pygame.display.flip()

restart = True

while restart == True:
	gameRunning = True

	# plays music infinitly
	pygame.mixer.music.play(-1)

	# counter for number of frames to skip for the color flashing
	framesToSkip = 1

	# player values
	playerX = width/2
	playerY = height/2
	playerSpeed = 10
	playerSizeMax = 20
	playerSizeMin = 10
	playerSize = playerSizeMin

	playerState = 'growing'

	numObstacles = 30

	obstacle = []
	for o in range(0,numObstacles):
		obstacle.append(Obstacle(width,height))

	clock = pygame.time.Clock()

	startTimer = time.clock()

	# the main game loop
	while gameRunning:

		# lock the gameloop at 60 fps
		clock.tick(60)

		# move the obstacles along
		for o in range(0,(numObstacles)):

			if obstacle[o].posX >= width - obstacle[o].size or obstacle[o].posX <= 0:
				obstacle[o].dirX *= -1

			if obstacle[o].posY >= height - obstacle[o].size or obstacle[o].posY <= 0:
				obstacle[o].dirY *= -1

			# the objects new position is its current position plus its (direction (-1 or 1) * its speed (number of pixels to move))
			obstacle[o].posX = obstacle[o].posX + (obstacle[o].dirX * obstacle[o].speed)

			# the objects new position is its current position plus its (direction (-1 or 1) * its speed (number of pixels to move))
			obstacle[o].posY = obstacle[o].posY + (obstacle[o].dirY * obstacle[o].speed)

		# restart game if collision with box accures
		for o in range(0,(numObstacles)):
			if playerX in range(obstacle[o].posX - playerSize, obstacle[o].posX + obstacle[o].size + playerSize) and \
			   playerY in range(obstacle[o].posY - playerSize, obstacle[o].posY + obstacle[o].size + playerSize):
				gameRunning = False
				#pygame.QUIT

		# fill the screen with a random background color
		if framesToSkip == 10:
			framesToSkip = 1
			bgR, bgG, bgB = randint(0,255), randint(0,255), randint(0,255)
		screen.fill((bgR,bgG,bgB))

		# draw all obstacles
		for o in range(0,numObstacles):
			pygame.draw.rect(screen, (255-bgR,255-bgG,bgB), (obstacle[o].posX, obstacle[o].posY, obstacle[o].size, obstacle[o].size), 0)

		# draw the main character
		pygame.draw.circle(screen, (255-bgR,255-bgG,255-bgB), (playerX, playerY), playerSize, 0)

		# draw the timer on the screen
		timeString = '%.3g' % ((time.clock() - startTimer))
		timerText = timerFont.render(timeString, 1, (255,255,255))
		screen.blit(timerText, (50, 20))

		pygame.display.flip()
		# playerSize changes
		if playerState == 'growing' and playerSize >= playerSizeMin:
			playerSize = playerSize + 1
			if playerSize >= playerSizeMax:
				playerState = 'shrinking'
		if playerState == 'shrinking' and playerSize <= playerSizeMax:
			playerSize = playerSize - 1
			if playerSize <= playerSizeMin:
				playerState = 'growing'
		# handle input
		for event in pygame.event.get():
			# exit if X button is pushed
			if event.type == pygame.QUIT:
				gameRunning = False
				restart = False
				pygame.QUIT
			# exit if ESC key is pushed
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					gameRunning = False
					restart = False
				 	pygame.QUIT
		# player movement + collision detection
		keys = pygame.key.get_pressed()
		# left border collision detection
		if (playerX != 0 + playerSizeMax) and (playerX > 0 + playerSizeMax + 5):
			# player movement input
			if keys[pygame.K_LEFT]:
				playerX = playerX - playerSpeed
		# right border collision detection
		if (playerX != width - playerSizeMax) and (playerX < width - (playerSizeMax + 5)):
			# player movement input
			if keys[pygame.K_RIGHT]:
				playerX = playerX + playerSpeed 
		# vertical border collision detection
		if (playerY != 0 + playerSizeMax) and (playerY > 0 + playerSizeMax + 5):
			# player movement input
			if keys[pygame.K_UP]:
				playerY = playerY - playerSpeed
		# vertical border collision detection
		if (playerY != height - playerSizeMax) and (playerY < height - (playerSizeMax + 5)):
			# player movement input
			if keys[pygame.K_DOWN]:
				playerY = playerY + playerSpeed
		framesToSkip = framesToSkip + 1

	pygame.mixer.music.stop()

