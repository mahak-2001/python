#set=unordered collection of unique elements.
#unordered:no index fix
# mutable
# not allow duplication elements:if we write so its not print.
#set element must be immutable type such as numbers,string,or tuples.
#syntax
# variable={value,value1}
x={}
print(type(x))
empty=set()
print(type(empty))
values={1,3,4.5,True,"mahak"}#if we take 1,0 and bool value ,so only 1st existance 
print("mahak" in values)
print(1 not in values)
for y in values:
   print(y)
values.add(56)
print(values)
set1={1,2,3,4}
set2={5,6,7,8}
set1.update([7,8,10])
print(set1)
#we use discard for removing error if any element is not present in set so it helps removing unnessary error
set1.discard(9)
print(set1)
set1.remove(8)
print(set1)
del set1
#update,intersection,union and other methods
s={1,2,3,4,5}
s1={4,5,6,7,8}
# s.update(s1)
# print(s)
print(s.union(s1))
print(s.intersection(s1))
print(s.difference(s1))
print(s.symmetric_difference(s1))

x={1,2,3,4,5}
x1={6,7,8}
#issubset:all elements of the first set are in the second set.
print(x.issubset(x1))
#issuperset: the first set contains all elements of the second set.
print(x.issuperset(x1))
#disjoint:the two sets share no elements.or all different elements will be store.
print(x.isdisjoint(x1))
x.add(8)
print(x)
y={1,2,3}
z=(4,5,6)
y.update(z)
print(y)
print(max(y))
print(sum(y))

#for removing duplicate values in any data type.
email=["mahak@gmail.com","ram@gmail.com","syam@gmail.com","mahak@gmail.com"]
new_email=set(email)
print(new_email)
