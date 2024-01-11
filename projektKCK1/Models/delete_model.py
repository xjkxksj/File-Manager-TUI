import os
from Models import main_model


class DeleteModel(main_model.MainModel):
    def __init__(self):
        super().__init__()

    def delete(self, source):
        if os.path.isfile(source):
            os.remove(source)
        else:
            os.rmdir(source)