#!/usr/bin/env python
import socket
s = socket.socket()
host = socket.gethostname()
port = 8088

s.connect(("192.168.0.105",port))
print s.recv(1024)
