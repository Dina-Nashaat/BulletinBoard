import Pyro4

class Client:
    def __init__(self):
        ns = Pyro4.locateNS()
        uri = ns.lookup('obj')
        o = Pyro4.Proxy(uri)
        print(o.read())
