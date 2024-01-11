import os
import curses

from Controllers import copy_controller, main_controller, inspect_controller
from Views import list_view
from Models import left_list_model, right_list_model


class ListController(main_controller.MainController):

    def __init__(self, window, path):
        super().__init__()
        self.window = window
        self.which_active = True  # true is left list, false - right list
        self.left_model = left_list_model.LeftListModel()
        self.right_model = right_list_model.RightListModel()
        self.left_model.directory_path = path
        self.right_model.directory_path = path
        self.left_list = self.left_model.directory_list()
        self.right_list = self.right_model.directory_list()
        self.screen_left = list_view.ListView()
        self.screen_right = list_view.ListView()
        self.box_left = curses.newwin(curses.LINES - 2, curses.COLS // 2 - 1, 1, 1)
        self.box_left.box()
        self.box_right = curses.newwin(curses.LINES - 2, curses.COLS // 2 - 1, 1, curses.COLS // 2 - 1)
        self.box_right.box()
        self.screen_left.display(self.box_left, self.left_list, self.left_model.top_left_list, self.model.max_lines,
                                 self.left_model.current_left_list, self.left_model.directory_path)
        self.screen_right.display(self.box_right, self.right_list, self.right_model.top_right_list,
                                  self.model.max_lines,
                                  self.right_model.current_right_list, self.right_model.directory_path)

        self.current = curses.color_pair(2)

    def get_active(self):
        return self.which_active

    def set_active(self, bool):
        self.which_active = bool

    def input_stream(self):
        """Waiting an input and run a proper method according to type of input"""
        self.screen_left.display(self.box_left, self.left_list, self.left_model.top_left_list, self.model.max_lines,
                                 self.left_model.current_left_list, self.left_model.directory_path)
        self.screen_right.display(self.box_right, self.right_list, self.right_model.top_right_list,
                                  self.model.max_lines,
                                  self.right_model.current_right_list, self.right_model.directory_path)
        while True:
            self.screen_left.display(self.box_left, self.left_list, self.left_model.top_left_list, self.model.max_lines,
                                     self.left_model.current_left_list, self.left_model.directory_path)
            self.screen_right.display(self.box_right, self.right_list, self.right_model.top_right_list,
                                      self.model.max_lines,
                                      self.right_model.current_right_list, self.right_model.directory_path)

            ch = self.window.getch()
            if ch == curses.KEY_UP:
                if self.which_active:
                    self.left_model.scroll(self.model.UP)
                else:
                    self.right_model.scroll(self.model.UP)
            elif ch == curses.KEY_DOWN:
                if self.which_active:
                    self.left_model.scroll(self.model.DOWN)
                else:
                    self.right_model.scroll(self.model.DOWN)
            elif ch == curses.KEY_LEFT:
                if self.which_active:
                    self.left_model.paging(self.model.UP)
                else:
                    self.right_model.paging(self.model.UP)
            elif ch == curses.KEY_RIGHT:
                if self.which_active:
                    self.left_model.paging(self.model.DOWN)
                else:
                    self.right_model.paging(self.model.DOWN)
            elif ch == 27:
                break
            elif ch == ord('l') or ch == curses.KEY_F1:
                self.which_active = True
            elif ch == ord('r') or ch == curses.KEY_F2:
                self.which_active = False
            elif ch == ord('\n'):
                if self.which_active:
                    if len(self.left_list) > 0:
                        path = self.left_model.directory_path + self.left_list[
                            self.left_model.top_left_list + self.left_model.current_left_list]
                        if os.path.isdir(path):
                            self.left_model.directory_path += self.left_list[
                                            self.left_model.top_left_list + self.left_model.current_left_list] + '\\'
                            self.left_list = self.left_model.directory_list()
                        else:
                            os.system('"' + path + '"')
                else:
                    if len(self.right_list) > 0:
                        path = self.right_model.directory_path + self.right_list[
                            self.right_model.top_right_list + self.right_model.current_right_list]
                        if os.path.isdir(path):
                            self.right_model.directory_path += self.right_list[
                                            self.right_model.top_right_list + self.right_model.current_right_list] + '\\'
                            self.right_list = self.right_model.directory_list()
                        else:
                            os.system('"' + path + '"')
            elif ch == ord('\b'):
                if self.which_active:
                    self.left_model.get_parent_path()
                    self.left_list = self.left_model.directory_list()
                else:
                    self.right_model.get_parent_path()
                    self.right_list = self.right_model.directory_list()
            elif ch == ord('i') or ch == curses.KEY_F3:
                try:
                    if self.which_active:
                        inspect_control = inspect_controller.InspectController(
                            self.left_model.directory_path + self.left_list[
                                self.left_model.top_left_list + self.left_model.current_left_list], self.window)
                        inspect_control.inspect_control()
                    else:
                        inspect_control = inspect_controller.InspectController(
                            self.right_model.directory_path + self.right_list[
                                self.right_model.top_right_list + self.right_model.current_right_list], self.window)
                        inspect_control.inspect_control()
                except Exception:
                    pass

            elif ch == ord('c') or ch == curses.KEY_F4:
                try:
                    copy_control = copy_controller.CopyController(self.window,
                                                                  self.left_list[self.left_model.top_left_list + self.left_model.current_left_list],
                                                                  self.left_model, self.right_model)
                    copy_control.copy_control()
                    self.left_list = self.left_model.directory_list()
                    self.right_list = self.right_model.directory_list()
                except Exception:
                    pass
            elif ch == ord('m') or ch == curses.KEY_F5:
                try:
                    move_control = copy_controller.CopyController(self.window,
                                                                  self.left_list[self.left_model.top_left_list + self.left_model.current_left_list],
                                                                  self.left_model, self.right_model)
                    move_control.move()
                    self.left_list = self.left_model.directory_list()
                    self.right_list = self.right_model.directory_list()
                except Exception:
                    pass
            elif ch == ord('d') or ch == curses.KEY_F6:
                try:
                    if self.which_active:
                        delete_control = copy_controller.CopyController(self.window, self.left_list[self.left_model.top_left_list +
                            self.left_model.current_left_list], self.left_model, self.right_model)
                        delete_control.delete()
                    else:
                        delete_control = copy_controller.CopyController(self.window, self.right_list[self.right_model.top_right_list +
                            self.right_model.current_right_list], self.right_model, self.right_model)
                        delete_control.delete()
                    self.left_list = self.left_model.directory_list()
                    self.right_list = self.right_model.directory_list()
                except Exception:
                    pass
