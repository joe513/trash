class Wrap:

    def __init__(self, cls):
        self.klass = cls
        self.calls = 0

    def __call__(self, *args, **kwargs):
        self.calls += 1
        return self.klass(*args, **kwargs)


@Wrap
class Mine:

    def __init__(self, name):
        self.name = name

    def __call__(self, *args, **kwargs):
        print(*args)


@Wrap
def miner():
    print('Hello')


b = miner()
print(miner.calls)

class Be:
    def __init__(self):
        self.a = 10


food = Wrap(Be())
