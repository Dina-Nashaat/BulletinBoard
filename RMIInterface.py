import Pyro4
from reader import Reader
from writer import Writer

@Pyro4.expose
class RMIInterface:
    data = "5"

    def read(self):
        return self.data

    def write(self, data):
        self.data = data
