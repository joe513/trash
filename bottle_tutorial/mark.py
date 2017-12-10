import re


class ObjectAnalysis:

    def __init__(self, obj):
        self.obj = obj

    def get_all_object_methods(self):

        patterner = re.compile('__(.*)__')

        self.methods = []

        for attr in dir(self.obj):

            if callable(getattr(self.obj, '%s'%attr)):
                if not re.match(patterner, str(attr)):
                    self.methods.append(attr)

        return self.methods


new = ObjectAnalysis(list((1, 2, 3)))

print(new.get_all_object_methods())
