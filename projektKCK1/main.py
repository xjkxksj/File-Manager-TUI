import sys
import curses
from Controllers import list_controller
from Views import main_view, start_view


def main():
    window = curses.initscr()
    window.keypad(True)
    window.border(0)

    curses.curs_set(0)
    curses.noecho()
    curses.cbreak()

    curses.start_color()
    try:
        path = sys.argv[1] + "\\"
        control = list_controller.ListController(window, path)
    except Exception:
        control = list_controller.ListController(window, "C:\\")
    start = start_view.StartView(window)
    start.ascend()
    window.getkey()
    start.descend()
    view = main_view.MainView(window)
    view.display()
    control.input_stream()


if __name__ == '__main__':
    main()
