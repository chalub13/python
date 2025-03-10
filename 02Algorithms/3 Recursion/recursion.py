# Using recursion to implement power and factorial functions

# example 2^4 = 2*2*2*2 = 16
def power(num, pwr):
    if pwr == 1:
        return num
    else:
        return num * power(num, pwr - 1)


# example 5! = 5*4*3*2*1 = 120
def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)


print("{} to the power of {} is {}".format(5, 3, power(5, 3)))
print("{} to the power of {} is {}".format(1, 5, power(1, 5)))
print("{} to the power of {} is {}".format(2, 4, power(2, 4)))
print("{}! is {}".format(4, factorial(4)))
print("{}! is {}".format(5, factorial(5)))
print("{}! is {}".format(0, factorial(0)))
