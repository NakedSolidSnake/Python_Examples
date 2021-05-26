#!/usr/bin/python3

import socket

HOST = '127.0.0.1'
PORT = 5000

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
dest = (HOST, PORT)

msg = input().encode()

while msg != '\x18':
    udp.sendto(msg, dest)
    msg = input().encode()

udp.close()