#!/usr/bin/env python
import socket


def server_program():
   
    host = socket.gethostname()
    port = 5006  
    
    server_socket = socket.socket()  
    
    server_socket.bind((host, port))  

    server_socket.listen(2)
    conn, address = server_socket.accept()  
    
    print("Connection from: " + str(address))
    while True:
        # receive data stream. it won't accept data packet greater than 1024 bytes
        data = conn.recv(1024).decode()
        numbers=data.split()
        data=numbers[0]
        if not data:
            # if data is not received break
            break
        print("from connected user: " + str(Sum))
      
        message="odd"
        if !message.isnumeric():
            message="Enter a valid number"
        else if data%2==0:
            message="Even"
        conn.send(message.encode())  # send data to the client

    conn.close()  # close the connection


if __name__ == '__main__':
    server_program()
