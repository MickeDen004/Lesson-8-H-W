# Без аргументов и без возврата результата
def no_name():
    print()
print(no_name())
print()






# С одним позиционным обязятельным аргументом но без результата


# Без аргументов но с одним результатом
def text():
    print("This is my result!")
print(text())
print()







# Рандомная функция
def check_password(username, password):
    if len(password)<8:
        print("The password is too short")
        return False
    elif username in password:
        print('The password includes username')
        return False
    else:
        print(f"{username} password is valid")
        return True

print(check_password('nikit','uightredmx'))
print()








#С одним ключевым аргументом необязательным
def f(a=None):
    pass


def check_password_improved(username, password, min_length=8,check_username=True):
    if len(password) < min_length:
        print('This password is too short')
        return False
    elif check_username and username in password:
        print('Password includes username')
        return False
    else:
        print(f"{username}'s password is valid")
        return True

print(check_password_improved('nikit','jkiyhddds'))






# Которая возвращает несколько результатов

def my_hours(happy_hours):
    week1 = happy_hours + 3
    week2 = happy_hours + 2
    week3 = happy_hours + 8
    return[week1,week2,week3]

print(my_hours(4))

# С любым количеством позиционных аргументов
def my_tuple(*tup):
    return tup

print(my_tuple(1,2,3,4,5,6,7))

# С любым колчиеством ключевых аргументов
def my_dict(**rrrrr):
    return rrrrr
print(my_dict(x = 1, s = "s", vik = 'kiv'))
print()



# С любым колчиеством как позиционных так и ключевых аргументов
# Функция возвращающая функцию
def cylinder():
    r = float(input())
    h = float(input())
    # площадь боковой поверхности цилиндра:
    side = 2 * 3.14 * r * h
    # площадь одного основания цилиндра:
    circle = 3.14 * r ** 2
    # полная площадь цилиндра:
    full = side + 2 * circle
    return full


square = cylinder()
print(square)
# Функция принимающая функцию как аргумент
def newfunc(n):
     def myfunc(x):
        return x + n
     return myfunc
new = newfunc(100)
print(new(200))

# Анонимная функция (безимянная), можно использовать в map()
print(list(map(lambda n: n*2, [1,2,3,4,5])))

nums = [1,2,3,4,5]

print(list(map(lambda n: n%5, nums)))



def double(n):
    return n*2
nums = [1,2,3,4,5]
print(list(map(double, nums)))