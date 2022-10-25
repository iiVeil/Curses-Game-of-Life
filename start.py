import curses
from board import Board


def main(stdscr):
    curses.curs_set(0)
    board = Board(stdscr)
    board.draw()
    event = stdscr.getch()
    match (event):
        case curses.KEY_MOUSE:
            _, mx, my, _, _ = curses.get_mouse()


if __name__ == "__main__":

    curses.wrapper(main)
