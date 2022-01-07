#Генератор лет
years = [i for i in range(1990, 2051)]
def list_years():
    for y in years:
        yield y
print(list_years())
# gen = list_years()
# for y in gen:
#     print(y)

#Age Gen
age = [a for a in range(0, 121)]
def list_age():
    for a in age:
        yield a

print(list_age())
# gen = list_age()
# for a in gen:
#     print(a)


#Height Gen
height = [h for h in range(10, 301)]
def list_height():
    for h in height:
        yield h
print(list_height())


#Option 2

years2 = (i for i in range(1990, 2051))
age2 = (a for a in range(0, 121))
height2 = (h for h in range(10,300))
alist = (years2, age2, height2)
print(alist)
print()
for item in alist:
    print(list(item))