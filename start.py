from reader import Reader
from writer import Writer
from server import Server


server = Server('192.168.1.26', 8888)
server.run()
# reader1 = Reader('172.20.10.4', 8888)
# reader1.connect()
# reader1.read()
# reader1.close()
