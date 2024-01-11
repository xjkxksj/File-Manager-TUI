import curses


class MainModel(object):
    UP = -1
    DOWN = 1

    def __init__(self):
        self.directory = "C:\\"
        self.directories = []
        self.files = []
        self.width = curses.COLS
        self.height = curses.LINES
        self.max_lines = self.height - 4
