import socket
from random import randrange
import threading
from Connection import Connection
import Queue


class Server:
    def __init__(self, host, port):
        self.server = Connection(host, port)
        self.connection = None

    def run(self):
        DATA = '4'
        my_queue = Queue.Queue()
        sSeq = 0
        THREADS = []
        queued = Queue.Queue()
        writer_thread = None
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

                if(not queued.empty()):
                    writer_thread = queued.get()
                    writer_thread.start()
                    
                if(not my_queue.empty()):
                    DATA = my_queue.get()

                if(request_type == '0'):
                    thread = threading.Thread(target=self.server.handleReader, args=[self.connection, DATA, my_queue, sSeq, self.addr, rNum+1])
                    THREADS.append(thread)
                    thread.start()
                elif (request_type == '1'):
                    thread = threading.Thread(target=self.server.handleWriter, args=[self.connection, DATA, my_queue, sSeq, self.addr])
                    if (writer_thread == None or not writer_thread.isAlive()):
                        writer_thread = thread
                        writer_thread.start()
                        DATA = my_queue.get()
                    else:
                        queued.put(thread)

                self.connection = None
            except socket.timeout:
                pass
