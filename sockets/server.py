#! usr/local/bin/python3.6

from socket import *
from time import ctime


HOST = ''
PORT = 21567
BUFSIZE = 1024
ADDR = (HOST, PORT)

sock = create_connection(ADDR)

data, from_who = sock.recvfrom(BUFSIZE)
sock.sendto(b'It will be ok', from_who)


print('%s: %s' % (from_who, data))







#
# udpSerSock = socket(AF_INET, SOCK_DGRAM)
# udpSerSock.bind(ADDR)
#
# while True:
#     print("Waiting messsage")
#     data, addr = udpSerSock.recvfrom(BUFSIZE)
#     udpSerSock.sendto(b'[%s] %s' % (bytes(ctime(), 'utf-8'), data), addr)
#     print('... recieved from returned to: ', addr)
#
