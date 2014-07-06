# import libraries
import pygame
import time, math

# size of the window in pixels
# this should be automatic in the future
width = 800
height = 600

# create a new window
screen = pygame.display.set_mode((width, height))
# set the window caption
pygame.display.set_caption('avoidr.v0.02')
# make a 3-tuple with the color white
background_colour = (255,255,255)
# fill the screen with the background color
screen.fill(background_colour)
# draw the current frame
pygame.display.flip()
# player position
playerX = 400
playerY = 300
# the main game loop
gameRunning = True
while gameRunning:
	# fill the screen with the background color
	screen.fill(background_colour)
	# draw the main character
	pygame.draw.circle(screen, (0,0,0), (playerX, playerY), 25, 0)
	pygame.display.flip()
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
			# if event.key == pygame.K_UP:
			# 	playerY = playerY - 10
			# if event.key == pygame.K_DOWN:
			# 	playerY = playerY + 10
			# if event.key == pygame.K_LEFT:
			# 	playerX = playerX - 10
			# if event.key == pygame.K_RIGHT:
			# 	playerX = playerX + 10
	keys = pygame.key.get_pressed()
	if keys[pygame.K_UP]:
		playerY = playerY - 1
	if keys[pygame.K_DOWN]:
		playerY = playerY + 1
	if keys[pygame.K_LEFT]:
		playerX = playerX - 1
	if keys[pygame.K_RIGHT]:
		playerX = playerX + 1
	time.sleep(0.01)
