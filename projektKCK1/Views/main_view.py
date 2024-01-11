import curses


class MainView(object):
    def __init__(self, window):
        self.window = window

    def display(self):
        self.window.attron(curses.color_pair(4))
        self.window.border()
        self.window.attroff(curses.color_pair(4))
        self.window.refresh()
        self.window.addstr(curses.LINES - 1, 1, "F1: ", curses.color_pair(4))
        self.window.addstr("L", curses.color_pair(5))
        self.window.addstr("eft  F2: ", curses.color_pair(4))
        self.window.addstr("R", curses.color_pair(5))
        self.window.addstr("ight  F3: ", curses.color_pair(4))
        self.window.addstr("I", curses.color_pair(5))
        self.window.addstr("nspect  F4: ", curses.color_pair(4))
        self.window.addstr("C", curses.color_pair(5))
        self.window.addstr("opy F5: ", curses.color_pair(4))
        self.window.addstr("M", curses.color_pair(5))
        self.window.addstr("ove F6: ", curses.color_pair(4))
        self.window.addstr("D", curses.color_pair(5))
        self.window.addstr("elete", curses.color_pair(4))

