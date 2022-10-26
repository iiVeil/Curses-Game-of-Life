import curses
from board import Board


def main(stdscr):
    curses.curs_set(0)
    curses.mousemask(curses.BUTTON1_CLICKED)
    board = Board(stdscr)
    while True:
        board.draw()
        event = stdscr.getch()
        if event == curses.KEY_MOUSE:
            _, mx, my, _, _ = curses.getmouse()
            if my < board.height:
                board.get_cell((mx, my)).swap()
        elif event == ord("i"):
            board.iterate()
        elif event == ord("r"):
            board.reset()


if __name__ == "__main__":

    curses.wrapper(main)
