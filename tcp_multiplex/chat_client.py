""" full duplex chat program server side"""

import socket
import select
import sys

def chat_client():
    if(len(sys.argv) < 3) :
        sys.exit()

    host = sys.argv[1]
    port = int(sys.argv[2])

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#    client_socket.settimeout(2)

    #connecting to remote host
    client_socket.connect((host, port))
    print "connected to remote host, you can send messages now"
    sys.stdout.write('[Me]');sys.stdout.flush()

    while 1:
        socket_list = [sys.stdin, client_socket]

        #get sockets list which are read by select
        read, write, error = select.select(socket_list, [], [])
#        print read()
#        print write
#        print error
        for sock in read :
           
            if sock == client_socket :
                # incoming msg from client_socket
                data = sock.recv(4000)
                if not data :
                    print "Disconnected"
                    sys.exit()
                else :
                    # print data
                    sys.stdout.write(data)
                    sys.stdout.write('[Me]');sys.stdout.flush()
            else :
                #user write somethng
                msg  = sys.stdin.readline()
                client_socket.send(msg)
                sys.stdout.write('[Me]'); sys.stdout.flush()
    
#    sys.exit(chat_client())
chat_client()
