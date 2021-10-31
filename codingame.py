

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def instancemethod(self, word):
        print('I am', self.name, 'and I can say', word)

    @classmethod
    def classmethod(cls, name, birth_year):
        return cls(name, birth_year)

    @staticmethod
    def staticmethod():
        print('static method called')


print(Person.classmethod('jjj', 33))
obj = Person('John', 33)
obj.instancemethod('hi')



class Employee:
    car_name = 'Bla Car'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def change_car(cls, car_name):
        cls.car_name = car_name

    # instance method
    def display(self):
        print(self.name, self.age, 'Car:', Employee.car_name)

jessica = Employee('jessica', 30)
jessica.display()

# change car_name
Employee.change_car('BMW')
jessica.display()


class Employee:
    def __init__(self, name, salary):
        self.name=name
        self.salary= salary
    def __str__(self):
        return 'Employee(x=' + self.name + ' salary=$'+str(self.salary)+')'

emp = Employee('John', 1500)
print(str(emp))
print(emp.__str__())

import datetime as dt
today = dt.datetime.now()
print('the output of str():', str(today))
print('the output of repr():', repr(today))


class MyClass:
    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        return MyClass(self.num + other.num)


a = MyClass(40)
b = MyClass(2)
c = a + b
print(c.num)



class MyClass:
    def __init__(self, lst):
        self.lst = lst
    def __len__(self):
        return len(self.lst)
instance = MyClass([10, 20, 30, 40])
print(len(instance))


import statistics

data = [21, 29, 31, 21, 19, 46, 19]
variance = statistics.variance(data)

print(variance)


def variance(data):
    n = len(data)

    mean = sum(data) / n

    sq_deviation = [(x - mean) ** 2 for x in data]

    variance = sum(sq_deviation) / (n -1)
    return variance

data = [21, 29, 31, 21, 19, 46, 19]
print(variance(data))



import statistics

data = [1, 8, 6, 5, 4, 8, 8, 9, 2, 5]

print(statistics.stdev(data))


import math


def variance(data):
    n = len(data)
    mean = sum(data) / n
    return sum((x - mean) ** 2 for x in data) / (n-1)


def stdev(data):
    var = variance(data)
    std_dev = math.sqrt(var)
    return std_dev

print(stdev([21, 29, 31, 21, 19, 46, 19]))


data = [1, 8, 6, 5, 4, 8, 8, 9, 2, 5]

range = max(data) - min(data)

print(range)

import numpy as np

data = [21, 29, 31, 21, 19, 46, 19]

Q1 = np.percentile(data, 25, interpolation = 'midpoint')

Q3 = np.percentile(data, 75, interpolation = 'midpoint')

IQR = Q3 - Q1

print(IQR)

import numpy as np

def outlier_treatment(datacolumn):
    sorted(datacolumn)
    Q1,Q3 = np.percentile(datacolumn , [25,75])
    IQR = Q3 - Q1
    return IQR

data = [21, 29, 31, 21, 19, 46, 19]
print(outlier_treatment(data))


import numpy as np

def IQR(data):
    sorted(data)
    Q1,Q3 = np.percentile(data , [25,75])
    IQR = Q3 - Q1
    return IQR

data = [21, 29, 31, 21, 19, 46, 19]
print(IQR(data))


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

class Audi(Car):
    pass

A1 = Audi('e-tron', 2018)
A1.printname()

class VW(Car):

    def __init__(self):
        # calling and using the initialization function of Car
        Car.__init__(self, 'Tiguan', 2020)

vw = VW()
vw.printname()
vw.printmodel()


class Audi(Car):

    def new_method(self):
        print('I have got more skills than my parent')

A1 = Audi('e-tron', 2018)
A1.new_method()




#creating parent class
class Car:

    def __init__(self,name,model, ecofriendly=True):
        self.name=name
        self.model=model
        self.ecofriendly=ecofriendly

    def turbo(self):
        print("I have turbo functionality")

    # function to print the car model
    def printmodel(self):
        print("The model of the car is:",self.model)



class VW(Car):

    def __init__(self, name, model=2017, ecofriendly=False):
        self.name = name
        self.model = model
        self.ecofriendly = ecofriendly

    def turbo(self):
        print("I am fast but not too fast")

vw = VW('Tiguan')
vw.model
vw.turbo()
vw.printmodel()



#creating parent class
class Car:

    def __init__(self,name='unknown' ,model='unknown' , ecofriendly=True):
        self.name=name
        self.model=model
        self.ecofriendly=ecofriendly

    def turbo(self):
        print("I have turbo functionality")

    # function to print the car model
    def printmodel(self):
        print("The model of the car is:",self.model)

class VW(Car):

    def __init__(self, price='budget'):
        self.price = price
        super().__init__(self)

vw = VW()

print(vw.price)
vw.turbo()
vw.printmodel()




class John:

    def own(self):
        print("John owns three cars")

class Sarah:

    def fix_car(self):
        print("Sarah knows how to fix cars")

class Business(John, Sarah):
    pass

operation = Business()
operation.own()
operation.fix_car()


nums = [1, 2, 3, 4]

for num in nums:
    print(num)

dir(nums_iterator)

nums_iterator = iter(nums)

print(next(nums_iterator))
print(next(nums_iterator))
print(next(nums_iterator))
print(next(nums_iterator))
print(next(nums_iterator))

import inspect

help(list)


class MyCustomIterable:
    def __init__(self, start, end):
        self.current = start - 1
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        self.current += 1
        if self.current < self.end:
            return self.current
        raise StopIteration


for i in MyCustomIterable(5, 9):
    print(i)