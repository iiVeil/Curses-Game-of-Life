import curses
from board import Board


def main(stdscr):
    curses.mousemask(curses.BUTTON1_CLICKED)
    grid = Board(stdscr)
    while True:
        curses.curs_set(0)
        grid.draw()
        event = stdscr.getch()
        if event == curses.KEY_MOUSE:
            _, mx, my, _, _ = curses.getmouse()
            if grid.on_grid((mx, my)):
                grid.get_cell((mx, my)).swap()
        elif event == ord("i"):
            grid.iterate()
        elif event == ord("r"):
            grid.reset()


if __name__ == "__main__":
    curses.wrapper(main)
