import pygame


def update_all():
    neighbours = []
    for i in range(math):
        for j in range(matw):
            if i != 0 and j != 0 and i != math - 1 and j != matw-1:
                neighbours = (matrix[i - 1][j - 1].state + matrix[i - 1][j].state + matrix[i - 1][j + 1].state +
                              matrix[i][j - 1].state + matrix[i][j + 1].state + matrix[i + 1][j - 1].state + matrix[i + 1][
                                  j].state + matrix[i + 1][j + 1].state)
                if neighbours not in [2, 3] and matrix[i][j].state == 1:
                    matrix[i][j].state = 0
                elif neighbours == 3 and matrix[i][j].state == 0:
                    matrix[i][j].state = 1
            elif j != 0 and i != math - 1 and j != matw-1:
                neighbours = (matrix[i][j - 1].state + matrix[i][j + 1].state + matrix[i + 1][j - 1].state + matrix[i + 1][
                                  j].state + matrix[i + 1][j + 1].state)
                if neighbours not in [2, 3] and matrix[i][j].state == 1:
                    matrix[i][j].state = 0
                elif neighbours == 3 and matrix[i][j].state == 0:
                    matrix[i][j].state = 1
            elif i != 0 and i != math - 1 and j != matw - 1:
                neighbours = (matrix[i - 1][j].state + matrix[i - 1][j + 1].state +
                              matrix[i][j + 1].state + matrix[i + 1][j].state + matrix[i + 1][j + 1].state)
                if neighbours not in [2, 3] and matrix[i][j].state == 1:
                    matrix[i][j].state = 0
                elif neighbours == 3 and matrix[i][j].state == 0:
                    matrix[i][j].state = 1
            if i != math - 1 and j != matw-1:
                neighbours = (matrix[i][j + 1].state + matrix[i + 1][j].state + matrix[i + 1][j + 1].state)
                if neighbours not in [2, 3] and matrix[i][j].state == 1:
                    matrix[i][j].state = 0
                elif neighbours == 3 and matrix[i][j].state == 0:
                    matrix[i][j].state = 1
            if i != 0 and j != 0 and j != matw-1:
                neighbours = (matrix[i - 1][j - 1].state + matrix[i - 1][j].state + matrix[i - 1][j + 1].state +
                              matrix[i][j - 1].state + matrix[i][j + 1].state)
                if neighbours not in [2, 3] and matrix[i][j].state == 1:
                    matrix[i][j].state = 0
                elif neighbours == 3 and matrix[i][j].state == 0:
                    matrix[i][j].state = 1
            if i != 0 and j != 0 and i != math - 1:
                neighbours = (matrix[i - 1][j - 1].state + matrix[i - 1][j].state +
                              matrix[i][j - 1].state + matrix[i + 1][j - 1].state + matrix[i + 1][j].state)
                if neighbours not in [2, 3] and matrix[i][j].state == 1:
                    matrix[i][j].state = 0
                elif neighbours == 3 and matrix[i][j].state == 0:
                    matrix[i][j].state = 1
            if i != 0 and j != 0:
                neighbours = (matrix[i - 1][j - 1].state + matrix[i - 1][j].state +
                              matrix[i][j - 1].state)
                if neighbours not in [2, 3] and matrix[i][j].state == 1:
                    matrix[i][j].state = 0
                elif neighbours == 3 and matrix[i][j].state == 0:
                    matrix[i][j].state = 1


def generate():
    matrix = [[0]*matw]*math
    for i in range(math):
        for j in range(matw):
            matrix[i][j] = Cell(50 + j * 50, 100 + i * 50)
    return matrix


def move(arrow):
    if arrow == "right":
        for i in range(math):
            for j in range(matw - 1):
                matrix[i][j].state = matrix[i][j + 1].state
        math[i][-1].state = 0
    if arrow == "left":
        for i in range(math):
            for j in range(matw - 1, 0, -1):
                matrix[i][j].state = matrix[i][j - 1].state
        math[i][0].state = 0
    if arrow == "down":
        for i in range(math - 1):
            for j in range(matw):
                matrix[i][j].state = matrix[i + 1][j].state
        for i in range(matw):
            matrix[-1][i].state = 0
    if arrow == "up":
        for i in range(math - 1, 0, -1):
            for j in range(matw):
                matrix[i][j].state = matrix[i - 1][j].state
        for i in range(matw):
            matrix[0][i].state = 0


class Cell(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(cells)
        self.x = x
        self.y = y
        self.state = 0

    def update(self):
        if self.state == 0:
            self.state = 1
        else:
            self.state = 0

    def draww(self):
        pygame.draw.rect(screen, (255, 255, 255), (self.x, self.y, self.x + 50, self.y + 50))
        if self.state == 0:
            pygame.draw.rect(screen, (0, 0, 0), (self.x + 5, self.y + 5, self.x + 45, self.y + 45))
        else:
            pygame.draw.rect(screen, (0, 0, 0), (self.x + 5, self.y + 5, self.x + 45, self.y + 45))
            pygame.draw.rect(screen, (255, 255, 255), (self.x + 10, self.y + 10, self.x + 40, self.y + 40))


pygame.init()
w,h = pygame.display.Info().current_w, pygame.display.Info().current_h
matw, math = (w - 100) // 50, (h - 200) // 50
screen = pygame.display.set_mode((w, h))
screen.fill((25, 0, 0))
running = True
cells = pygame.sprite.Group()
matrix = generate()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in cells:
                if event.pos[0] in list(range(i.x, i.x + 50)) and event.pos[1] in list(range(i.y, i.y + 50)):
                    i.update()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                move("right")
            if event.key == pygame.K_LEFT:
                move("left")
            if event.key == pygame.K_UP:
                move("up")
            if event.key == pygame.K_DOWN:
                move("down")
        update_all()
        for i in cells:
            i.draww()


