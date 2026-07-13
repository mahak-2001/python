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
