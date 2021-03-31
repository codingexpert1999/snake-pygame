# General Imports
import pygame
import sys

# Model Classes
from models.snake import Snake
from models.food import Food
from models.grid import Grid
from models.menu import Menu

# Constants
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
SQUARE_SIZE = 25

# Initial Variables
snake_pos_x = 10
snake_pos_y = 10
snake_dir = 'east'

# Game variables
gameOver = False
gameStarted = False
score = 0
highscore = 0

pygame.init()

pygame.display.set_caption("Snake Game")
window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

grid = Grid(window, SCREEN_WIDTH, SCREEN_HEIGHT, SQUARE_SIZE)
snake = Snake(snake_pos_x, snake_pos_y, snake_dir, SQUARE_SIZE)
food = Food(15, 15, SCREEN_WIDTH / SQUARE_SIZE,
            SCREEN_HEIGHT / SQUARE_SIZE, SQUARE_SIZE)
menu = Menu(window, SCREEN_WIDTH, SCREEN_HEIGHT)

clock = pygame.time.Clock()

while True:
    pygame.time.delay(40)
    clock.tick(10)

    if gameStarted == False:
        menu.draw(score, highscore)

    if gameOver == False and gameStarted:
        grid.draw(snake, food)

        snake.move()

        if snake.checkForWallCollision(grid.cols, grid.rows) or snake.checkForSelfCollision():
            gameOver = True

        if snake.checkFoodCollision(food):
            food.eaten = True
            snake.grow()
            score += 1

        if gameOver:
            gameStarted = False

            if score > highscore:
                highscore = score

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if gameStarted and gameOver == False:
                if event.key == pygame.K_UP:
                    if snake.dir != 'south':
                        snake.dir = 'north'
                if event.key == pygame.K_DOWN:
                    if snake.dir != 'north':
                        snake.dir = 'south'
                if event.key == pygame.K_RIGHT:
                    if snake.dir != 'west':
                        snake.dir = 'east'
                if event.key == pygame.K_LEFT:
                    if snake.dir != 'east':
                        snake.dir = 'west'

            if gameStarted == False:
                if event.key == pygame.K_SPACE:
                    gameStarted = True

                    if gameOver:
                        gameOver = False
                        score = 0
                        snake = Snake(snake_pos_x, snake_pos_y,
                                      snake_dir, SQUARE_SIZE)
                        food.placeRandom()

    pygame.display.update()
