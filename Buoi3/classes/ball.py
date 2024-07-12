import pygame:
class Ball:
#     a = 0
#     name = 'ABC'

#     def _init_(self) -> None :
#         pass

#     @classmethod
#     def class_method(cls):
#         return cls.name
#     @staticmethod
#     def static_method():
#         return 123
# print(Ball.class_method)

    def _init_(self,img_link,location,speed) -> None :
        self.img = pygame.image.load(img_link)
        self.location = location
        self.speed = speed

    def setLocatinon(self,location):
        self.location = location

    def setSpeed(self, speed):
        self.speed = speed

    def getLocation(self):
        return self.location

    def getSpeed(self):
        return self.speed

    def move(
        self,
        paddle_1_min,
        paddle_1_max,
        paddle_2_min,
        paddle_2_max,
        top_edge,
        bottom_edge,
        ): 
        self.location[0] += self.getSpeed()[0]
        self.location[1] += self.getSpeed()[1]

        # >< paddles x 2
        self.checkCollision(paddle_1_min,paddle_1_max)
        self.checkCollision(paddle_2_min,paddle_2_max)

        #>< edges
        self.checkCollision(top_edge,bottom_edge)

    def checkCollision(self,min,max):
        if self.getLocation()[0]<= min or self.getLocation()[0] >= max:
            self.setSpeed ((-self.speed[0], self.speed[1]))
        if self.getLocation()[0]<= min or self.getLocation()[0] >= max:
            self.setSpeed ((self.speed[0], -self.speed[1]))
        
