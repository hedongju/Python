from socket import *
from time import ctime
import os

host = ''
port = 20567
BUFSIZE = 1024
addr = (host,port)

tcpServer = socket(AF_INET,SOCK_STREAM)
tcpServer.bind(addr)
tcpServer.listen(5)

def getStatusoutput(cmd):
    info = os.popen(cmd)
    info_text = info.read()
    info_status = info.close()
    return info_text,info_status
while True:
    print 'waiting for connect....'
    tcpServer ,addr = tcpServer.accept()
    print '... connetcted from :',addr

    while True:
        data = tcpServer.recv(BUFSIZE)
        if not data:
            break
        text,status = getStatusoutput(data.strip()) 
        if not status:
            tcpServer.send(text)
        else:
            tcpServer.send('error:cmd')
    tcpServer.close()
tcpServer.close()
