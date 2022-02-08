from pprint import pprint


class Cell:
    def __init__(self, val, x, y, w, h) -> None:
        self.val = val
        self.next_val = val
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.pos = x, y

        self.neighbours = []

    def calculate_neighbours_pos(self, x, y) -> tuple:
        if x < 0:
            x = self.w - 1
        if y < 0:
            y = self.h - 1

        if x > self.w - 1:
            x = 0
        if y > self.h - 1:
            y = 0

        return x, y

    def find_neighbours(self, grid: list):
        x, y = self.x, self.y
        neighbours_coord = [
            self.calculate_neighbours_pos(x - 1, y - 1),  # 1
            self.calculate_neighbours_pos(x, y - 1),  # 2
            self.calculate_neighbours_pos(x + 1, y - 1),  # 3
            self.calculate_neighbours_pos(x + 1, y),  # 4
            self.calculate_neighbours_pos(x + 1, y + 1),  # 5
            self.calculate_neighbours_pos(x, y + 1),  # 6
            self.calculate_neighbours_pos(x - 1, y + 1),  # 7
            self.calculate_neighbours_pos(x - 1, y)  # 8
        ]
        for row in grid:
            for cell in row:
                if cell.pos in neighbours_coord:
                    self.neighbours.append(cell)

    def count_live_neighbours(self) -> int:
        count = 0
        for cell in self.neighbours:
            if cell.val == 1:
                count += 1
        return count

    def __str__(self) -> str:
        return f"{self.val}=({self.x},{self.y})"

    def __repr__(self) -> str:
        return f"{self.val}=({self.x},{self.y})"


if __name__ == '__main__':
    # Use __str__
    print(Cell(0, 1, 2, 100, 100))

    # Use __repr__
    data = [Cell(0, 1, 2, 100, 100)]
    pprint(data)
