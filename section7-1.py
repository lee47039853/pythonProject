# ------------------------------
# State Design Pattern
# ------------------------------
# Allow an object to alter its behavior when its internal state changes.
# The object will appear to change its class.

# https://github.com/rajan2275/Python-Design-Patterns/blob/master/Behavioral/state.py


from abc import ABC
from itertools import repeat


class State(ABC):
    def handle_state(self):
        pass

class StateA(State):
    def handle_state(self):
        print('State changed to StateA.')

class StateB(State):
    def handle_state(self):
        print('State changed to StateB.')

class StateC(State):
    def handle_state(self):
        print('State changed to StateC.')


class Context(State):
    def __init__(self):
        self.state = None

    def set_state(self, state):
        self.state = state

    def handle_state(self):
        self.state.handle_state()
    



context = Context()
stateA = StateA()
context.set_state(stateA)
context.handle_state()



print('-------------------------------------')

stateB = StateB()
context.set_state(stateB)
context.handle_state()

print('-------------------------------------')


def foo(a,b):
    """

    :param a: 나이
    :param b: 성별
    """
    pass



'''
class $class$($object$):
    """$cls_doc$"""

    def __init__(self,$args$):
        """Constructor for $class$"""
$END$

'''

'''
print($contents$)
$END$

'''







