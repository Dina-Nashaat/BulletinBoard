import time
from client import Client

client = Client()


data = client.read()
print(data)

client.write("10")

data = client.read()
print(data)
