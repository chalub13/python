r = range(30)
print(type(r))
print(type(1))
print(type("a"))
print(type("Hi there"))


class Car:
    pass


class Truck:
    pass


c = Car()
covert = Car()
t = Truck()
print(type(c))
print(type(t))
print(type(c) == type(t))
print(type(c) == type(covert))

print(isinstance(c, Car))
print(isinstance(t, Car))

if isinstance(r, range):
    print(list(r))

