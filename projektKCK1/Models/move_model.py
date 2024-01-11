import os
import shutil
from Models import main_model


class MoveModel(main_model.MainModel):
    def __init__(self):
        super().__init__()

    def move(self, source, destination):
        if os.path.isfile(source) and os.access(source, os.X_OK):
            shutil.copy2(source, destination)
            os.remove(source)
        else:
            if os.access(source, os.X_OK):
                shutil.copytree(source, destination)
                os.rmdir(source)