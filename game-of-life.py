import pygame
from pygame.locals import *
import random
from cell import Cell

from pprint import pprint as pp

from utils import _time


class GameOfLife:

    def __init__(self,
                 width: int = 640,
                 height: int = 480,
                 cell_size: int = 10,
                 speed: int = 10) -> None:
        self.width = width
        self.height = height
        self.cell_size = cell_size

        self.screen_size = width, height

        self.screen = pygame.display.set_mode(self.screen_size)
        self.cell_width = self.width // self.cell_size
        self.cell_height = self.height // self.cell_size

        self.speed = speed

        self.mouse_down = False
        self.pause = False

    def draw_lines(self) -> None:
        for x in range(0, self.width, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color('black'),
                             (x, 0), (x, self.height))

        for y in range(0, self.height, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color('black'),
                             (0, y), (self.width, y))

    def run(self) -> None:
        pygame.init()
        clock = pygame.time.Clock()
        pygame.display.set_caption('Game of Life')
        self.screen.fill(pygame.Color('white'))
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                    elif event.key == K_SPACE:
                        self.pause = not self.pause
                elif event.type == pygame.MOUSEMOTION:
                    self.check_mouse_motion_event(event)
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.check_mouse_button_event(True)
                elif event.type == pygame.MOUSEBUTTONUP:
                    self.check_mouse_button_event(False)

            if not self.pause:
                self.draw_grid()
                self.draw_lines()
                self.get_next_generation()

            pygame.display.flip()
            clock.tick(self.speed)
        pygame.quit()

    def check_mouse_motion_event(self, event):
        if self.mouse_down:
            mouse_pos = event.pos
            self._check_cell_focus(mouse_pos)

    def check_mouse_button_event(self, down):
        self.mouse_down = down
        if self.mouse_down:
            mouse_pos = pygame.mouse.get_pos()
            self._check_cell_focus(mouse_pos)

    def _check_cell_focus(self, mouse_pos):
        # TODO
        pass

    # Time  18.247326
    @_time
    def create_grid(self, randomazie: bool = False) -> list:
        grid = []

        # Create greed
        for y in range(0, self.cell_height):
            row = []
            for x in range(0, self.cell_width):
                if randomazie:
                    value = random.randint(0, 1)
                else:
                    value = 0
                row.append(Cell(value, x, y, self.cell_width, self.cell_height))
            grid.append(row)
        # Find neighbours for all cells
        for row in grid:
            for cell in row:
                cell.find_neighbours(grid)

        return grid

    def draw_grid(self):
        for row in grid:
            for cell in row:
                if cell.val == 1:
                    color = Color(20, 120, 0)
                else:
                    color = Color(255, 255, 255)
                x = cell.x * self.cell_size
                y = cell.y * self.cell_size
                pygame.draw.rect(self.screen, color,
                                 (x, y, self.cell_size, self.cell_size))

    def get_next_generation(self):
        for row in grid:
            for cell in row:
                count_live_neighbours = cell.count_live_neighbours()
                if cell.val == 1:
                    if count_live_neighbours < 2 or count_live_neighbours > 3:
                        cell.next_val = 0
                else:
                    if count_live_neighbours == 3:
                        cell.next_val = 1

        count_live = 0
        count_empty = 0
        for row in grid:
            for cell in row:
                cell.val = cell.next_val
                if cell.val == 1:
                    count_live += 1
                else:
                    count_empty += 1

        print(f"Live: {count_live} Empty: {count_empty}")


if __name__ == '__main__':
    # 65
    # 80
    seed_id = random.randint(1, 100)
    print(f"Seed: {seed_id}")
    random.seed(seed_id)
    game = GameOfLife(1280, 740, 20, 10)
    grid = game.create_grid(randomazie=True)
    # pp(grid)
    game.run()
