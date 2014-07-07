# import libraries
import pygame
import os, time, math

# initializing pygame/pygame modules
pygame.init()

# imports ogg sound file
pygame.mixer.music.load(os.path.join('audio','death.beat.v1.wav'))
# plays music infinitly
pygame.mixer.music.play(-1)

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
pygame.display.set_caption('avoidr.v0.03')
# make a 3-tuple with the color white
background_colour = (255,255,255)

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

# player position
playerX = width/2
playerY = height/2

# the main game loop
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
	# player movement input
	keys = pygame.key.get_pressed()
	if keys[pygame.K_UP]:
		playerY = playerY - 1
	if keys[pygame.K_DOWN]:
		playerY = playerY + 1
	if keys[pygame.K_LEFT]:
		playerX = playerX - 1
	if keys[pygame.K_RIGHT]:
		playerX = playerX + 1
	time.sleep(0.005)
