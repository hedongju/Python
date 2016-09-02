##!/usr/bin/python
def gen();
for i in range(10):
    X = yield i
    print(X)

G = gen()
