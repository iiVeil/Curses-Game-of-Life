from cell import Cell
import time


class Board:
    def __init__(self, stdscr):
        self.window = stdscr
        self.height, self.width = stdscr.getmaxyx()
        self.height -= 2
        self.grid = [[Cell((x, y)) for x in range(self.width)]
                     for y in range(self.height)]
        self.states = ["□", "█"]

    def draw(self) -> None:
        """
        ? Description:
        * * Using curses, draw our grid to the screen using character cells
        """
        self.window.clear()
        for y, _ in enumerate(self.grid):
            line = ''
            for x in self.grid[y]:
                if x.alive:
                    line += self.states[1]
                else:
                    line += self.states[0]
            self.window.addstr(y, 0, line)
        self.window.addstr(
            self.height, 0, "Welcome to Conways Game of Life!")
        self.window.addstr(
            self.height+1, 0, "* * Click above on the grid to start placing your cells, i to iterate, r to reset")

    def iterate(self) -> None:
        """
        ? Description:
        * * Iterate our grid with the rules of Conways Game of Life
        * * * Any alive cell with less than 2 alive neighbors dies (underpopulation)
        * * * Any alive cell with more than 3 alive neighbors dies (overpopulation)
        * * * Any dead cell with 3 alive neighbors becomes a live cell (reproduction)
        """
        swaps = []
        for y, _ in enumerate(self.grid):
            for cell in self.grid[y]:
                alive = cell.alive
                alive_neighbors = self.get_alive_neighbors(cell)
                if alive:
                    if alive_neighbors < 2:
                        # * (underpopulation)
                        swaps.append(cell)
                    elif alive_neighbors > 3:
                        # * (overpopulation)
                        swaps.append(cell)
                elif not alive:
                    if alive_neighbors == 3:
                        # * (reproduction)
                        swaps.append(cell)
        for cell in swaps:
            cell.swap()

    def get_alive_neighbors(self, cell: Cell) -> int:
        """
        ? Description:
        * * Get the states of the 8 cardinal neighbors of a given cell

        ? Args:
        * * cell (Cell): the cell to check the neighbors of

        ? Returns:
        * * Int: Amount of live neighbors
        """
        alive = 0
        x, y = cell.x, cell.y
        checks = [(x+1, y+1), (x-1, y-1), (x-1, y+1),
                  (x+1, y-1), (x, y-1), (x, y+1), (x+1, y), (x-1, y)]
        for pos in checks:
            if self.on_grid(pos):
                if self.get_cell(pos).alive:
                    alive += 1
        return alive

    def on_grid(self, cell: tuple) -> bool:
        """
        ? Description:
        * * Returns true or false if a given pair is on the grid

        ? Args:
        * * cell (Cell): The pair to check

        ? Returns:
        * * bool: True if on the grid, False if off the grid
        """
        x, y = cell
        return True if (self.height-1 >= y and self.width-1 >= x and y >= 0 and x >= 0) else False

    def get_cell(self, cell: tuple) -> Cell:
        """
        ? Description:
        * * Get the cell at a position on the board

        ? Args:
        * * cell (tuple): The (X, Y) tuple of the cell

        ? Returns:
        * * cell.Cell: The cell object
        """
        x, y = cell
        return self.grid[y][x]

    def reset(self):
        self.grid = [[Cell((x, y)) for x in range(self.width)]
                     for y in range(self.height)]
