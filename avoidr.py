# import libraries
import pygame
import os, time, math, random
from random import randint

# import the player class
from player import Player
# import the obstacle class, for obstacles that the player must avoid
from obstacle import Obstacle

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

	# the number of
	bgFramesToSkip = 10
	# counter for number of frames to skip for the color flashing
	skippedBgFrames = 0

	# create a player object
	player = Player(width,height)

	# the number of obstacles objects to create
	numObstacles = 10
	# create the obstacle objects
	obstacle = []
	for o in range(0,numObstacles):
		obstacle.append(Obstacle(width,height))

	clock = pygame.time.Clock()

	startTimer = time.clock()

	# the main game loop
	while gameRunning:

		# lock the gameloop at 60 fps
		clock.tick(60)

		#-----------------------START: player / obstacle position updating-----------------------#

		# update the size of the player (the player glows in size in a sinusoidal fashion)
		player.updateSize()

		# player movement + collision detection
		keys = pygame.key.get_pressed()

		# update the player position (move according to keystrokes)
		player.updatePos(keys)

		# move the obstacles along
		for o in range(0,(numObstacles)):
			obstacle[o].updatePos()

		# restart game if collision with box accures
		# MOVE THIS TO THE OBSTACLE CLASS SOON (SEND IN THE PLAYER POSITION)
		for o in range(0,(numObstacles)):
			if player.posX in range(obstacle[o].posX - player.size, obstacle[o].posX + obstacle[o].size + player.size) and \
			   player.posY in range(obstacle[o].posY - player.size, obstacle[o].posY + obstacle[o].size + player.size):
				# quit the current game
				gameRunning = False

		#------------------------END: player / obstacle position updating------------------------#

		#---------------------START: draw/blit background, player, obstacles, & timer---------------------#

		# fill the screen with a random background color
		if skippedBgFrames == bgFramesToSkip:
			skippedBgFrames = 1
			bgR, bgG, bgB = randint(0,255), randint(0,255), randint(0,255)
		screen.fill((bgR,bgG,bgB))

		invertedBgColor = (255-bgR,255-bgG,255-bgB)

		# draw all obstacles
		for o in range(0,Obstacle.count):
			pygame.draw.rect(screen, invertedBgColor, (obstacle[o].posX, obstacle[o].posY, obstacle[o].size, obstacle[o].size), 0)

		# draw the main character
		pygame.draw.circle(screen, (255-bgR,255-bgG,255-bgB), (player.posX, player.posY), player.size, 0)

		# draw the timer on the screen
		timeString = '%.3g' % ((time.clock() - startTimer))
		timerText = timerFont.render(timeString, 1, (255,255,255))
		screen.blit(timerText, (50, 20))

		pygame.display.flip()

		#----------------------END: draw/blit background, player, obstacles, & timer----------------------#

		#------------------------START: player movement input handling------------------------#

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

		#-------------------------END: player movement input handling-------------------------#

		skippedBgFrames += 1

	pygame.mixer.music.stop()

