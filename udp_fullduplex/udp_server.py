"""full duplex udp chat server """

import sys
import socket
import select

socket_list = []
host = socket.gethostname()  # get the host name
port = 5006 # arbitrary post
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# AF_INIT--> address family for IPv4
# SOCK_DGRAM--> datagram sockets
s.bind((host, port))
#socket_list.append(s)
print "waiting for connection"
sys.stdout.write('[server]');sys.stdout.flush()
while(1) :
    socket_list = [sys.stdin, s]
    read, write, error = select.select(socket_list, [], [])
    for sock in read :
        if sock == s:
#            print "the message is : ",
            data, addr = s.recvfrom(1024)
            print  data
            sys.stdout.write('[server]');sys.stdout.flush()
#            print data
        else :
            reply = raw_input("")
            s.sendto(reply, addr)
            sys.stdout.write('[server]');sys.stdout.flush()
#            s.sendto(reply, addr)

#    print 'Message[' + addr[0] + ':' + str(addr[1]) + '] -' + data.strip()
s.close()

