import pygame

class Grid():
    def __init__(self, window, width, height, square_size):
        self.cols = int(height / square_size)
        self.rows = int(width / square_size)
        self.window = window
        self.square_size = square_size

    def draw(self, snake, food):
        self.window.fill((0, 0, 0))

        for i in range(1, self.cols):
            pygame.draw.line(self.window, (78, 78, 78), (i * self.square_size, 0), (i * self.square_size, self.cols * self.square_size))

        for i in range(1, self.rows):
            pygame.draw.line(self.window, (78, 78, 78), (0, i * self.square_size), (self.rows * self.square_size, i * self.square_size))

        snake.draw(self.window)
        food.draw(self.window)