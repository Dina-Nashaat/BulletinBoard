import Pyro4

class Client:
	__server_interface = None

	def __init__(self):
		ns = Pyro4.locateNS()
		uri = ns.lookup('obj')
		self.__server_interface = Pyro4.Proxy(uri)

	def read(self):
		return self.__server_interface.read()

	def write(self, value):
		self.__server_interface.write(value)
