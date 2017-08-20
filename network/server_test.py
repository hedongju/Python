#!/usr/bin/env python
import socket
s = socket.socket()
host = socket.gethostname()
port = 8088
s.bind(("192.168.0.105",8088))
s.listen(5)
while True:
    c,addr = s.accept()
    print 'Got connection from',addr
    c.send('Thank you for connection')
    c.close()
