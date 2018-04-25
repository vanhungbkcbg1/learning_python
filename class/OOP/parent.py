class Parent:

    __name=None
    def __init__(self,name):
        print 'parent'
        self.__name=name
    def test(self):
        print 'test'