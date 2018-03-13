import sys
import time
import socket


class Writer(object):
	__host = None
	__port = None

	def __init__(self, host, port):
		self.__host = host
		self.__port = port

	def connect(self):
		self.__socket = socket.create_connection((self.__host, self.__port))

	def write(self, sleep_time, message):
		self.__socket.sendall('1')
		self.__socket.sendall('1')
		time.sleep(sleep_time)
		self.__socket.sendall(message)

	def close(self):
		self.__socket.close()