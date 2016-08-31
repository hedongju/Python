#!/usr/bin/python3
# File makedb.py: staore Person objects on a shelve database
from person import Person, Manager
bob = Person('Bob Smith')
sue = Person('Sue Jones', job = 'dev', pay = 10000)
tom = Manager('Tom Jones', 50000)

import shelve
db = shelve.open('persondb')
for object in (bob, sue, tom):
    db[object.name] = object
db.close()
