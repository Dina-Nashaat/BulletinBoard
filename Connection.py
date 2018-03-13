import threading
import socket
import sys


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
        return self.conn
        # REQUEST_TYPE = self.conn.recv(1024)
        # print(REQUEST_TYPE)
        # return REQUEST_TYPE

    def handleThread(self, request, data, out_queue):
        request_type = request.recv(1)
        if(request_type == '0'):
            request.sendall(data)
            print("\nHello Reader")
            out_queue.put(data)
            sys.exit()
        elif (request_type == '1'):
            print("Hello Writer")
            data = request.recv(1)
            print("\nThe new writer value is: " + data)
            out_queue.put(data)
            sys.exit()
        else:
            print("Nothing of value")
        