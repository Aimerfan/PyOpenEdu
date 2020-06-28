from PyOpenEdu import OpenEdu
import pandas as pd
from Config import Config
from Data import DataProcess
from Loader import Loader 
import filter_data as fd


#import types
#
#class StrategyExample:
#   def __init__(self, func = None):
#      self.name = 'Strategy Example 0'
#      if func is not None:
#         self.execute = types.MethodType(func, self)
#
#   def execute(self):
#      print(self.name)
#
#def execute_replacement1(self): 
#    print(self.name + 'from execute 1', )
#
#def execute_replacement2(self):
#    print(self.name + 'from execute 2')
#
#if __name__ == '__main__':
#   strat0 = StrategyExample()
#   strat1 = StrategyExample(execute_replacement1)
#   strat1.name = 'Strategy Example 1'
#   strat2 = StrategyExample(execute_replacement2)
#   strat2.name = 'Strategy Example 2'
#   strat0.execute()
#   strat1.execute()
#   strat2.execute()

openedu = OpenEdu()


a = openedu.load_csv('../log_data.csv')

DataProcess = DataProcess()
b = DataProcess.filter_data_function.filter_data_event_source(a,'serv')

c = DataProcess.filter_data_function.filter_data_bridge(b)

e = DataProcess.filter_data_function.filter_data_username(c,'Xi')

f = DataProcess.filter_data_function.filter_data_bridge(e)

#
#f = fd.filter_interface(a,'event_source','b')
#fd.filter_data_event_source(f.data,f.field,f.value)

import abc


class Abstraction:
    """
    Define the abstraction's interface.
    Maintain a reference to an object of type Implementor.
    """

    def __init__(self, imp):
        self._imp = imp

    def operation(self):
        self._imp.operation_imp()


class Implementor(metaclass=abc.ABCMeta):
    """
    Define the interface for implementation classes. This interface
    doesn't have to correspond exactly to Abstraction's interface; in
    fact the two interfaces can be quite different. Typically the
    Implementor interface provides only primitive operations, and
    Abstraction defines higher-level operations based on these
    primitives.
    """

    @abc.abstractmethod
    def operation_imp(self):
        pass


class ConcreteImplementorA(Implementor):
    """
    Implement the Implementor interface and define its concrete
    implementation.
    """

    def operation_imp(self):
        print('a')


class ConcreteImplementorB(Implementor):
    """
    Implement the Implementor interface and define its concrete
    implementation.
    """

    def operation_imp(self):
        print('b')


def main():
    concrete_implementor_a = ConcreteImplementorA()
    abstraction = Abstraction(concrete_implementor_a)
    abstraction.operation()


if __name__ == "__main__":
    main()
    








































