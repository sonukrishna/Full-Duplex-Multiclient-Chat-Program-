""" udp server """

import socket

host = socket.gethostname()  # get the host name
port = 5005 # arbitrary post
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# AF_INIT--> address family for IPv4
# SOCK_DGRAM--> datagram sockets
s.bind((host, port))
print "waiting for connection"
while(1) :
    data, addr = s.recvfrom(1024)
    print data
    reply = raw_input("enter the messg:")
    s.sendto(reply, addr)
#    print 'Message[' + addr[0] + ':' + str(addr[1]) + '] -' + data.strip()
s.close()
