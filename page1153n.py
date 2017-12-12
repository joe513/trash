import time

def timer(label='', trace=True):

    def onDecorator(func):

        def onCall(*args, **kargs):
            start = time.clock()
            result = func(*args, **kargs)
            elapsed = time.clock() - start
            onCall.alltime += elapsed
            if trace:
                print(label, elapsed)

            return result

        onCall.alltime = 0

        return onCall
    return onDecorator


class Person:

    def __init__(self, pay, name):
        self.name = name
        self.pay = pay

    @timer('Bomb: ')
    def giveRaise(self, percent):
        self.pay *= (1.0 + percent)


g = Person(10, 'George')
g.giveRaise(0.4)

