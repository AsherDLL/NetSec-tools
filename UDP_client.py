import socket

target_host="127.0.0.1"
target_port=80

#create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#AF_INET: To use the IPv4 standard
#Sock stream: Indicates that it is going to be a UDP client

#Bind connection
client.bind((target_host, target_port))

#send data
client.sendto("AAABBBCCC", (target_host, target_port))

#receive data
data, addr= client.recvfrom(4096)

print data