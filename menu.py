# import libraries
import pygame
import os, time, math, random
from random import randint

class Menu():

	#def __init__(self, title, menuItems, inputSet, choiceSet):
	def __init__(self):
		self.menuClock = pygame.time.Clock()

		self.displayMenu = True

		self.titleFont = pygame.font.SysFont("monospace", 100)
		self.menuItemFont = pygame.font.SysFont("monospace", 27)

		self.exitGame = False
		# self.title = title
		# self.menuItems = menuItems
		# self.inputSet = inputSet
		# self.choiceSet = choiceSet
		# self.displayMenu = True


	def show(self, menuName):

		# initializing pygame/pygame modules
		pygame.init()
		pygame.display.init()

		# get information about the display
		# we only really care about the size of the display
		self.displayInfo = pygame.display.Info()
		self.width = self.displayInfo.current_w
		self.height = self.displayInfo.current_h

				# create a new window
		self.screen = pygame.display.set_mode((self.width, self.height),pygame.FULLSCREEN)
		pygame.display.set_caption('MENU')
		pygame.mouse.set_visible(False)

		self.displayMenu = True

		while self.displayMenu == True:

			# lock the loop at 5 fps
			self.menuClock.tick(5)

			# create three random r,g,b values
			bgR = randint(0,255)
			bgG = randint(0,255)
			bgB = randint(0,255)
			self.screen.fill((bgR,bgG,bgB))

			# render text
			mainTitle = self.titleFont.render("AVOIDR", 1, (255,255,255))
			self.screen.blit(mainTitle, (100, 60))
			menuItemText = self.menuItemFont.render("press spacebar to start", 1, (255,255,255))
			self.screen.blit(menuItemText, (100, 170))

			pygame.display.flip()

			for event in pygame.event.get():
				# exit if X button is pushed
				if event.type == pygame.QUIT:
					self.displayMenu = False
					pygame.mouse.set_visible(True)
					#pygame.display.quit()
					pygame.QUIT
					self.exitGame = True
				# exit if ESC key is pushed
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE:
						self.displayMenu = False
						pygame.mouse.set_visible(True)
						#pygame.display.quit()
					 	pygame.QUIT
					 	self.exitGame = True
					if event.key == pygame.K_SPACE:
						self.displayMenu = False
						#pygame.display.quit()
					 	pygame.QUIT

	def exitOrNot(self):
		return self.exitGame