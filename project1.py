print("i am Ruth")
print("o____")
print('  ||||')
print("*" * 10)
price = 10
price = 20
print(price)
name = input("what is your name? ")
print ('hi ' + name)
name = input("what is your name? ")
color = input("what is your favorite color? ")
print(name + ' likes ' + color)
birth_year = (input("Birth year: "))
print (type(birth_year))
age = 2019 - int(birth_year)
print(type(age))
print(age)
weight_lbs = input("Enter your weight in pounds: ")
weight_kgs = int(weight_lbs) * 0.45
print(weight_kgs)
course = "python for beginnners"
print(course)
print(course[0])
print(course[-1])
print(course[0:])
print(course[:5])
print(course[:])
email = '''
hi seline

thank you for enrolling to this course
enjoy your study

bye
'''

print (email)
name= input("Enter your name: ")
gender= input("enter your gender: ")
if gender.lower()=='female': 
    print(name.upper() +' youre a lady!')
elif gender.lower()=='male':
    print(name.upper() + ' youre a gent!')
else:
    print(name.upper() +' its complicated!')