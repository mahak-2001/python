# #tuples:create immutable sequence of values.
tup=(1,2,3,4)
print(type(tup))
tupl=(1,)#if we cannot use comma so it count as integer in python
print(tupl)

# #METHODS:
tup=(1,2,3,4,2,2)
print(tup.index(1))#index(element)
print(tup.count(2))#count(element)
#test
# movies=[]
# mov1=input("enter movie: ")
# mov2=input("enter movie: ")
# mov3=input("enter movie: ")
# movies.append(mov1)
# movies.append(mov2)
# movies.append(mov3)
# print(movies)
 #another method:
# fruit=[]
# fruit.append(input("enter 1st fruit: "))
# fruit.append(input("enter 2nd fruit: "))
# fruit.append(input("enter 3rd fruit: "))
# print(fruit)

t=("mahak",24,"python")
x=list(t)
print(x)
#x.insert(1,"m")
print(x.append(11))
t=tuple(x)
print(t)

z=[1,2,[5,6,7,8,],9,3,]
print(len(z))

mix=("mahak",3,15.5,[1,2,3],True,3)
print(mix)
a=list(mix)
a.pop()
print(a)
mix=tuple(a)
print(mix)
y=2*mix
print(y)
num=(1,)
print(type(num))
a=(1,2,3,4)
b=(5,6,7,8)
c=a+b
print(c)
number=((1,2),(3,4),5,6,7,4,7,8,3)
#we use * for assign remaining value to single variable
#n1,n2,*n3=number
#print(n3)
#print(n1)
n1,n2,n3,*n4=number
print(n3)
print(n4)
t=(1,2,3,2,4,5,7,8,2,3,4,5,6)
m=t.index(2)
m2=t.index(2,m+1)
print(m2)