import Pyro4

class Client:
    def __init__(self):
        ns = Pyro4.locateNS()
        uri = ns.lookup('obj')
        o = Pyro4.Proxy(uri)
        data = o.read()
        print(data)
        o.write("10")
        data = o.read()
        print(data)
