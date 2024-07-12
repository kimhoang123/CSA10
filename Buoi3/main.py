import pygame
from classes.ball import Ball
from classes.paddle import Paddle
class Main:

    def _init_(
        self,
        size, 
        background, 
        title, 
        ball_location, 
        ball:Ball,
        paddle_1: Paddle,
        paddle_2: Paddle,
    ) -> None:
        # khai bao man choi
        pygame.init()
        self.size = size
        self.background = background
        self.title = title
        pygame.display.set_caption(self.title)
        self.canvas = pygame.display.set=mode(size=self.size)
        global clock
        self.clock = pygame.time.Clock()

        #khai bao obj can cho man choi
        self.ball = ball
        self.paddle_1 = paddle_1
        self.paddle_2 = paddle_2

    def run(self):
        while True:  # play game
            events = pygame.event.get()  # bat su kien
            for e in events:
                # quit
                if e.type == pygame.QUIT:
                    return
                # keyboard check
                elif e.type == pygame.KEYDOWN:  # nhan phim
                    if e.key == pygame.K_w:
                        self.player.setKeyUp1(True)
                    elif e.key == pygame.K_s:
                        self.player.setKeyDown1(True)
                    elif e.key == pygame.K_UP:
                        self.player.setKeyUp2(True)
                    elif e.key == pygame.K_DOWN:
                        self.player.setKeyDown2(True)

                elif e.type == pygame.KEYUP:  # khong nhan phim
                    if e.key == pygame.K_w:
                        self.player.setKeyUp1(False)
                    elif e.key == pygame.K_s:
                        self.player.setKeyDown1(False)
                    elif e.key == pygame.K_UP:
                        self.player.setKeyUp2(False)
                    elif e.key == pygame.K_DOWN:
                        self.player.setKeyDown2(False)
            self.ball.move(
                paddle_1_max=self.paddle_1.getLocation()[1] + 120,
                paddle_1_min=self.paddle_1.getLocation()[1],
                paddle_2_max=self.paddle_2.getLocation()[1] + 120,
                paddle_2_min=self.paddle_2.getLocation()[1],
                top_edge=0,
                bottom_edge=480,
            )
                
                self.paddle_1.move(top_edge=0,bottom_edge=480)
                self.paddle_2.move(top_edge=0,bottom_edge=480)
    def drawCanvas(self);
        pass
     # show canvas
            self.canvas.fill(self.bg)
            self.canvas.blit(self.ball.img_url, (self.ball.getX(), self.ball.getY()))
            self.canvas.blit(
                self.paddle_1.img, (self.paddle_1.getX(), self.paddle_1.getY())
            )
            self.canvas.blit(
                self.paddle_2.img, (self.paddle_2.getX(), self.paddle_2.getY())
            )
            self.clock.tick(60)
            pygame.display.flip()


# Driver code
main = Main(
    title="Ping Pong",
    size=(600, 600),
    bg=(252, 16, 140),
    ball_img_link="Buoi3\\assets\\ball.png",
    paddle_img_link="Buoi3\\assets\\paddle.png",
    ball_location=(285, 300),
    ball_speed=(1.5, 3.5),
    paddle_1_location=(0, 250),
    paddle_2_location=(570, 250),
)
main.run()