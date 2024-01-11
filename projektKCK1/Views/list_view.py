import curses
from Views import main_view


class ListView(main_view.MainView):

    def __init__(self):
        pass

    def display(self, window, items, top, max_lines, current, directory_path):
        window.clear()
        window.border()
        window.addstr(0, 1, directory_path)
        """Display the items on window"""
        for idx, item in enumerate(items[top:top + max_lines]):
            # Highlight the current cursor line
            if idx == current:
                window.addnstr(idx + 1, 1, item, 58, curses.color_pair(2))
            else:
                window.addnstr(idx + 1, 1, item, 58)
        window.refresh()
