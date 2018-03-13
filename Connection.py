import threading
import socket


class Connection(threading.Thread):
    def __init__(self, host, port):
        super(Connection, self).__init__()
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((host, port))
        self.sock.listen(3)
        self.data_size = size

    def handleThread(self, request_type):
        if request_type == 0
            print("Hello Reader")
        else if request_type == 1
            print("Hello Writer")