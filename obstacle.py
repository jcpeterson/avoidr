from random import randint

class Obstacle:

   # common base class for obstacles

   # counter for how many obstacle instances have been created
   count = 0

   def __init__(self, screenWidth, screenHeight):

      # the width/height of the screen is te range that the x/y position can vary
      self.posRangeX = screenWidth
      self.posRangeY = screenHeight

      # generate a random starting position for the obstacle
      self.posX = randint(1,self.posRangeX)
      self.posY = randint(1,self.posRangeY)

      # make sure the obstacles don't start too close to the player
      wiggleRoom = 200 # standardize later!
      while (self.posX in range((self.posRangeX/2) - wiggleRoom,(self.posRangeX/2) + wiggleRoom)) or \
               (self.posY in range((self.posRangeY/2) - wiggleRoom,(self.posRangeY/2) + wiggleRoom)):
         self.posX = randint(1,self.posRangeX)
         self.posY = randint(1,self.posRangeY)
      
      # generate a random starting direction for the obstacle
      # the direction can either be 1 or -1 (right or left)
      # this is because -1 * speed results in left motion
      self.dirX = randint(-1,1)
      self.dirY = randint(-1,1)
      # we don't want any zeros 
      while self.dirX == 0 or self.dirY == 0:
         self.dirX = randint(-1,1)
         self.dirY = randint(-1,1)

      # generate a random starting size for the obstacle
      self.sizeMin = 5
      self.sizeMax = 40
      self.size = randint(self.sizeMin,self.sizeMax)

      # generate a random speed for the obstacle
      self.speedMin = 1
      self.speedMax = 4
      self.speed = randint(self.speedMin,self.speedMax)

      # one (more) obstacle instance has been made
      Obstacle.count += 1

   # update the position of the player
   def updatePos(self):

      if self.posX >= self.posRangeX - self.size or self.posX <= 0:
         self.dirX *= -1

      if self.posY >= self.posRangeY - self.size or self.posY <= 0:
         self.dirY *= -1

      # the objects new position is its current position plus its (direction (-1 or 1) * its speed (number of pixels to move))
      self.posX = self.posX + (self.dirX * self.speed)

      # the objects new position is its current position plus its (direction (-1 or 1) * its speed (number of pixels to move))
      self.posY = self.posY + (self.dirY * self.speed)

   # THESE SET-GET FUNCTIONS ARE NOT BEING USED YET!!!
   # def getPosX(self):
   #   return self.posX

   # def setPosX(self, posX):
   #   self.posX = posX

   # def getPosY(self):
   #   return self.posY

   # def setPosY(self):
   #   self.posY = posY
