#! /usr/local/bin/python3.6

from socket import *

HOST = 'localhost'
PORT = 21567
BUFSIZE = 1024
ADDR = (HOST, PORT)

udpCliSock = socket(AF_INET, SOCK_DGRAM)

while True:
    data = input('Enter: ')
    if not data:
        break
    udpCliSock.sendto(bytes(data, 'utf-8'), ADDR)
    data, ADDR  = udpCliSock.recvfrom(BUFSIZE)
    if not data:
        break
    print(data.decode('utf-8'))

