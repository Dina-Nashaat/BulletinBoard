import Pyro4

@Pyro4.expose
class RMIInterface:

    def read(self):
        f = open('value.txt', 'r')
        return f.read()

    def write(self, data):
        f = open('value.txt', 'w')
        f.write(data)