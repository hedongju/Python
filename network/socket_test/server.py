from socket import *
from time import ctime

host = ''
port = 20567
BUFSIZE = 1024
addr = (host,port)

tcpServer = socket(AF_INET,SOCK_STREAM)
tcpServer.bind(addr)
tcpServer.listen(5)

while True:
    print 'waiting for connect....'
    tcpServer ,addr = tcpServer.accept()
    print '... connetcted from :',addr

    while True:
        data = tcpServer.recv(BUFSIZE)
        if not data:
            break
        tcpServer.send('[%s] %s'%(ctime(),data.upper()))
    tcpServer.close()
tcpServer.close()
