# a collection of instructions
# a collection of code

def function1():
    print("ahhhh")
    print("aaahahhaha 2")
print(f"This is outside the function, and tis is inside the function{function1()}")

# a mapping
def  function2(x):
    return 2*x
a = function2(3)
print(a)
def function3(x, y):
    return x+y

e = function3(1,2)
print(e)
print()

def function4(x):
    print(x)
    print("still in the function")
    return 3*x
f = function4(4)
print(f)
def function5(some_arg):
    print(some_arg)
    print("weeeee")
print(function5(4))


# BMI calculator
name1 = "YK"
height_m1 = 2
weight_kg1 = 90

name2 = "YK's sister"
height_m2 = 1.3
weight_kg2 = 23

name3 = "YK's brother"
height_m3 = 1.88
weight_kg3 = 88

def bmi_calculator(name, height_m, weight_kg):
    bmi = weight_kg / (height_m **2)
    print("bmi: ")
    print(bmi)
    if bmi < 25:
        return name + " not overweight "
    else:
        return name + " is overweight"

result1 = bmi_calculator(name1, height_m1, weight_kg1)
print(result1)

