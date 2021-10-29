class Item:
    def __init__(self, path="", name="", uri=""):
        self.path = path

    def get_path(self):
        return self.path

    def get_name(self):
        name = self.path.replace(".txt", "")
        name = name.replace("_data", "")
        name = name.replace("_", " ")
        return name

    def get_uri(self):
        uri = self.path.replace(".txt", "")
        uri = uri.replace("_data", "")
        return uri