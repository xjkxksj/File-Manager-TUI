import curses
from Models import main_model


class MainController(object):

    def __init__(self):
        self.model = main_model.MainModel()
        self.list_active = True


        curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_CYAN)
        curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)
        curses.init_pair(4, curses.COLOR_BLACK, curses.COLOR_WHITE)
        curses.init_pair(5, curses.COLOR_YELLOW, curses.COLOR_MAGENTA)
        curses.init_pair(6, curses.COLOR_BLUE, curses.COLOR_BLACK)

        self.current = curses.color_pair(2)
