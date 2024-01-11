from Views import copy_view, exception_view, move_view, delete_view
from Controllers import main_controller
from Models import copy_model, move_model, delete_model


class CopyController(main_controller.MainController):
    def __init__(self, window, file, left_model, right_model):
        super().__init__()
        self.window = window
        self.file = file
        self.left_model = left_model
        self.right_model = right_model
        self.copy_model = copy_model.CopyModel()
        self.move_model = move_model.MoveModel()
        self.delete_model = delete_model.DeleteModel()

    def copy_control(self):
        try:
            self.new_tab = copy_view.CopyView(self.window)
            self.new_tab.display(self.file, self.right_model.directory_path)
            key = self.window.getkey()
            while True:
                if key == '\n':
                    self.copy_model.copy(self.left_model.directory_path + self.file,
                                         self.right_model.directory_path + self.file)
                    break
                elif key == chr(27):
                    break
                key = self.window.getkey()
            self.new_tab.destroy()
        except Exception:
            except_view = exception_view.ExceptionView(self.window)
            except_view.display(self.left_model.directory_path + self.file)

    def move(self):
        try:
            self.new_tab = move_view.MoveView(self.window)
            self.new_tab.display(self.file, self.right_model.directory_path)
            key = self.window.getkey()
            while True:
                if key == '\n':
                    self.move_model.move(self.left_model.directory_path + self.file,
                                         self.right_model.directory_path + self.file)
                    break
                elif key == chr(27):
                    break
                key = self.window.getkey()
            self.new_tab.destroy()
        except Exception:
            except_view = exception_view.ExceptionView(self.window)
            except_view.display(self.left_model.directory_path + self.file)

    def delete(self):
        try:
            self.new_tab = delete_view.DeleteView(self.window)
            self.new_tab.display(self.file)
            key = self.window.getkey()
            while True:
                if key == '\n':
                    self.delete_model.delete(self.left_model.directory_path + self.file)
                    break
                elif key == chr(27):
                    break
                key = self.window.getkey()
            self.new_tab.destroy()
        except Exception:
            except_view = exception_view.ExceptionView(self.window)
            except_view.display(self.left_model.directory_path + self.file)
