class Board:
    def __init__(self, stdscr):
        self.window = stdscr
        self.height, self.width = stdscr.getmaxyx()
        self.board = [[False for _ in range(self.width)]
                      for _ in range(self.height-2)]
        self.states = ["░", "█"]

    def draw(self):
        for iy, _ in enumerate(self.board):
            line = ''
            for x in self.board[iy]:
                if x:
                    line += self.states[1]
                else:
                    line += self.states[0]
            self.window.addstr(iy, 0, line)
        self.window.addstr(
            self.height-2, 0, "Welcome to Conways Game of Life!")
        self.window.addstr(
            self.height-1, 0, "  Click above on the grid to start placing your cells, then press enter to start iteration!")

    def swap(self, cell: tuple):
        pass
