import random
import pygame


class Object:
    def __init__(self, main_screen, screen_size_x, screen_size_y):
        self.screen = main_screen
        self.s_x = screen_size_x
        self.s_y = screen_size_y
