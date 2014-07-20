# AVOIDR v0.14

import pygame

# this module may be removed in the future, so check for it...
try:
    import pygame.gfxdraw
    antialias = True
except ImportError:
    print 'this is a different version of pygame. antialiasing is off!'
    antialias = False

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

def generateRandColor():
	"""
    This function generates random RGB triplets.
    """
	return (randint(0,255), randint(0,255), randint(0,255))

exit = False
restart = True

while restart:

	exit = menu.exitOrNot()
	if not exit:
		menu.show('main')
	else:
		restart = False
	exit = menu.exitOrNot()

	if not exit:

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
		numObstacles = 27
		# create the obstacle objects
		obstacle = []
		for obs in range(numObstacles):
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
			for obs in obstacle:
				obs.updatePos()

			# restart game if collision with box accures
			# MOVE THIS TO THE OBSTACLE CLASS SOON (SEND IN THE PLAYER POSITION)
			# collision detection after jumping is currently hacky. should use a timer later on...
			if not player.isJumping or (player.size in range(player.sizeMin,player.sizeMin+5)):
				for obs in obstacle:
					if obs.rect.colliderect(player.rect):
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
			for obs in obstacle:
				obs.updateColor(backgroundColor)
				pygame.draw.rect(screen, obs.color, obs.rect, 0)

			# draw the player shadow if jumping
			if player.isJumping:
				#pygame.draw.circle(screen, (50,50,50), (player.posX, player.posY+25), player.sizeMax-player.size, 0)	
				pygame.draw.ellipse(screen, (50,50,50), ((player.rect.x,player.rect.y+25),(player.size,player.size)), 0)	
				if antialias:
					# this is a horrible way to antialias the player for now; it must be called twice to fill in all the gaps
					pygame.gfxdraw.aaellipse(screen, player.rect.x+(player.size/2), player.rect.y+(player.size/2)+25, player.rect.width/2 -1, player.rect.height/2 -1, (50,50,50))
					pygame.gfxdraw.aaellipse(screen, player.rect.x+(player.size/2-1), player.rect.y+(player.size/2-1)+25, player.rect.width/2 -1, player.rect.height/2 -1, (50,50,50))
	

			# update the player color
			player.updateColor(backgroundColor)

			# draw the main character
			pygame.draw.ellipse(screen, player.color, player.rect, 0)
			if antialias:	
				# this is a horrible way to antialias the player for now; it must be called twice to fill in all the gaps
				pygame.gfxdraw.aaellipse(screen, player.rect.x+(player.size/2), player.rect.y+(player.size/2), player.rect.width/2 -1, player.rect.height/2 -1, player.color)
				pygame.gfxdraw.aaellipse(screen, player.rect.x+(player.size/2-1), player.rect.y+(player.size/2-1), player.rect.width/2 -1, player.rect.height/2 -1, player.color)

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
				# exit if ESC key is pushed
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE:
						gameRunning = False
			#																		   #
			#-------------------------END: game input handling-------------------------#

			# iterate the number of skipped frames
			skippedBgFrames += 1

	pygame.mixer.music.stop()