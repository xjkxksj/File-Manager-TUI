import curses
import curses.textpad
from Views import main_view

class InspectView(main_view.MainView):
    def __init__(self, lines, window):
        super().__init__(window)
        self.file_lines = lines
        self.file_window = curses.newpad(len(lines) + 1, 300)
        self.box = curses.newwin(28, curses.COLS - 2, 1, 1)
        window.refresh()
        for i in self.file_lines:
            self.file_window.addstr(i)


    def display(self):
        self.box.refresh()
        self.file_window.refresh(0, 0, 1, 1, curses.LINES - 2, curses.COLS - 2)


    def refresh(self, line):
        self.file_window.refresh(line, 0, 1, 1, curses.LINES - 2, curses.COLS - 2)

    def destroy(self):
        self.file_window.erase()
        self.file_window.refresh(0, 0, 1, 1, curses.LINES - 2, curses.COLS - 2)
        super(InspectView, self).display()
        self.box.clear()
        self.box.refresh()