import socket
import tkinter
import os


serv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=0)
serv_sock.bind(('192.168.0.104', 53210))  # Your IP and wanted port
serv_sock.listen(10)  # How many clients can wait for you


def tkinter_f():
    tkinter.Tk()
    tkinter.mainloop()


def hello_world():
    print("Hello world!")


actions = {"tkinter": tkinter_f, "exit": lambda: client_sock.close(), 'hello': hello_world}


while True:
    client_sock, client_addr = serv_sock.accept()

    print('Connected by', client_addr)

    while True:
        data = client_sock.recv(1024).decode('utf-8')

        if data in actions.keys():
            actions[data]()

        client_sock.send(b'I RECIEVED!')

    client_sock.close()
