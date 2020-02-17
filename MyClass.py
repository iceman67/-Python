'''
class MyClass:
    pass
'''

class MyClass:
    def __init__(self, arg_1, arg_2, arg_3):
        self.x = arg_1
        self.y = arg_2
        self.z = arg_3
        print(f'an instance of {type(self).__name__} created')
        print(f'arg_1: {arg_1}, arg_2: {arg_2}, arg_3: {arg_3}')

# __call__ can be particularly useful in classes with instances that need to often change their state. the *vars argument can be used, which captures all arguments passed and stores them in a tuple, which can be unpacked as shown above.
    def __call__(self, *vars):
        self.x, self.y = vars

# create an instance of MyClass and assign the reference to it  to a new variable a
a = MyClass(2, 4, 8)
print (a)
print (type(a))
print (a.__class__.__name__)

print( vars(a))

a(200, 300)
print(a.__dict__)
print(id(a), '\n')
