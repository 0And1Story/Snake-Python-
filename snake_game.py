#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame
import os
from settings import Settings
from functions import Functions
from snake_body import SnakeBody
from food import Food

window_settings = Settings()
local_functions = Functions()

class SnakeGame():
    def __init__(self):
        self.snake = SnakeBody([[13, 12], [13, 13], [13, 14]])
        self.food = Food()

    def run_game(self):
        pygame.init()
        screen = pygame.display.set_mode((window_settings.screen_width, window_settings.screen_height))
        pygame.display.set_caption('Snake')
        local_functions.clear_device(screen)
        self.snake.draw_body(screen, self.food)
        pygame.MOVE_ON = pygame.USEREVENT + 1
        pygame.time.set_timer(pygame.MOVE_ON, 250)
        pygame.display.flip()

        while True:
            self.check_events(screen)
    
    def check_events(self, screen):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                os._exit(0)
            elif event.type == pygame.MOVE_ON:
                self.snake.move_on(screen, self.food)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.snake.direct = 2
                elif event.key == pygame.K_RIGHT:
                    self.snake.direct = 0
                elif event.key == pygame.K_UP:
                    self.snake.direct = 3
                elif event.key == pygame.K_DOWN:
                    self.snake.direct = 1
