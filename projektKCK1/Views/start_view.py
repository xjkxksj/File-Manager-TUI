import curses
import time

from Views import main_view


class StartView(main_view.MainView):
    def __init__(self, window):
        super().__init__(window)
        self.pad = curses.newpad(6, 100)
        self.window.refresh()
        self.pad.addstr(" _____ _ _        __  __  \n", curses.color_pair(6))
        self.pad.addstr("|  ___(_) | ___  |  \/  | __ _ _ __   __ _  __ _  ___ _ __ \n", curses.color_pair(6))
        self.pad.addstr("| |_  | | |/ _ \ | |\/| |/ _` | '_ \ / _` |/ _` |/ _ \ '__|\n", curses.color_pair(6))
        self.pad.addstr("|  _| | | |  __/ | |  | | (_| | | | | (_| | (_| |  __/ |   \n", curses.color_pair(3))
        self.pad.addstr("|_|   |_|_|\___| |_|  |_|\__,_|_| |_|\__,_|\__, |\___|_|   \n", curses.color_pair(3))
        self.pad.addstr("                                           |___/           ", curses.color_pair(3))
        self.x_at_center = 0

    def ascend(self):
        yLine = curses.LINES // 4
        for i in range(59):
            self.window.clear()
            self.window.refresh()
            self.pad.refresh(0, 59 - i, yLine, i - 59, yLine + 6, 59 + i)
            time.sleep(0.005)
        for i in range((curses.COLS // 2) - 28):
            self.window.clear()
            self.window.refresh()
            self.pad.refresh(0, 0, yLine, i, yLine + 6, 59 + i)
            time.sleep(0.005)
            self.x_at_center = i

        start_line = "Press any key to start"
        self.window.addstr(yLine * 2, (curses.COLS // 2) - len(start_line) // 2, start_line, curses.color_pair(1) )

    def descend(self):
        yLine = curses.LINES // 4
        for i in range(self.x_at_center, curses.COLS - 59):
            self.window.clear()
            self.window.refresh()
            self.pad.refresh(0, 0, yLine, i, yLine + 6, 59 + i)
            time.sleep(0.002)