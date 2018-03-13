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
        self.connection = None

    def run(self):
        DATA = '4'
        my_queue = Queue.Queue()
        sSeq = 0
        THREADS = []
        while not self.connection:
            try:
                sSeq = sSeq + 1
                self.connection, self.addr = self.server.connect()

                request_type = self.connection.recv(1)
                thread = None
                rNum = 0

                for t in THREADS:
                    if t.isAlive():
                        rNum = rNum + 1

                if(request_type == '0'):
                    thread = threading.Thread(target=self.server.handleReader, args=[self.connection, DATA, my_queue, sSeq, self.addr, rNum+1])
                elif (request_type == '1'):
                    thread = threading.Thread(target=self.server.handleWriter, args=[self.connection, DATA, my_queue, sSeq, self.addr])

                THREADS.append(thread)
                thread.start()
                DATA = my_queue.get()

                self.connection = None
            except socket.timeout:
                pass
