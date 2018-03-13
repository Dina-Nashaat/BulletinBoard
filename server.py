import socket
from random import randrange
from threading import Thread
from Connection import Connection

#Initial Values
SERVERIP = '127.0.0.1'
SERVERPORT = 8888
THREADS = []

# Starting Server
server = Connection(SERVERIP, SERVERPORT)
print "Server has Started"

# Start main server
REQUEST_TYPE = None
Nsequence = 0
while not REQUEST_TYPE:
    try:
        REQUEST_TYPE = server.connection.recv()
        THREAD = server(SERVERIP, randrange(2000, 8000))
        THREADS.append(THREAD)
        print "Thread Created"
        Thread(target=THREAD.handleThread, args=[REQUEST_TYPE]).start()
        REQUEST_TYPE = None
    except socket.timeout:
        pass
