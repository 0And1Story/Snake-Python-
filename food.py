#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame
import random
from settings import Settings
from functions import Functions

window_settings = Settings()
local_functions = Functions()

class Food():
    def __init__(self):
        self.update_food()
    
    def update_food(self):
        self.x = random.randint(0, window_settings.block_num - 1)
        self.y = random.randint(0, window_settings.block_num - 1)
    
    def draw_food(self, screen):
        block = pygame.Surface((window_settings.block_size, window_settings.block_size))
        block.fill(window_settings.food_color)
        screen.blit(block, local_functions.to_real_pos((self.x, self.y)))
        pygame.display.flip()
    
    def get_position(self):
        return [self.x, self.y]
