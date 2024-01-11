import curses

from Controllers import main_controller
from Views import inspect_view, exception_view
from Models import inspect_model


class InspectController(main_controller.MainController):
    def __init__(self, path, window):
        super().__init__()
        self.inspect_model = inspect_model.InspectModel()
        self.path = path
        self.window = window

    def inspect_control(self):
        try:
            self.inspect_model.inspect(self.path)
            self.inspect_view = inspect_view.InspectView(self.inspect_model.file_content, self.window)
            self.inspect_view.display()
            line = 0
            while True:
                ch = self.window.getch()
                if ch == curses.KEY_UP:
                    if line > 0:
                        line = line - 1
                elif ch == curses.KEY_DOWN:
                    if line < len(self.inspect_model.file_content):
                        line = line + 1
                elif ch == 27:
                    break
                self.inspect_view.refresh(line)
            self.inspect_view.destroy()
        except Exception:
            except_view = exception_view.ExceptionView(self.window)
            except_view.display(self.path)
