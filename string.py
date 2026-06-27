print("hello guyzz")
a=5
b=7
c=a+b
print(c)
#multiple element in single variable
fruits="apple","papaya","orange"
print(fruits)
f1,f2,f3=fruits
print(f2)
#user input line
name=input("my name is:")
print("hello",name)
#scope:local scope:-
def function():
    print("name")
function()
#local scope convert into global scope:
def show():
    global name
    name="jiya"
show()
print(name)
#gobal and local
age=20
def my_function():
    age=18
    print(age)
my_function()
print(age)
#data type
a=20
b=20.9
#type of data
print(type(a))
#convert int to float
c=complex(a)
print(c)
#length of data
p="hello this is my 1st python program"
print(len(p))
#indexing for search specific index value
print (p[4])
#slice method(start,stop,start)
print(p[2:9])
print(p[:10])
#backward printing(indexing start with 1)
print(p[-15:-2])
#replace any word
print(p.replace("python","java"))
#checking any word is present or not in string
print("python" in p) 
print("python" not in p)
#check with condition
if("python" in p):
 print(" python present in p")
else:
   print(" python not present in p")
#condition elements
x=6
y=6.5
print(x==y)
print(x==int(y))


#list programs
colors=["red","yellow","orange"]
print(colors)
print(type(colors))
#index access
print(colors[2])
#add new elements
colors.append("black")
print(colors)
#remove any elements
colors.remove("red")
print(colors)