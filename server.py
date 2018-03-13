import socket
from random import randrange
from threading import Thread
from Connection import Connection

#Initial Values
SERVERIP = '192.168.1.26'
SERVERPORT = 8888
THREADS = []


class Server:
    def __init__(self,host,port):
        self.server = Connection(host, port)
        self.request_type = None

# while not REQUEST_TYPE

    def run(self):
        while not self.request_type:
            try:
                self.request_type = self.server.connect()
                THREAD = Connection(SERVERIP, randrange(2000, 8000))
                THREADS.append(THREAD)
                Thread(target=THREAD.handleThread, args=[self.request_type]).start()
                self.request_type = None
            except socket.timeout:
                pass
