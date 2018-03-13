import socket
from random import randrange
import threading
from Connection import Connection
import Queue

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
        DATA = '4'
        my_queue = Queue.Queue()
        while not self.request_type:
            try:
                self.request_type = self.server.connect()
                THREAD = Connection(SERVERIP, randrange(2000, 8000))
                THREADS.append(THREAD)
                thread1 = threading.Thread(target=THREAD.handleThread, args=[self.request_type, DATA, my_queue])
                thread1.start()
                thread1.join()
                
                DATA = my_queue.get()
                print(DATA)
                self.request_type = None
            except socket.timeout:
                pass
