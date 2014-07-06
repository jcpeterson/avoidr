# import libraries
import pygame
import time, math

# size of the window
(width, height) = (800, 600)

# create a new black window
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('avoidr.v0.01')
background_colour = (0,0,0)
screen.fill(background_colour)

running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

#This is Connor.
