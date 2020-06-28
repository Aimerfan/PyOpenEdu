## -*- coding: utf-8 -*-
#"""
#Created on Tue Apr 14 20:45:59 2020
#
#@author: user
#"""
#
#class Dog:
#    def __init__(self, func):
#        self.a = 7
#        self.function = func
#    
#    def __call__(self, *args, **kwargs): 
#        
#        result = self.function(*args, **kwargs)     
#        
#        return result 
#        
#
#    def bark(self):
#        print("Bark !!!")
#
#
#@Dog
#def dog_can_pee(a,b):
#    print("I can pee very hard......",a,b)
#
#
#@Dog
#def dog_can_jump():
#    print("I can jump uselessly QQQ")
#
#
#@Dog
#def dog_can_poo():
#    print("I can poo like a super pooping machine!")
#
#
#
#if __name__ == "__main__":
#    
#    dog_can_pee(7,"abc")
#    
##    dog_1 = dog_can_pee(7)
##    dog_1.a
##    dog_1.talent()
#    # > I can pee very hard......
#
#    dog_2 = dog_can_jump
#    dog_2.function()
#    # > I can jump uselessly QQQ
#
#    dog_3 = dog_can_poo
#    dog_3.function()
#    # > I can poo like a super pooping machine!
#    
#   
#from functools import wraps, partial
class testa():
    
    def use_logging(func):
        def wrapper(self, *a,**dic):
        
            return func(self, *a, **dic)   # 把 foo 当做参数传递进来时，执行func()就相当于执行foo()
        return wrapper
    
@testa.use_logging
def foo(a,b):
    print('i am foo',a,b)

t = testa()
#
#t.use_logging(foo(10,[0,1,2]))
foo(10,[0,1,2])
