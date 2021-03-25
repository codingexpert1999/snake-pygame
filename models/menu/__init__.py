import pygame

class Menu():
    def __init__(self, window, screen_width, screen_height):
        self.window = window
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.pressKeyFont = pygame.font.Font("freesansbold.ttf", 25)
        self.scoreFont = pygame.font.Font("freesansbold.ttf", 18)

        self.draw(0, 0)

    def draw(self, score, highscore):
        self.window.fill((0, 0, 0))

        pressKeyText = self.pressKeyFont.render("PRESS SPACE TO START THE GAME", True, (255, 255, 255))
        self.window.blit(pressKeyText, (
            (self.screen_width / 2) - (pressKeyText.get_width() / 2), (self.screen_height / 2) - 50)
            )

        scoreText = self.scoreFont.render("Score : " + str(score), True, (255, 255, 255))
        self.window.blit(scoreText, (125, (self.screen_height / 2) + 50))

        highscoreText = self.scoreFont.render("Highscore : " + str(highscore), True, (255, 255, 255))
        self.window.blit(highscoreText, (275, (self.screen_height / 2) + 50))