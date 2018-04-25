import module
from module import test as A
from module import doSomething as something
import sys

module.test()
A()
something()

print sys.path