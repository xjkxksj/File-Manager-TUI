from Models import main_model

class InspectModel(main_model.MainModel):
    def __init__(self):
        super(InspectModel, self).__init__()
        self.file_content = []

    def inspect(self, path):
        file = open(path, "r")
        for line in file:
            self.file_content.append(line)