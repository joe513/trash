class MyList:

    def __init__(self, spisok):
        self.list = spisok[:]

    def __getattr__(self, item):
        return getattr(self.list, item)

    def __add__(self, other):
        print(MyList(self.list + other))
        return MyList(self.list + other)

    def __iter__(self):
        self.x = 0
        return self

    def __next__(self):
        try:
            retik = self.list[self.x]
            self.x += 1
        except IndexError:
            raise StopIteration

        return retik

    def __getitem__(self, item):
        return self.list[item]

    def __setitem__(self, key, value):
        self.list[key] = value

    def __repr__(self):
        return repr(self.list)

    def __mul__(self, other):
        return MyList(self.list * other)

    def __len__(self):
        return len(self.list)


class MyListSub(MyList):

    def __init__(self, spisok):
        MyList.__init__(self, spisok)

        # Счётчики!
        self.n__init__ = 0
        self.n__getattr__ = 0
        self.n__add__ = 0
        self.n__iter__ = 0
        self.n__getitem__ = 0
        self.n__setitem__ = 0
        self.n__repr__ = 0
        self.n__mul__ = 0
        self.n__len__ = 0
        self.n__next__ = 0

        self.common_number_of_calls = 0

    def display(self, name, number):
        self.common_number_of_calls += 1
        print('The %s operation is called already %s' % (name, number))

    def __getattr__(self, item):
        self.display('__getattr__', self.n__getattr__)
        self.n__getattr__ += 1
        MyList.__getattr__(self, item)

    def __add__(self, other):
        self.display('__add__', self.n__add__)
        self.n__add__ += 1
        return MyList.__add__(self, other)


my = MyListSub(['Nobody'])

print(my+['H'])

g = my+['J']

print(type(my+['H']))