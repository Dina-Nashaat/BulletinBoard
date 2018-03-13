import time
from reader import Reader
from writer import Writer
from server import Server

host = '192.168.1.26'
port = 8888

# server = Server(host, port)
# server.run()

reader1 = Reader(host, port)
reader1.connect()
reader1.read(7)

writer1 = Writer(host, port)
writer1.connect()
writer1.write(2, '5')

reader2 = Reader(host, port)
reader2.connect()
reader2.read(1)

reader1.close()
print('reader1 done')

writer1.close()
print('writer1 done')

print('reader2 done')
reader2.close()
