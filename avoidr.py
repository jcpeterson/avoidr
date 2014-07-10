# AVOIDR v0.01

# import libraries
import pygame
import os, time, math, random
from random import randint

from menu import Menu
# import the player class
from player import Player
# import the obstacle class, for obstacles that the player must avoid
from obstacle import Obstacle

# initializing pygame/pygame modules
pygame.init()

menu = Menu()
#menu.show('main')

# a simple function to generate random color RGB triplets
def generateRandColor():
	return (randint(0,255), randint(0,255), randint(0,255))

exit = False
restart = True

while restart == True:

	exit = menu.exitOrNot()
	if exit == False:
		menu.show('main')
	else:
		restart = False
	exit = menu.exitOrNot()

	if exit == False:

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
		pygame.display.set_caption('avoidr.v0.09')

		pygame.mouse.set_visible(False)

		WHITE = (255,255,255)

		gameStart = True
		gameRunning = True

		# create the initial random background color
		backgroundColor = generateRandColor()

		# initialize timer font; must be called after 'pygame.init()' to avoid 'Font not Initialized' error
		timerFont = pygame.font.SysFont("Arial", 100, bold=True)

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
		numObstacles = 50
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

			#-----------------------START: player/obstacle size/position updating-----------------------#
	        #                                                                                           #
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
			if player.isJumping == False:
				for o in range(0,(numObstacles)):
					if player.posX in range(obstacle[o].posX - player.size, obstacle[o].posX + obstacle[o].size + player.size) and \
					   player.posY in range(obstacle[o].posY - player.size, obstacle[o].posY + obstacle[o].size + player.size):
						# quit the current game
						gameRunning = False
	        #                                                                                           #
			#------------------------END: player/obstacle size/position updating------------------------#

			#---------------------START: draw/blit background, player, obstacles, & timer---------------------#
	        #																								  #
			# fill the screen with a random background color
			if skippedBgFrames == bgFramesToSkip:
				skippedBgFrames = 1
				backgroundColor = generateRandColor()
			screen.fill(backgroundColor)

			# draw all obstacles
			for o in range(0,numObstacles):
				obstacle[o].updateColor(backgroundColor)
				pygame.draw.rect(screen, obstacle[o].color, (obstacle[o].posX, obstacle[o].posY, obstacle[o].size, obstacle[o].size), 0)				

			# update the player color
			player.updateColor(backgroundColor)

			# draw the main character
			pygame.draw.circle(screen, player.color, (player.posX, player.posY), player.size, 0)

			# draw the timer on the screen
			timeString = '%.3g' % ((time.clock() - startTimer))
			timerText = timerFont.render(timeString, 1, WHITE)
			screen.blit(timerText, (50, 20))

			# render everything that has just been drawn/blitted to the screen
			pygame.display.flip()

			#																								  #
			#----------------------END: draw/blit background, player, obstacles, & timer----------------------#

			#------------------------START: game input handling------------------------#
			# 																		   #
			for event in pygame.event.get():
				# exit if X button is pushed
				if event.type == pygame.QUIT:
					gameRunning = False
					#restart = False
					#pygame.display.quit()
					pygame.QUIT
				# exit if ESC key is pushed
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE:
						gameRunning = False
						#restart = False
						#pygame.display.quit()
					 	pygame.QUIT
			#																		   #
			#-------------------------END: game input handling-------------------------#

			# iterate the number of skipped frames
			skippedBgFrames += 1

	pygame.mixer.music.stop()

