import pygame 
class Paddle:
    def _init_(self)  def _init_(self,img_link,location,speed: int , key_up,key_down) -> None:
        self.img = pygame.image.load(img_link)
        self.location = location
        self.speed = speed
        self.key_up = key_up
        self.key_down = key_down

    def setLocatinon(self,location):
        self.location = location

    def setKeyUp(self, key_up):
        self.key_up = key_up

    def setKeyDown(self, key_down):
        self.key_down = key_down

    def getKeyUp(self):
        return self.key_up

    def getKeyDown(self):
        return self.key_down
        
    def getLocation(self):
        return self.location

    def getSpeed(self):
        return self.speed
    
    def move(
        self,
        top_edge,
        bottom_edge,
    ): 
        if self.checkCollision(top_edge, bottom_edge):
            if self.key_up:
                self.location[1] -= self.speed
            if self.key_down:
                self.location[1] += self.speed
      

    def checkCollision(self,min,max):
        if self.location[1] <= min of self.location[1] >= max:
            return False
        return True
        