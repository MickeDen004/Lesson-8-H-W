# Basic function
def add(x,y):
    return x + y


print(add(4, 7))
print()

def newfunction(n):
    def myfunc(x):
        return x + n
    return myfunc

new = newfunction(230)
print(new(200))
print()

def first(f):
    def second(s):
        return f + s
    return second
sum = first(300)
print(sum(23))

def func(*mytuple):
    return mytuple
print(func(1, 2, 3, "abc"))
print()
def func2(**mydict):
    return mydict
print(func2(wolf="Wilk", bear="Niedźwiedź"))
print()
def print_sum(a=2, b=3):
    sum = a + b
    print(sum)
print_sum(5,1)
def adder(x, y, z):
    print ("sum:", x + y + z)

print(adder(10, 20, 30))
print()


# *args
def adders(*nums):
    sum = 0

    for n in nums:
        sum += n

    print("Sum: ", sum)

print(adders(3,5))
print(adders(3,5, 7, 90))
print(adders(3,5, 4, 5, 6, 7, 2 ,6,6))

# **kwargs

def intro(**data):
    print("\nData type of argument: ", type(data))

    for key, value in data.items():
        print("{} is {}".format(key, value))

intro(Firstname="Salem", Lastname="Alyonovich", age="Unknown, perhaps infinity", phone="Unknown" )
