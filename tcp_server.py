import socket
import threading

bind_ip = "0.0.0.0"
bind_port = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#AF_INET: To use the IPv4 standard
#Sock stream: Indicates that it is going to be a TCP sever

#Bind connection
server.bind((bind_ip,bind_port))


#Maximum of 5 backlog connections
server.listen(5)

print "[*] Listening on %s:%d" % (bind_ip,bind_port)


#Client -handling thread
def handle_client(client_socket):
    #print out what client sends
    request = client_socket.recv(1024)
    print "[*] Received: %s" % request
    
    #send back a packet
    client_socket.send("ACK!")
    
    client_socket.close()

#Loop waiting for incoming connections
while True:
    client,addr = server.accept()
    print "[*] Accepted connection from: %s:%d" % (addr[0],addr[1])
    
    #Handle incoming data
    client_handler = threading.Thread(target=handle_client, args=(client,))
    client_handler.start()