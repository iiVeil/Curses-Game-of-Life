import curses
from board import Board


def main(stdscr):
    curses.mousemask(curses.BUTTON1_CLICKED)
    board = Board(stdscr)
    while True:
        curses.curs_set(0)
        board.draw()
        event = stdscr.getch()
        if event == curses.KEY_MOUSE:
            _, mx, my, _, _ = curses.getmouse()
            if board.on_grid((mx, my)):
                board.get_cell((mx, my)).swap()
        elif event == ord("i"):
            board.iterate()
        elif event == ord("r"):
            board.reset()


if __name__ == "__main__":
    curses.wrapper(main)
