import time
from client import Client

client = Client()


data = client.read()
print(data)

time.sleep(8)

client.write("10")

data = client.read()
print(data)
