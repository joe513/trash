class Person:

    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay

    def lastName(self):
        return self.name.split()[-1]

    def giveRaise(self, percent):
        self.pay = int(self.pay*(1+percent))

    def __str__(self):
        return '[Person: %s, %s]'%(self.name,self.pay)


class Ron(Person):
    '''
    Hello
    '''
    def giveRaise(self, percent, hello):
        self.pay = percent+hello


g = Ron('alex')
print(g.__dict__)
print(Ron.__dict__)
x = {}
print(x.__doc__)

