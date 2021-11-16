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