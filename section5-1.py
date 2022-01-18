# encapsulation-2.py

# This example builds on top of `encapsulation-1.py`.
# Here we see how we can set values in methods without
# going through the method itself, ie.. how we can break
# encapsulation.
# https://github.com/arvimal/Python-and-OOP/blob/master/02-encapsulation-2.py

# NOTE: BREAKING ENCAPSULATION IS BAD.
from abc import ABCMeta, abstractmethod

I_NUMBER = 10


class MyClassParant(object, metaclass=ABCMeta):
    def __init__(self):
        pass

    @abstractmethod
    def set_val(self, val):
        pass

    @abstractmethod
    def get_val(self):
        pass

    @abstractmethod
    def print_test(self, i):
        pass


class MyClass(MyClassParant):
    def set_val(self, val):
        self.value = val

    def get_val(self):
        print(self.value)

    def print_test(self, i=10):
        print(i)
        print(i)
        print(i)


a = MyClass()
b = MyClass()
c = I_NUMBER

a.set_val(10)
b.set_val(1000)
a.value = 100    # <== Overriding `set_value` directly
# <== ie..  Breaking encapsulation

a.get_val()
b.get_val()
a.print_test()