import os
from Models import main_model

class RightListModel(main_model.MainModel):

    def __init__(self):
        super().__init__()
        self.page_right_list = None
        self.current_right_list = None
        self.bottom_right_list = None
        self.top_right_list = None
        self.directory_path = self.directory
        self.directories = []
        self.files = []
        self.active = False

        self.items_right_list = self.directory_list()

    def set_items(self, items):
        self.items_right_list = items
        self.bottom_right_list = len(self.items_right_list)

    def get_items(self):
        return self.items_right_list

    def get_current_right_list(self):
        return self.current_right_list

    def is_file(self, path):
        return os.path.isfile(path)

    def is_dir(self, path):
        return os.path.isdir(path)

    def directory_list(self):
        self.directories = []
        self.files = []
        with os.scandir(self.directory_path) as catalog:
            for element in catalog:
                if element.is_file():
                    self.files.append(element.name)
                elif element.is_dir():
                    self.directories.append(element.name)

        self.top_right_list = 0
        self.bottom_right_list = len(self.directories + self.files)
        self.current_right_list = 0
        self.page_right_list = self.bottom_right_list // self.max_lines

        return self.directories + self.files

    def get_parent_path(self):
        dir = self.directory_path.split('\\')
        new_path = "C:\\"
        for d in range(1, len(dir) - 2):
            new_path += dir[d] + '\\'
        self.directory_path = new_path
        self.items_right_list = self.directory_list()

    def scroll(self, direction):
        next_line_right_list = self.current_right_list + direction

        if (direction == self.UP) and (self.top_right_list > 0 and self.current_right_list == 0):
            self.top_right_list += direction
            return

        if (direction == self.DOWN) and (next_line_right_list == self.max_lines) and (
                self.top_right_list + self.max_lines < self.bottom_right_list):
            self.top_right_list += direction
            return

        if (direction == self.UP) and (self.top_right_list > 0 or self.current_right_list > 0):
            self.current_right_list = next_line_right_list
            return

        if (direction == self.DOWN) and (next_line_right_list < self.max_lines) and (
                self.top_right_list + next_line_right_list < self.bottom_right_list):
            self.current_right_list = next_line_right_list
            return

    def paging(self, direction):
        current_right_list_page = (self.top_right_list + self.current_right_list) // self.max_lines
        next_page_right_list = current_right_list_page + direction

        if next_page_right_list == self.page_right_list:
            self.current_right_list = min(self.current_right_list, self.bottom_right_list % self.max_lines - 1)

        if (direction == self.UP) and (current_right_list_page > 0):
            self.top_right_list = max(0, self.top_right_list - self.max_lines)
            return

        if (direction == self.DOWN) and (current_right_list_page < self.page_right_list):
            self.top_right_list += self.max_lines
            return