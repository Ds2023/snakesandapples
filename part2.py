import pygame
from pygame.locals import * #helps us import global variables ie keydown etc

class Snake:#will have the block obj to makeup the snake
    def __init__(self,parent_screen):
        self.parent_screen = parent_screen
        self.block = pygame.image.load("/Users/victor/Downloads/box.png").convert()
        self.x = 10
        self.y = 10


    def draw(self):
        self.parent_screen.fill((252, 186, 3)) #moves to constructor class #erase surface before drawing to prevent overlap
        self.parent_screen.blit(self.block,(self.x,self.y))
        pygame.display.flip()

    def move_left(self):
        self.x -= 10
        self.draw()

    def move_right(self):
        self.x += 10
        self.draw()

    def move_up(self):
        self.y -= 10
        self.draw()

    def move_down(self):
        self.y += 10
        self.draw()

    

class Game:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((1000,600))
        self.surface.fill((252, 186, 3)) #since the snake is part of the game and the game class is our main function
        self.snake = Snake(self.surface)
        self.snake.draw()


    def run(self):

        running = True
        while running:
            for event in pygame.event.get():
                if event.type  == KEYDOWN:
                    #press the esc key on the keyboard
                    if event.key == K_ESCAPE:
                        running = False
                    #moving the block up #moving along the y axis
                    if event.key == K_UP:                    
                        self.snake.move_up()
                        # function to draw the ball
                    #moving along the y axis
                    if event.key == K_DOWN:                   
                        self.snake.move_down()
                    #moving along the X axis(RIGHT)
                    if event.key == K_RIGHT:                   
                        self.snake.move_right()
                    #moving along the X axis(LEFT)
                    if event.key == K_LEFT:                   
                        self.snake.move_left()
                #hit quit on cancel button on the window  
                elif event.type == QUIT:
                    running = False
        



if __name__ == "__main__":
    game = Game()
    game.run() 