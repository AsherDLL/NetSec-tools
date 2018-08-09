
#In this code let's assume 3 things
# 1 The connection will always succeed 
# 2 The server is always expecting us to start sending data
# 3 The server will always respond in a timely fashion

import socket

target_host="www.google.com"
target_port=80

#create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#AF_INET: To use the IPv4 standard
#Sock stream: Indicates that it is going to be a TCP client

#connect the client
client.connect((target_host, target_port))

#send data
client.send("GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")

#receive data
response = client.recv(4096)

print response