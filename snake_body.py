#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame
from settings import Settings
from functions import Functions

window_settings = Settings()
local_functions = Functions()

class SnakeBody():
    def __init__(self, __cp = []):
        self.snake = __cp
        self.dx = [ 1, 0,-1, 0]
        self.dy = [ 0, 1, 0,-1]
        self.direct = 3
    
    def move_on(self, screen, food):
        ns = [(self.snake[0][0]+self.dx[self.direct]) % window_settings.block_num, 
              (self.snake[0][1]+self.dy[self.direct]) % window_settings.block_num]
        self.snake.insert(0, ns)
        if (ns != food.get_position()):
            self.snake.pop()
        else:
            food.update_food()
        self.draw_body(screen, food)

    def draw_body(self, screen, food):
        local_functions.clear_device(screen)
        block = pygame.Surface((window_settings.block_size, window_settings.block_size))
        block.fill(window_settings.block_color)
        for body in self.snake:
            x, y = body
            screen.blit(block, local_functions.to_real_pos((x, y)))
        food.draw_food(screen)
        pygame.display.flip()
