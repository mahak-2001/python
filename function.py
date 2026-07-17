# function:
#make easier code
def greet(name):#name is parameter
    print("hello",name)
    print("welcome to python")
greet("mahak")#function call
greet("jiya")#jiya is argument

def say_hello():
    print("hello!")
say_hello()

def addition(a,b):
    print("sum",a+b)
addition(10,20)

def student_name(name,age,grade):
    print("name:",name)
    print("age:",age)
    print("grade:",grade)
student_name("mahak",20,"BCA")

#DEFAULT PARAMETER have predefined value.
#if python
# def function(a,b,c=10):
#     print(a,b,c)
#     function(a=5,6)







def calculate(a,b):
        return a+b,a-b,a*b
x,y,z=calculate(3,4)
print(x,y,z)


def function(a,b=2):
     a=a+b
     b=a*b
     return a,b
x,y=function(3)
print(x+y)

def greet(name="mahak"):
     print("hello",name)
greet()

def f(x=2,y=3):
     return x+y
print(f(5))

def g(items):
     return[x*x for x in items if x%2==0]
print(g([1,2,3,4]))


def greet(name):
     print("hello",name)
result=greet("riya")
print(result)


def calculate(a,b):
     print(a+b)
     return a*b
reult=calculate(3,4)
print(result)

def test():
     return 5
print(10)
print(test())

def total(a,b=5,c=2):
     return a+b*c
print(total(3))

def total(a,b=5,c=2):
     return a+b*c
print(total(3,4))

def addition(first,second):
     return first+second
result=addition(10,20)


def message():
     return print("Python")
value=message()
print(value)

def calculate(a,b=2):
     a=a+b
     b=a*b
     return a,b
x,y=calculate(3)
print(x+y)


def operation(a,b):
     return a+b
def calculate(x):
     return operation(x,x*2)
print(calculate(4))


def compare(a,b=10):
     if a>b:
          return a 
     if a==b:
      return 0
     return b 
print(compare(10))


def show(number):
     print(number)
     value =show(5)
     print(value+2)


def statistics(a,b):
     return a+b,a*b,a-b
result=statistics(6,2)
print(result[1])
     
# def greet():
#      return "hello"
# print(Greet())

def one():
     return 1
def increase(number):
     return number+1
print(increase(increase(one())))

def check(number):
     if number>0:
          return "positive"
     return "non-positive"
print(check(0))

def first_even(numbers):
     for number in numbers:
          if number%2==0:
               return number
          return None
     print(first_even([1,3,6,8]))


def calculate(number):
     return number+1
print(calculate(calculate(2)+calculate(1)))

def message():
     return print("Python")
value=message()
print(value)

def operation(a,b):
     return a+b
def calculate(x):
     return operation(x,x*2)
print(calculate(4))

def compare(a,b=10):
     if a>b:
          return a
     if a==b:
       return 0
     return b
print(compare(10))

# def addition(a,b):
#      return a+b
# print(addition(10))

def calculate(a,b=3,c=4):
     return a*b-c
print(calculate(5,c=2))

#*args store multiple positional argument as a tuple
def add_numbers(*numbers):
     total=0
     for num in numbers:
          total += num
          return total
print(add_numbers(1,2))
print(add_numbers(5,10,15,20))


def show_names(*names):
       for name in names:
             print(name)
show_names("mahak","jiya","teena")

def show_names(greet,*names):
       for name in names:
             print(greet,name)
show_names("hello","mahak","jiya","teena")

#add ** when work with keyword and print as a dict.
def show_details(**details):
      for key,value in details.items():
            print(key,":",value)
show_details(name="rohit",age=20,city="pune")

def show_details(**details1):
      for key,value in details1.items():
            print(key,value)
show_details(name="rohit",age=20,city="pune")

def create_profile(**user):
      print("user profile")
      print("Name:",user.get("name"))
      print("Age:",user.get("age"))
      print("Email:",user.get("email"))
create_profile(name="sneha",age=25,email="sneha66@gmail.com")

count=0
def increase():
      global count
      count+=1
increase()
increase()

print(count)

def square(number):
      """
      this function return square of a number
      """
      return number * number
print(square(5))
print(square.__doc__)

#typein
def add(a: int,b:int)->int:
      return a+b
print(add(10,20))

#mix

#lambda function
#it is a small anonymous function.
#it is usually used for shot operation.
#sytax 
# lambda arrgument:expression
square=lambda x:x*x
print(square(6))


add=lambda a,b:a+b
print(add(3,4))

#map,filter,sorted

def find_largest(numbers):
      largest=numbers[0]
      for number in numbers:
            if number>largest:
                  largest=number
marks=[67,76,4,3]
print(find_largest(marks))
