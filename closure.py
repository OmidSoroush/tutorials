def outer_func(msg):
    '''This is the outer function'''

    def inner_func():
        '''This is the nested function'''
        print(msg)

    return inner_func

another_func = outer_func('Hello')

another_func()

del outer_func

another_func()


def to_be_added(x):
    def add(y):
        return x + y
    return add

adding = to_be_added(10)

print(adding(5))
print(adding(20))

#creating parent class
class Car:

    def __init__(self,name,model):
        self.name=name
        self.model=model

    # function to print the car name
    def printname(self):
        print("The name of car is:",self.name)

    # function to print the car model
    def printmodel(self):
        print("The model of the car is:",self.model)
class VW(Car):

    def __init__(self):
        # calling and using the initialization function of Car
        Car.__init__(self, 'Tiguan', 2020)

vw = VW()

print('The name of car is:', vw.name)
print('The model of the car is:', vw.model)