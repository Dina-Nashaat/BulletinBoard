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
        print("Listening:")
        self.conn, self.addr = self.sock.accept()
        return self.conn, self.addr

    def handleThread(self, request, data, out_queue, name, addr, sleep ):
        print(str(name) + " has started")
        while True:
            try:
                request_type = request.recv(1)
                if(request_type == '0'):
                    request.sendall(data)
                    print("\nHello Reader " + str(name) + " from " + str(addr) + " will take " + str(sleep))
                    #############
                    out_queue.put(data)
                elif (request_type == '1'):
                    print("Hello Writer" + str(name) + " from " + str(addr) + " will take " + str(sleep))
                    data = request.recv(1)
                    print("\nThe new writer value is: " + data)
                    ##############
                    out_queue.put(data)
                else:
                    print("Nothing of value")
                    raise Exception("Client closed")
            except Exception as err:
                print(err)
                print("Connection has closed for " + str(name))
                request.close()
                return False