#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame
from settings import Settings

window_settings = Settings()

class Functions():
    def to_real_pos(self, block = (0, 0)):
        return (block[0] * window_settings.block_size + window_settings.block_start, block[1] * window_settings.block_size + window_settings.block_start)
    
    def clear_device(self, screen):
        screen.fill(window_settings.bd_color)
        surf = pygame.Surface((window_settings.block_size * window_settings.block_num, window_settings.block_size * window_settings.block_num))
        surf.fill(window_settings.bg_color)
        screen.blit(surf, (window_settings.block_start, window_settings.block_start))
