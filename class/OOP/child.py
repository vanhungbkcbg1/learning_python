from  parent import Parent
class Child(Parent):

    def __init__(self):
        Parent.__init__(self,"vanhung")
        print 'child'
    def test(self):
        print 'child'
    def getName(self):
        return  getattr(self,'name','No_name')
