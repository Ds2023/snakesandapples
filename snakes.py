import pygame
from pygame.locals import *
def draw_block():
    surface. fill((252,186,3))#moves to constructor class
    surface.blit(block, (block_x,block_y))
    pygame.display.flip()

if __name__ =="__main__"
    pygame.init()

    surface = pygame.display.set_mode((1000,600))
    surface.fill(252,186,3))
    default_size = (25,25)
    block = pygame.image.load("")
    block = pygame.transform.scale(block, default _size)
    block_x = 10
    block_y = 10
    surface.blit(block,(block_x,block_y))

    pygame.display.flip()

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                if event.key == K_UP:
                    block_y =  block _y -10
                    draw_block()
                 if event.key == K_DOWN:
                    block_y =  block _y + 10
                    draw_block()
                 if event.key == K_RIGHT:
                    block_x=  block _x +10
                    draw_block()
                 if event.key == K_LEFT:
                    block_x=  block _x -10
                    draw_block()
            elif event.type == QUIT:
                 running = False
