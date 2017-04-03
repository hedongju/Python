from socket import *
host = '192.168.0.107'
port = 20567
BUFSIZE = 1024
addr = (host,port)

tcpClient = socket(AF_INET,SOCK_STREAM)
tcpClient.connect(addr)

while True:
    data = raw_input('>>>   ')
    if not data:
        break
    tcpClient.send(data)
    data = tcpClient.recv(BUFSIZE)
    print data

tcpClient.close()
