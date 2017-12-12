def tracer(classname, supers, classdict):

    aClass = type(classname, supers, classdict)

    return aClass


class Person(metaclass=tracer):

    def __init__(self, name, hours, rate):
        print('Person.INIT')
        self.name = name
        self.hours = hours
        self.rate = rate

    def pay(self):
        return self.hours * self.rate


bob = Person('Bob', 40, 50)
