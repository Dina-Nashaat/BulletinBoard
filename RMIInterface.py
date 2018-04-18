import Pyro4
import time
@Pyro4.expose
class RMIInterface:

    def __init__(self, daemon):
        self.daemon = daemon

    def read(self):
        f = open('value.txt', 'r')
        print("Client: ", Pyro4.current_context.client_sock_addr[0])
        print("number of busy threads: ", len(self.daemon.transportServer.pool.busy))
        print("sequence Number: ", Pyro4.current_context.seq)
        return f.read()

    def write(self, data):
        f = open('value.txt', 'w')
        print("Client: ", Pyro4.current_context.client_sock_addr[0])
        print("number of busy threads: ", len(self.daemon.transportServer.poo))
        print("sequence Number: ", Pyro4.current_context.seq)
        f.write(data)