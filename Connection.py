import threading
import socket




class Connection(threading.Thread):

    def __init__(self, host, port):
        super(Connection, self).__init__()
        self.conn = None
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((host, port))
        self.sock.listen(3)
        print("The server has started and listening")
        print(port)


    def connect(self):
        print("Listening:")
        self.conn, self.addr = self.sock.accept()
        REQUEST_TYPE = self.conn.recv(1024)
        self.conn.sendall('0')
        print(REQUEST_TYPE)
        return REQUEST_TYPE

    def handleThread(self, request_type):
        if(request_type == '0'):
            print("Hello Reader")

        elif (request_type == '1'):
            print("Hello Writer")
        else:
            print("Nothing of value")