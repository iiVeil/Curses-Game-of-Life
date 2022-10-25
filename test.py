import curses

screen = curses.initscr()
# curses.noecho()
curses.curs_set(0)
curses.mousemask(curses.BUTTON1_CLICKED)

screen.addstr("This is a Sample Curses Script\n\n")

while True:
    event = screen.getch()
    if event == ord("q"):
        break
    if event == curses.KEY_MOUSE:
        _, mx, my, _, _ = curses.getmouse()
        y, x = screen.getyx()
        screen.addstr(y, x, screen.instr(my, mx, 5))

curses.endwin()
