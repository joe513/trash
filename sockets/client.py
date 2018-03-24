#! /usr/local/bin/python3.6

import socket

cl = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cl.connect(('192.168.0.104', 53210))

while True:
    data = input('Enter: ')
    cl.send(bytes(data, 'utf-8'))
    r = cl.recv(1024)
    print(r.decode('utf-8'))

