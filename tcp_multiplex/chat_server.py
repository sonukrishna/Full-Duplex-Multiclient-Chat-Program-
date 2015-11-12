""" a full duplex chat program """

import socket
import select
import sys
#list for socket descriptors
socket_list = []
#host = socket.gethostname()
port = 8121
def chat_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(("", port))
    server_socket.listen(10)

    # add server socket to the list
    socket_list.append(server_socket)

    print "chat server started on port" + str(port)

    while 1:
        #get the list of sockets to be read through select
        read, write, error = select.select(socket_list, [], [])
        for sock in read:
            if sock == server_socket:
                sock_obj, addr = server_socket.accept()
                socket_list.append(sock_obj)
                print "Client (%s, %s) connected"%addr

                broadcast(server_socket, sock_obj, 
                          "[%s, %s] entered our chat address\n" %addr)
            else :
                #process data recieved from client,
                data = sock.recv(4000)
                if data :
                    broadcast(server_socket, sock, 
                              'Message : %s\n'  % data.strip())
                else :
                    # remove the broken socket
                    if sock in socket_list :
                        socket_list.remove(sock)
                    broadcast(server_socket, sock, 
                              "Client (%s, %s) is offline" %addr)

    server_socket.close()

# broadcast the messages to our clients
def broadcast (server_socket, sock, msg):
    for sockets in socket_list :
        if sockets != server_socket and sockets != sock :
            sockets.send(msg)
#if __name__ == "__main__" :
    #    sys.exit(chat_server())
chat_server()
