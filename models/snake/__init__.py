import pygame

class Snake():
    def __init__(self, posX, posY, dir, square_size):
        self.posX = posX
        self.posY = posY
        self.dir = dir
        self.square_size = square_size
        self.tail = []
        self.tailGrow = False

    def draw(self, window):
        pygame.draw.rect(
            window, (0, 230, 0), pygame.Rect(self.posX * self.square_size, self.posY * self.square_size, self.square_size, self.square_size)
        )

        for i in range(len(self.tail)):
            pygame.draw.rect(
                window, (0, 230, 0), pygame.Rect(self.tail[i][0] * self.square_size, self.tail[i][1] * self.square_size, self.square_size, self.square_size)
            )

    def move(self):
        if len(self.tail) > 1:
            for i in range(len(self.tail) - 1, 0, -1):
                self.tail[i][0] = self.tail[i - 1][0]
                self.tail[i][1] = self.tail[i - 1][1]

        if len(self.tail) > 0:
            self.tail[0][0] = self.posX
            self.tail[0][1] = self.posY

        if self.dir == 'east':
            self.posX += 1
        elif self.dir == 'west':
            self.posX -= 1
        elif self.dir == 'north':
            self.posY -= 1
        else:
            self.posY += 1

    def checkFoodCollision(self, food):
        return self.posX == food.posX and self.posY == food.posY
    
    def checkForWallCollision(self, cols, rows):
        return self.posX <= -1 or self.posX >= cols + 1 or self.posY <= -1 or self.posY >= rows + 1

    def checkForSelfCollision(self):
        for pos in self.tail:
            if self.posX == pos[0] and self.posY == pos[1]:
                return True

        return False

    def grow(self):
        if len(self.tail) == 0:
            self.tail.append([self.posX, self.posY])
        else:
            self.tail.append([self.tail[len(self.tail) - 1][0], self.tail[len(self.tail) - 1][1]])