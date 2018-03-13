import socket
import sys

class Reader(object):
	__host = None
	__port = None

	def __init__(self, host, port):
		self.__host = host
		self.__port = port

	def connect(self):
		self.__socket = socket.create_connection((self.__host, self.__port))

	def read(self):
		self.__socket.sendall('0')
		message = self.__socket.recv(4096)
		print(message)

	def close(self):
		self.__socket.close()