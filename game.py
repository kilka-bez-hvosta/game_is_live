import pygame


def update_all():
    matrixx = [[(x.state) for x in y] for y in matrix]
    neighbours = []
    for i in range(math):
        for j in range(matw):
            if i != 0 and j != 0 and i != math - 1 and j != matw-1:
                neighbours = (matrixx[i - 1][j - 1] + matrixx[i - 1][j] + matrixx[i - 1][j + 1] +
                              matrixx[i][j - 1] + matrixx[i][j + 1] + matrixx[i + 1][j - 1] + matrixx[i + 1][
                                  j] + matrixx[i + 1][j + 1])
                if neighbours not in [2, 3] and matrixx[i][j] == 1:
                    matrix[i][j].upd()
                elif neighbours == 3 and matrixx[i][j] == 0:
                    matrix[i][j].upd()
            elif j != 0 and i != math - 1 and j != matw-1:
                neighbours = (matrixx[i][j - 1] + matrixx[i][j + 1] + matrixx[i + 1][j - 1] + matrixx[i + 1][
                                  j] + matrixx[i + 1][j + 1])
                if neighbours not in [2, 3] and matrixx[i][j] == 1:
                    matrix[i][j].upd()
                elif neighbours == 3 and matrixx[i][j] == 0:
                    matrix[i][j].upd()
            elif i != 0 and i != math - 1 and j != matw - 1:
                neighbours = (matrixx[i - 1][j] + matrixx[i - 1][j + 1] +
                              matrixx[i][j + 1] + matrixx[i + 1][j] + matrixx[i + 1][j + 1])
                if neighbours not in [2, 3] and matrixx[i][j] == 1:
                    matrix[i][j].upd()
                elif neighbours == 3 and matrixx[i][j] == 0:

                    matrix[i][j].upd()
            elif i != math - 1 and j != matw-1:
                neighbours = (matrixx[i][j + 1] + matrixx[i + 1][j] + matrixx[i + 1][j + 1])
                if neighbours not in [2, 3] and matrixx[i][j] == 1:
                    matrix[i][j].upd()
                elif neighbours == 3 and matrixx[i][j] == 0:
                    matrix[i][j].upd()
            elif i != 0 and j != 0 and j != matw-1:
                neighbours = (matrixx[i - 1][j - 1] + matrixx[i - 1][j] + matrixx[i - 1][j + 1] +
                              matrixx[i][j - 1] + matrixx[i][j + 1])
                if neighbours not in [2, 3] and matrixx[i][j] == 1:
                    matrix[i][j].upd()
                elif neighbours == 3 and matrixx[i][j] == 0:
                    matrix[i][j].upd()
            elif i != 0 and j != 0 and i != math - 1:
                neighbours = (matrixx[i - 1][j - 1] + matrixx[i - 1][j] +
                              matrixx[i][j - 1] + matrixx[i + 1][j - 1] + matrixx[i + 1][j])
                if neighbours not in [2, 3] and matrixx[i][j] == 1:
                    matrix[i][j].upd()
                elif neighbours == 3 and matrixx[i][j] == 0:
                    matrix[i][j].upd()
            elif i != 0 and j != 0:
                neighbours = (matrixx[i - 1][j - 1] + matrixx[i - 1][j] +
                              matrixx[i][j - 1])
                if neighbours not in [2, 3] and matrixx[i][j] == 1:
                    matrix[i][j].upd()
                elif neighbours == 3 and matrixx[i][j] == 0:
                    matrix[i][j].upd()


def draw_text():
    text_list = ["ESC - выход;", "SPACE - пауза;", "Стрелки - движение;", "ПКМ - смена", "состояния клетки;",
                 "Все изменения", "возможны только", "в паузе."]
    for i in range(len(text_list)):
        text = myfont.render(text_list[i], False, (255, 255, 255))
        screen.blit(text, (w-250, 100 + i*50))


def move(arrow):
    if arrow == "right":
        for i in range(math):
            for j in range(matw - 1):
                matrix[i][j].state = matrix[i][j + 1].state
        matrix[i][-1].state = 0
    if arrow == "left":
        for i in range(math):
            for j in range(matw - 1, 0, -1):
                matrix[i][j].state = matrix[i][j - 1].state
        matrix[i][0].state = 0
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
        self.x = x
        self.y = y
        self.state = 0

    def upd(self):
        if self.state == 0:
            self.state = 1
        else:
            self.state = 0

    def draww(self):
        pygame.draw.rect(screen, (255, 255, 255), (self.x, self.y, 50, 50))
        if self.state == 0:
            pygame.draw.rect(screen, (0, 0, 25), (self.x + 5, self.y + 5, 40, 40))
        else:
            pygame.draw.rect(screen, (0, 0, 0), (self.x + 5, self.y + 5, 40, 40))
            pygame.draw.rect(screen, (255, 255, 255), (self.x + 10, self.y + 10, 30, 30))


pygame.init()
pygame.font.init()

myfont = pygame.font.SysFont('Comic Sans MS', 20)
w,h = pygame.display.Info().current_w, pygame.display.Info().current_h

screen = pygame.display.set_mode((w, h))
screen.fill((25, 0, 0))

running = True
pause = True

matw, math = (w - 300) // 50, (h - 200) // 50
matrix = [[Cell(50 + x*50, 100+y*50) for x in range(matw)] for y in range(math)]



while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
        if event.type == pygame.MOUSEBUTTONDOWN and pause:
            for j in matrix:
                for i in j:
                    if event.pos[0] in list(range(i.x, i.x + 50)) and event.pos[1] in list(range(i.y, i.y + 50)):
                        i.upd()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT and pause:
                move("right")
            if event.key == pygame.K_LEFT and pause:
                move("left")
            if event.key == pygame.K_UP and pause:
                move("up")
            if event.key == pygame.K_DOWN and pause:
                move("down")
            if event.key == pygame.K_ESCAPE:
                running = False
                break
            if event.key == pygame.K_SPACE:
                if pause:
                    pause = False
                else:
                    pause = True
    if not pause:
        update_all()
    screen.fill((25, 0, 0))
    for i in range(math):
        for j in range(matw):
            matrix[i][j].draww()
    if pause:
        text = myfont.render('Pause', False, (255, 255, 255))
        screen.blit(text, (15, 15))
    else:
        text = myfont.render('Live', False, (255, 255, 255))
        screen.blit(text, (15, 15))
    draw_text()
    pygame.display.flip()
    pygame.time.wait(100)

