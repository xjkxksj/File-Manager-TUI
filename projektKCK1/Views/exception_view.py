import curses

from Views import main_view


class ExceptionView(main_view.MainView):

    def __init__(self, window):

        super().__init__(window)
        self.size_line = 6
        self.size_col = 50
        self.center_col = curses.COLS//2
        self.center_line = curses.LINES//2
        self.box = curses.newwin(self.size_line, self.size_col, self.center_line - (self.size_line // 2) - 1, self.center_col - (self.size_col // 2))
        self.box.box()

    def display(self, exception):
        self.box.clear()
        self.box.attron(curses.color_pair(3))
        self.box.border()
        self.box.attroff(curses.color_pair(3))
        string = "Press any button to continue..."
        self.box.addstr(1, 1, "Exception:" )
        self.box.addstr(2, 1, "Permission denied: " + exception)
        self.box.addstr(4, self.size_col - len(string) - 1, string)
        self.box.refresh()
        self.box.getch()
        self.destroy()

    def destroy(self):
        self.box.clear()
        self.box.refresh()