"""full duplex udp chat client prograaam """
import sys
import socket
import select
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
port = 5006;
host = socket.gethostname()
#s.bind((host, port))
print "client is ready now :"
sys.stdout.write('[client]');sys.stdout.flush()
while(1):
    socket_list = [sys.stdin, s]
    read, write, error = select.select(socket_list, [], [])
    for sock in read :
        if sock != s :
            msg = raw_input("to server")
            s.sendto(msg, (host, port))
            sys.stdout.write('[client]');sys.stdout.flush()

        else :
#            print "the msg from server",
            reply, addr = s.recvfrom(1024)
            print  reply
            sys.stdout.write('[client]');sys.stdout.flush()
#            print reply
#            sys.stdout.write('[Me]');sys.stdout.flush()
s.close()

