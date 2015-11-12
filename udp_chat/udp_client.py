""" udp client for simple chat program """

import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
port = 5005;
host = socket.gethostname()
#s.bind((host, port))
while(1):
    msg = raw_input("enter the msg:")
    s.sendto(msg, (host, port))
    reply, addr = s.recvfrom(1024)
    print 'Server reply :' ,reply
s.close()
