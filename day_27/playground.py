from numpy.ma.core import multiply


# def add(*args):
#     print(args[0])
#
#     sum = 0
#     for n in args:
#         sum += n
#     return sum
#
# print(add(3, 5, 6))

# def calculate(n, **kwargs):
#     for key, value in kwargs.items():
#         print(key, value)
#     n += kwargs['add']
#     n *= kwargs['multiply']
#     print(n)
#
# calculate(2, add = 3, multiply = 5)

class Car:
    def __init__(self,mat, **kw):
        self.make = kw.get('make')
        self.model = kw.get('model')
        self.material = mat

my_car = Car(make = 'Nissan', mat = 'Metal')
print(my_car.material)