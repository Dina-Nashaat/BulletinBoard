import socket
import sys

class Client(object):
	__host = None
	__port = None

	def __init__(self, host, port):
		self.__host = host
		self.__port = port

	def connect(self):
		self.__socket = socket.create_connection((self.__host, self.__port))

	def read(self):
		self.__socket.sendall('0')
		self.__socket.recv(4096)