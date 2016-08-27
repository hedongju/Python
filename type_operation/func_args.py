#!/usr/bin/python
def func(a, b, c, d):print(a, b, c, d)
args = (1, 2)
args += (3, 4)
func(*args)
