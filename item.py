class Item:
    def __init__(self, uri=""):
        self.uri = uri


    def get_name(self):
        name = self.uri.replace("_", " ")
        return name


    def get_uri(self):
        return self.uri


    def get_plot_path(self):
        plot_path = 'plots/' + self.get_uri() + '.html'
        return plot_path
