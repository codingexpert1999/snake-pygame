import pygame
import random

class Food():
    def __init__(self, posX, posY, grid_cols, grid_rows, square_size):
        self.posX = posX
        self.posY = posY
        self.grid_cols = grid_cols
        self.grid_rows = grid_rows
        self.square_size = square_size
        self.eaten = False

    def placeRandom(self):
        self.posX = random.randint(0, self.grid_rows - 1)
        self.posY = random.randint(0, self.grid_cols - 1)

    def draw(self, window):
        if self.eaten:
            self.eaten = False
            self.placeRandom()

        pygame.draw.rect(window, (230, 0, 0), pygame.Rect(self.posX * self.square_size, self.posY * self.square_size, self.square_size, self.square_size))
