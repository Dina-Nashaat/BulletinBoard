import time
from reader import Reader
from writer import Writer

host = '172.20.10.2'
port = 8888

# server = Server(host, port)
# server.run()

reader1 = Reader(host, port)
reader1.connect()
reader1.read(1)

reader1.close()
print('reader1 done')

writer1 = Writer(host, port)
writer1.connect()
writer1.write(1, '3')

writer2 = Writer(host, port)
writer2.connect()
writer2.write(3, '7')

reader2 = Reader(host, port)
reader2.connect()
reader2.read(8)

writer1.close()
print('writer1 done')

writer2.close()
print('writer2 done')

print('reader2 done')
reader2.close()

reader3 = Reader(host, port)
reader3.connect()
reader3.read(8)

print('reader3 done')
reader3.close()