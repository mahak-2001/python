#tuples:createimmutable sequence of values.
tup=(1,2,3,4)
print(type(tup))
tupl=(1,)#if we cannot use comma so it count as integer in python
print(tupl)

#METHODS:
tup=(1,2,3,4,2,2)
print(tup.index(2))
print(tup.count(2))

#test
movies=[]
mov1=input("enter movie: ")
mov2=input("enter movie: ")
mov3=input("enter movie: ")
movies.append(mov1)
movies.append(mov2)
movies.append(mov3)
print(movies)
#another method:
fruit=[]
fruit.append(input("enter 1st fruit: "))
fruit.append(input("enter 2nd fruit: "))
fruit.append(input("enter 3rd fruit: "))
print(fruit)
