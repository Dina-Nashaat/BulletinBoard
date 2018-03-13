from reader import Reader
from writer import Writer

reader1 = Reader('172.20.10.4', 8888)
reader1.connect()
reader1.read()
reader1.close()



