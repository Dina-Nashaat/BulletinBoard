import socket
from random import randrange
from threading import Thread
from Connection import Connection

#Initial Values
SERVERIP = '192.168.1.26'
SERVERPORT = 8888
THREADS = []

# Starting Server
server = Connection(SERVERIP, SERVERPORT)
print "Server has Started"

# Start main server
REQUEST_TYPE = None
Nsequence = 0
# while not REQUEST_TYPE
try:
    print("Hello")
    REQUEST_TYPE = server.connect()
    print(REQUEST_TYPE)
    THREAD = Connection(SERVERIP, randrange(2000, 8000))
    THREADS.append(THREAD)
    print "Thread Created"
    Thread(target=THREAD.handleThread, args=[REQUEST_TYPE]).start()
    REQUEST_TYPE = None
except socket.timeout:
    pass
