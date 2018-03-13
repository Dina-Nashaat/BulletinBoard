import sys
import time
import socket


class Reader(object):
	__host = None
	__port = None

	def __init__(self, host, port):
		self.__host = host
		self.__port = port

	def connect(self):
		self.__socket = socket.create_connection((self.__host, self.__port))

	def read(self, sleep_time):
		self.__socket.sendall('0')
		self.__socket.sendall('0')	
		time.sleep(sleep_time)
		message = self.__socket.recv(1)
		print(message)

	def close(self):
		self.__socket.close()