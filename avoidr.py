# import libraries
import pygame
import os, time, math
from random import randint

# initializing pygame/pygame modules
pygame.init()

# imports ogg sound file
pygame.mixer.music.load(os.path.join('audio','death.beat.v1.wav'))

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
pygame.display.set_caption('avoidr.v0.05')

pygame.mouse.set_visible(False)

# the menu screen
# initialize font; must be called after 'pygame.init()' to avoid 'Font not Initialized' error
logoFont = pygame.font.SysFont("monospace", 100)
instrFont = pygame.font.SysFont("monospace", 27)

# render text
logoText = logoFont.render("AVOIDR", 1, (255,255,255))
screen.blit(logoText, (100, 60))
instrText = instrFont.render("press spacebar to start", 1, (255,255,255))
screen.blit(instrText, (100, 170))
pygame.display.flip()

gameStart = True
gameRunning = True

# create the initial random background color
bgR = randint(0,255)
bgG = randint(0,255)
bgB = randint(0,255)

# game loop for start screen
while gameStart:
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
	bgR = randint(0,255)
	bgG = randint(0,255)
	bgB = randint(0,255)
	screen.fill((bgR,bgG,bgB))
	screen.blit(logoText, (100, 60))
	screen.blit(instrText, (100, 170))
	pygame.display.flip()
	time.sleep(0.1)

# plays music infinitly
pygame.mixer.music.play(-1)

# counter for number of frames to skip for the color flashing
framesToSkip = 1

# player values
playerX = width/2
playerY = height/2
playerSpeed = 1
playerSize = 25
playerSizeMax = 50
counter = 1

# the main game loop
while gameRunning:
	# fill the screen with a random background color
	if framesToSkip == 50:
		framesToSkip = 1
		bgR = randint(0,255)
		bgG = randint(0,255)
		bgB = randint(0,255)
	screen.fill((bgR,bgG,bgB))
	# draw the main character
	pygame.draw.circle(screen, (255-bgR,255-bgG,255-bgB), (playerX, playerY), playerSize, 0)
	pygame.display.flip()
	# playerSize changes
	if counter == 1 and playerSize >= 25:
		playerSize = playerSize + 1
		if playerSize >= 50:
			counter = 0
	if counter == 0 and playerSize <= 50:
		playerSize = playerSize - 1
		if playerSize <= 25:
			counter = 1
	# handle input
	for event in pygame.event.get():
		# exit if X button is pushed
		if event.type == pygame.QUIT:
			gameRunning = False
			pygame.QUIT
		# exit if ESC key is pushed
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				gameRunning = False
			 	pygame.QUIT
	# player movement + collision detection
	keys = pygame.key.get_pressed()
	# left border collision detection
	if playerX != 0 + playerSizeMax:
		# player movement input
		if keys[pygame.K_LEFT]:
			playerX = playerX - playerSpeed
	# right border collision detection
	if playerX != width - playerSizeMax:
		# player movement input
		if keys[pygame.K_RIGHT]:
			playerX = playerX + playerSpeed
	# vertical border collision detection
	if playerY != 0 + playerSizeMax:
		# player movement input
		if keys[pygame.K_UP]:
			playerY = playerY - playerSpeed
	# vertical border collision detection
	if playerY != height - playerSizeMax:
		# player movement input
		if keys[pygame.K_DOWN]:
			playerY = playerY + playerSpeed
	# increment frames to skip - standardize this later!
	framesToSkip = framesToSkip + 1
	# delay the loop a bit - bind this to 60 fps later
	time.sleep(0.001)
