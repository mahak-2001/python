# function:
#make easier code
# def greet(name):#name is parameter
#     print("hello",name)
#     print("welcome to python")
# greet("mahak")#function call
# greet("jiya")#jiya is argument

# def say_hello():
#     print("hello!")
# say_hello()

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

