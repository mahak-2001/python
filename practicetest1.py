#test1
##which of the following is a valid Python varible name?
#: 2value  ,  user-name   ,  _user2  ,  class

x=10
x=str(x)
print(x*2,type(x).__name__)
#1010str

value="5.8"
number=float(value)
print(int(number),bool(number),type(number).__name__)
#5 True float

x=10
def show():
    x=20
    print(x,end=" ")
show()
print(x)
#20 10

count=5
def update():
    global count
    count+=3
update()
print(count)
#8

text="Python"
print(text[1],text[-1],text[1:5:2])
#y n yh

text=" PyTHOn "
clean=text.strip()
print(clean.lower(),clean.upper())
#python PYTHON

text="banana"
print(text.replace("a","o",2),text.count("an"))
#bonona 2

text="red,green,blue"
parts=text.split(",")
print("-".join(parts),len(parts))
# red-green-blue 3

text="intern_python.py"
print(text.find("python"),text.startswith("intern"),text.endswith(".py"))
#7 True True

code="Python3"
year="2026"
print(code.isalpha(),code.isalnum(),year.isdigit())
#False True True

numbers=[1,2,3]
numbers.append([4,5])
print(numbers)
#[1,2,3,[4,5]]

numbers=[1,2,3]
numbers.extend((4,5))
print(numbers)
#[1,2,3,4,5]

values=[10,30]
values.insert(1,20)
print(values)
#[10,20,30]

numbers=[1,2,3,2]
numbers.remove(2)
print(numbers)
#[1,3,2]

numbers=[10,20,30]
value=numbers.pop(1)
print(value,numbers)
#20[10,30]

numbers=[3,1,2]
result=numbers.sort()
print(result,numbers)
#none [1,2,3]

values=[1,2,3]
values.reverse()
print(values)
#[3,2,1]

a=[10,20]
b=a
c=a.copy()
b.append(30)
c.append(40)
print(a,c)
#[10,20,30][10,20,40]

result=[x**2 for x in range(1,6)if x%2==0]
print(result)
#[4,16]

# data=(10,20,30)
# data[0]=100
# #a type error occurs

data=(1,2,[3])
data[2].append(4)
print(data)
#(1,2,[3,4])

data=(1,2)
extra=[3,4]
data=data+tuple(extra)
print(data)
#(1,2,3,4)

a,b,*c=(1,2,3,4)
print(a,b,c)
#1 2 [3,4]

data=(1,2,1,3)
print(data.count(1),data.index(3))
#2 3

values={1,1,2,3,3}
print(len(values))
#3

values={1,2}
values.add(3)
print(len(values),3 in values)
#3 True

values={1,2}
values.add((3,4))
print(len(values),(3,4)in values)
#3 True

# values={1,2}
# values.add([3,4])
# print(values)
# #TypeError occurs because a list is unhasable

values={1,2}
values.update([2,3,4])
print(len(values),4 in values)
#4 True
values=set()
values.add("ab")
print(len(values),"a" in values,"ab" in values)
#1 False True