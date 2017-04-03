#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright 漏 2017 hedj <hedj@hedj-virtual-machine>
#
# Distributed under terms of the MIT license.

"""

"""
import sys,socket
host = sys.argv[1]
port = 70
filename = sys.argv[2]
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((host,port))
s.sendall(filename + '\r\n')

while True:
    buf = s.recv(2048)
    if not len(buf):
        break
    sys.stdout.write(buf)
s.close()
