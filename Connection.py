import threading
import socket
import sys
import time

class Connection(threading.Thread):

    def __init__(self, host, port):
        super(Connection, self).__init__()
        self.conn = None
        self.var = '4'
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((host, port))
        self.sock.listen(3)
        print("The server has started and listening")
        print(port)


    def connect(self):
        self.conn, self.addr = self.sock.accept()
        return self.conn, self.addr

    def handleReader(self, request, data, out_queue, seq, addr, rNum):
        while True:
            try:
                ping = request.recv(1)
                if ping:
                    request.sendall(data)
                    print(str(seq) + '\t' + str(data) + '\t' + str(ping) + '\t' + str(rNum))
                    out_queue.put(data)
                else:
                    raise Exception("Client closed")
            except:
                request.close()
                return False

    def handleWriter(self, request, data, out_queue, seq, addr):
        while True:
            try:
                ping = request.recv(1)
                if ping:
                    print(str(seq) + '\t' + str(data) + '\t' + str(ping))
                    data = request.recv(1)
                    out_queue.put(data)
                else:
                    raise Exception("Client closed")
            except:
                request.close()
                return False