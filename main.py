import pygame
import random
import sqlite3

SCALE = 50
screen = None
cntmines = 10


class Board:  # Таблица
    def __init__(self, x_pos, y_pos, is_mine, opened=0):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.is_mine = is_mine
        self.opened = opened


class Minesweeper(Board):
    currcountmine = 0
    list = []
    listmine = []

    def __init__(self, width, height, countmine, x_pos=0, y_pos=0, is_mine=-1):
        super().__init__(x_pos, y_pos, is_mine)
        self.width = width
        self.height = height
        self.countmine = countmine
        global SCALE, screen
        i = (int)(width / SCALE)
        j = (int)(height / SCALE)
        j -= 1
        for index in range(countmine):
            self.listmine.append(random.randint(0, i * j))

        for index in range(i):
            for index2 in range(j):
                mine = -1
                self.currcountmine += 1
                if self.listmine.count(self.currcountmine) != 0 and (self.currcountmine != 0):
                    mine = 10

                self.list.append(Board(index * SCALE, SCALE + (index2 * SCALE), mine))

    def open_cell(self, pos, types):
        x = pos[0]
        y = pos[1]
        global screen, SCALE

        w, h = screen.get_size()
        cnt = 0

        if y >= SCALE:
            for index in range(len(self.list)):
                if self.list[index].is_mine != 10:
                    if ((self.list[index].x_pos < x) and
                            ((self.list[index].x_pos + SCALE) > x)
                            and (self.list[index].y_pos < y) and
                            ((self.list[index].y_pos + SCALE) > y)):
                        if types == 1:
                            if self.list[index].opened == 0:
                                flag = pygame.image.load('flag.jpg')
                                screen.blit(flag,
                                            (self.list[index].x_pos + 12,
                                             self.list[index].y_pos + 12))
                                self.list[index].opened = 1
                                cnt = -2
                            else:
                                cnt = -3
                                self.list[index].opened = 0
                                draw_point(screen, [0, 0, 0], [self.list[index].x_pos, self.list[index].y_pos])
                        else:
                            draw_point(screen, [0, 0, 255], [self.list[index].x_pos, self.list[index].y_pos])
                        pygame.draw.line(screen, [255, 255, 255],
                                         [self.list[index].x_pos, self.list[index].y_pos],
                                         [self.list[index].x_pos, self.list[index].y_pos + SCALE])
                        pygame.draw.line(screen, [255, 255, 255],
                                         [self.list[index].x_pos, self.list[index].y_pos],
                                         [self.list[index].x_pos + SCALE, self.list[index].y_pos])
                        break
                if self.list[index].is_mine == 10:
                    if ((self.list[index].x_pos < x) and
                            ((self.list[index].x_pos + SCALE) > x)
                            and (self.list[index].y_pos < y) and
                            ((self.list[index].y_pos + SCALE) > y)):
                        if types == 1:
                            if self.list[index].opened == 0:
                                flag = pygame.image.load('flag.jpg')
                                screen.blit(flag, (self.list[index].x_pos + 12, self.list[index].y_pos + 12))
                                self.list[index].opened = 1
                                cnt = -2
                            else:
                                cnt = -3
                                self.list[index].opened = 0
                                draw_point(screen, [0, 0, 0],
                                           [self.list[index].x_pos, self.list[index].y_pos])
                        else:
                            flag = pygame.image.load('mines.jpg')
                            screen.blit(flag, (self.list[index].x_pos + 12, self.list[index].y_pos + 12))
                            cnt = -1
                        pygame.draw.line(screen, [255, 255, 255],
                                         [self.list[index].x_pos, self.list[index].y_pos],
                                         [self.list[index].x_pos, self.list[index].y_pos + SCALE])
                        pygame.draw.line(screen, [255, 255, 255],
                                         [ self.list[index].x_pos, self.list[index].y_pos],
                                         [ self.list[index].x_pos + SCALE, self.list[index].y_pos])
                        break

                    if ((self.list[index].x_pos < (x - SCALE)) and
                            ((self.list[index].x_pos + SCALE) > (x - SCALE))
                            and (self.list[index].y_pos < (y - SCALE)) and
                            ((self.list[index].y_pos + SCALE) > (y - SCALE))):
                        cnt += 1
                    if ((self.list[index].x_pos < (x - SCALE)) and
                            ((self.list[index].x_pos + SCALE) > (x - SCALE))
                            and (self.list[index].y_pos < y) and
                            ((self.list[index].y_pos + SCALE) > y)):
                        cnt += 1
                    if ((self.list[index].x_pos < (x - SCALE)) and
                            ((self.list[index].x_pos + SCALE) > (x - SCALE))
                            and (self.list[index].y_pos < (y + SCALE)) and
                            ((self.list[index].y_pos + SCALE) > (y + SCALE))):
                        cnt += 1
                    if ((self.list[index].x_pos < x) and
                            ((self.list[index].x_pos + SCALE) > x)
                            and (self.list[index].y_pos < (y - SCALE)) and
                            ((self.list[index].y_pos + SCALE) > (y - SCALE))):
                        cnt += 1
                    if ((self.list[index].x_pos < x) and
                            ((self.list[index].x_pos + SCALE) > x)
                            and (self.list[index].y_pos < (y + SCALE)) and
                            ((self.list[index].y_pos + SCALE) > (y + SCALE))):
                        cnt += 1
                    if ((self.list[index].x_pos < (x + SCALE)) and
                            ((self.list[index].x_pos + SCALE) > (x + SCALE))
                            and (self.list[index].y_pos < (y - SCALE)) and
                            ((self.list[index].y_pos + SCALE) > (y - SCALE))):
                        cnt += 1
                    if ((self.list[index].x_pos < (x + SCALE)) and
                            ((self.list[index].x_pos + SCALE) > (x + SCALE))
                            and (self.list[index].y_pos < y) and
                            ((self.list[index].y_pos + SCALE) > y)):
                        cnt += 1
                    if ((self.list[index].x_pos < (x + SCALE)) and
                            ((self.list[index].x_pos + SCALE) > (x + SCALE))
                            and (self.list[index].y_pos < (y + SCALE)) and
                            ((self.list[index].y_pos + SCALE) > (y + SCALE))):
                        cnt += 1

            if cnt > 0 and types == 0:
                x0 = 0
                y0 = 0
                for index in range(len(self.list)):
                    if (self.list[index].x_pos <= pos[0] <= self.list[index].x_pos + SCALE and
                            self.list[index].y_pos <= pos[1] <= self.list[index].y_pos + SCALE):
                        x0 = self.list[index].x_pos
                        y0 = self.list[index].y_pos

                        fontObj = pygame.font.Font('freesansbold.ttf', 26)
                        textSurfaceObj = fontObj.render(str(cnt), True, (255, 255, 255), (0, 0, 0))
                        textRectObj = textSurfaceObj.get_rect()
                        textRectObj.center = [x0 + (SCALE / 2), y0 + (SCALE / 2)]
                        screen.blit(textSurfaceObj, textRectObj)
            else:
                if cnt == 0 and types == 0:
                    if (x - SCALE) > 0:
                        self.open_cell([x - SCALE, y], 0)
                    if (y - SCALE) > 0:
                        self.open_cell([x, y - SCALE], 0)
                    # if (x - SCALE) > 0 and (y - SCALE) > 0:
                    #     self.open_cell([x - SCALE, y - SCALE], 0)
                    # if (x - SCALE) > 0 and (y + SCALE) < h:
                    #     self.open_cell([x - SCALE, y + SCALE], 0)
                    # if (y - SCALE) > 0 and (x + SCALE) < w:
                    #     self.open_cell([x + SCALE, y - SCALE], 0)
                    # if (x + SCALE) < w:
                    #     self.open_cell([x + SCALE, y], 0)
                    # if (y + SCALE) < h:
                    #     self.open_cell([x, y + SCALE], 0)
                    # if (y + SCALE) < h and (x + SCALE) < w:
                    #     self.open_cell([x + SCALE, y + SCALE], 0)

        return cnt


def set_mode(size, bcolor=None):
    if bcolor is None:
        bcolor = [200, 200, 200]
    global SCALE, screen
    screen = pygame.display.set_mode([size[0], size[1]])
    for i in range(0, size[0]):
        pygame.draw.line(screen, bcolor, [i * SCALE, SCALE], [i * SCALE, size[1] * SCALE])
    for i in range(1, size[1]):
        pygame.draw.line(screen, bcolor, [0, i * SCALE], [size[0] * SCALE, i * SCALE])
    return screen


def fill(screen_color, bcolor=None):
    if bcolor is None:
        bcolor = [255, 255, 255]
    global screen
    surface = screen
    surface.fill(screen_color)
    w, h = surface.get_size()
    for i in range(0, w):
        pygame.draw.line(surface, bcolor, [i * SCALE, 0], [i * SCALE, h * SCALE])
    for i in range(0, h):
        pygame.draw.line(surface, bcolor, [0, i * SCALE], [w * SCALE, i * SCALE])


def draw_point(surface, color, pos):
    return pygame.draw.rect(surface, color, [pos[0], pos[1], SCALE, SCALE ])


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Cапёр')
    size = width, height = 350, 450
    screen = set_mode(size)
    colored = [255, 0, 0]
    coord = [0, 0]
    cntorigmines = cntmines
    clock = pygame.time.Clock()
    mines = Minesweeper(350, 450, 10)
    v = 10  # пикселей в секунду
    x_pos = 0  # Текущая позиция центра круга
    cnt = 0
    running = True
    while running:
        for event in pygame.event.get():  # Берём событие
            if event.type == pygame.QUIT:  # Если событие выход, тогда завершаем
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:  # Если событие нажали кнопку мыши
                if event.button == 3 and cntmines > 0:
                    pos = event.pos
                    if cnt >= 0:
                        cnt = mines.open_cell(pos, 1)
                        if cnt == -1 or cnt == -2:
                            if cnt == -1:
                                cntorigmines -= 1
                            cntmines -= 1
                            cnt = 0
                        else:
                            if cnt == -3:
                                cntmines += 1
                                cnt = 0

                if event.button == 1:
                    pos = event.pos  # Текущая позиция там где нажали кнопку
                    if ((pos[0] < 200) and (pos[0] > 150) and (pos[1] < 50)):
                        cntmines = 10
                        screen = set_mode(size)
                        cnt = 0
                    else:
                        if cnt >= 0:
                            cnt = mines.open_cell(pos, 0)

        clock.tick()
        if cntmines > 0 and cnt >= 0:
            fontObj = pygame.font.Font('freesansbold.ttf', 26)
            texst = pygame.time.get_ticks() // 1000
            textSurfaceObj = fontObj.render(str(texst), True, (255, 255, 255), (0, 0, 0))
            textRectObj = textSurfaceObj.get_rect()
            textRectObj.center = [30, 25]
            screen.blit(textSurfaceObj, textRectObj)

        fontObj = pygame.font.Font('freesansbold.ttf', 26)
        texst = " " + str(cntmines) + " "
        textSurfaceObj = fontObj.render(str(texst), True, (255, 255, 255), (0, 0, 0))
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = [330, 25]
        screen.blit(textSurfaceObj, textRectObj)

        fontObj = pygame.font.Font('freesansbold.ttf', 26)
        texst = " " + str(cntmines) + " "
        textSurfaceObj = fontObj.render(str(texst), True, (255, 255, 255), (0, 0, 0))
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = [330, 25]
        screen.blit(textSurfaceObj, textRectObj)
        dog_surf = pygame.image.load('smilenone.jpg')
        if cntorigmines == 0:
            dog_surf = pygame.image.load('smileok.jpg')
            conn = sqlite3.connect("mydatabase.db")  # Подключаемся к базе данных
            cursor = conn.cursor()  # Получаем курсор
            texst = pygame.time.get_ticks() // 1000
            cursor.execute("INSERT INTO saper "
                           " VALUES(1,"+str(texst)+") ")  # Выполняем запрос на получение данных
            conn.commit()
        if (cnt < 0) or (cntorigmines != 0 and cntmines == 0):
            dog_surf = pygame.image.load('smilebad.jpg')
        screen.blit(dog_surf, (162, 12))

        pygame.display.flip()
