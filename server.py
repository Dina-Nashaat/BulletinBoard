import Pyro4
from RMIInterface import RMIInterface

class Server:
    def __init__(self):
        Pyro4.config.HOST = '192.168.8.100'
        daemon = Pyro4.Daemon()
        uri = daemon.register(RMIInterface)
        ns = Pyro4.locateNS()
        ns.register('obj', uri)
        print(uri)
        daemon.requestLoop()
