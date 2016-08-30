#!/usr/bin/python3
# Add methods to encapsulate operations for maintainability
class Person:
    def __init__(self, name, job = None, pay = 0):
        self.name = name
        self.job = job
        self.pay = pay
    def lastName(self):
        return self.name.split()[-1]
    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))

if __name__ == '__main__':
    # self-test code
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job = 'dev', pay = 10000)
    print(bob.name, bob.pay)
    print(sue.name, sue.pay)

    print(bob.lastName(), sue.lastName())
    print(sue.pay)
