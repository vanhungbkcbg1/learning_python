import student
from OOP import *

studentIntance=student.Student('vanhung')
print studentIntance.getName()
# or using methos bellow to access attributed in object

print getattr(studentIntance,'name')
# delete attribute
delattr(studentIntance,'name')

print studentIntance.name

if(hasattr(studentIntance,'name')):
    print 'has name in object'
else:
    print 'no name in object'

print studentIntance

child=Child()
child.test()

child.getName()