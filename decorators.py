def multiply_by_five(x):

    print(x * 5)

five_times = multiply_by_five

five_times(4)


def outer_func(msg):
    '''This is the enclosing function'''

    def inner_func():
        '''This is the nested function'''

        print(msg)

    return inner_func

my_python = outer_func('Python has a lot of features')

my_python()


def add_ten(num):
    return num +10

def my_func(func, x):
    return func(x)

print(my_func(add_ten, 5))


def uppercase_deco(func):
    def wrapper():
        convert_to_uppercase = func().upper()
        return convert_to_uppercase

    return wrapper

def my_name():
    return 'my name is Johnny'

decorate = uppercase_deco(my_name)
print(decorate())

@uppercase_deco
def my_name():
    return 'my name is Johnny'

print(my_name())


def my_decorator(func):

    def wrapper(name, city):
        print('length of name is', len(name))
        print('length of city is', len(city))
        return func(name, city)

    return wrapper


@my_decorator
def about_me(name, city):
    print(f'my name is {name}, and I live in {city}')

about_me('Scott', 'Berlin')

def general_purpose_deco(func):

    def wrapper(*args, **kwargs):
        # code to be executed before the function
        return func(*args, **kwargs)
        # code to be executed after the function
    return wrapper