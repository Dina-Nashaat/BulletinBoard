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
        sSeq = 0
        THREADS = []
        while not self.request_type:
            try:
                sSeq = sSeq + 1
                self.request_type = self.server.connect()
                THREAD = Connection(SERVERIP, randrange(2000, 8000))

                thread1 = threading.Thread(target=THREAD.handleThread, args=[self.request_type, DATA, my_queue])
                print(thread1.getName() + " has started")
                THREADS.append(thread1)
                thread1.start()

                for t in THREADS:
                    print(t.getName() + " is alive: " + str(t.isAlive()))

                DATA = my_queue.get()

                print("\nThe current data is: " + DATA)
                self.request_type = None
            except socket.timeout:
                pass
