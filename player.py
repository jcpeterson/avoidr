import pygame, os

class Player:

   # this takes in screen width/height to calculate the player's starting position (center of screen)
   # it also takes in the background color to compute its own color (inverted background color)
   def __init__(self, screenWidth, screenHeight):

      self.posRangeX = screenWidth
      self.posRangeY = screenHeight

      self.posX = screenWidth/2
      self.posY = screenHeight/2

      self.speed = 10

      self.sizeMax = 80
      self.sizeMin = 42#40
      # might as well start out at the minimum size
      self.size = self.sizeMin

      self.state = 'growing'

      # make the player color white; it doesn't really matter how it starts
      self.color = (255,255,255)

      self.isJumping = False
      self.goingUp = True

      self.killed = False
      self.exploding = False

      self.rect = pygame.Rect((self.posX,self.posY),(self.size,self.size))

      # load the jump sound
      self.jumpSound = pygame.mixer.Sound(os.path.join('audio','jump.wav'))

   def updateSize(self):

      # # player size changes
      # if self.state == 'growing' and self.size >= self.sizeMin:
      #    self.size += 1
      #    if self.size >= self.sizeMax:
      #       self.state = 'shrinking'

      # if self.state == 'shrinking' and self.size <= self.sizeMax:
      #    self.size -= 1
      #    if self.size <= self.sizeMin:
      #       self.state = 'growing'

      if self.isJumping:
         self.speed = 3
         # player size changes when jumpin
         if self.goingUp:
            self.size += 1
            if self.size == self.sizeMax:
               self.goingUp = False
         if not self.goingUp:
            self.size -= 1
            if self.size == self.sizeMin:
               self.isJumping = False
               self.goingUp = True
               self.speed = 10

      self.rect.width = self.size
      self.rect.height = self.size

      # sounds/animations for this have not been implemented yet
      if self.killed:
         self.exploding = True

   def updatePos(self, keys):

      # left border collision detection
      if (self.posX != 0 + self.sizeMax) and (self.posX > 0 + self.sizeMax + 5):
         # player movement input
         if keys[pygame.K_LEFT]:
            self.posX = self.posX - self.speed
      # right border collision detection
      if (self.posX != self.posRangeX - self.sizeMax) and (self.posX < self.posRangeX - (self.sizeMax + 5)):
         # player movement input
         if keys[pygame.K_RIGHT]:
            self.posX = self.posX + self.speed 
      # vertical border collision detection
      if (self.posY != 0 + self.sizeMax) and (self.posY > 0 + self.sizeMax + 5):
         # player movement input
         if keys[pygame.K_UP]:
            self.posY = self.posY - self.speed
      # vertical border collision detection
      if (self.posY != self.posRangeY - self.sizeMax) and (self.posY < self.posRangeY - (self.sizeMax + 5)):
         # player movement input
         if keys[pygame.K_DOWN]:
            self.posY = self.posY + self.speed
         # MOVE THIS OVER TO THE SIZE FUNCTION SOON!!!
         if keys[pygame.K_SPACE]:
            if not self.isJumping:
               # play the jump sound
               self.jumpSound.play()
               self.isJumping = True

      self.rect.x = self.posX
      self.rect.y = self.posY

      # use something like this for input handling later
      # for e in pygame.event.get():
      #    if e.type == QUIT: raise SystemExit, "QUIT"
      #    if e.type == KEYDOWN and e.key == K_ESCAPE:
      #       raise SystemExit, "ESCAPE"

      # pressed = pygame.key.get_pressed()
      # up, left, right = [pressed[key] for key in (K_UP, K_LEFT, K_RIGHT)]

   def updateColor(self,gameBgColor):
      # update the player color with the inverted current background color
      self.color = (255-gameBgColor[0],255-gameBgColor[1],255-gameBgColor[2])