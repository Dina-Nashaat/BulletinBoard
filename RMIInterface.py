import Pyro4

@Pyro4.expose
class RMIInterface:

    def read(self):
        return "Reading"

    def write(self):
        return "Writing"
