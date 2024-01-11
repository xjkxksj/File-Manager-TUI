import os
import shutil
from Models import main_model


class CopyModel(main_model.MainModel):
    def __init__(self):
        super().__init__()

    def copy(self, source, destination):
        if os.path.isfile(source):
            shutil.copy2(source,
                         destination)
        else:
            shutil.copytree(source,
                            destination)

