# #variable 
# name="mahak"
# print("hello,python!",name)

# x=int(input("enter value of x:"))
# y=int(input("enter value of y:"))
# print("sum",x+y)
# print("sub",x-y)
# print("mul",x*y)

# #condition
# z=20
# if(z%2==0):
#     print("value is even.")
# else:
#     print("value is odd")

# #string
# str="hello my self mahak"
# str1=str[::-1]
# print(str1)

# #count
# count=0
# for i in str:
#     if i in ("aeiou"):
#         count=count+1
# print(count)

# #remove duplicates from a list.
# value=[1,2,3,2,3,4,6,6,7,8]
# value1=set(value)
# value=list(value1)
# print(value)

#second largest no.
# number=[4,3,5,1,7,8,9,1]
# number.sort()
# print(number[-2])

#merge 2 dict,if keys overlap.
person={"name":"mahak","course":"python"}
person1={"name":"jiya"}
person.update(person1)
print(person)

#palindrome
text="mam"
if text==text[::-1]:
   print("yes it is palindrome")
else:
 print("no it is palindrome")

# list of tuple into a dict.
list=[("name","mahak"),("age",20)]
dict1=dict(list)
print(dict1)

# common element of two set:
set={1,2,3,4,5,6}
set1={4,5}
print(set.intersection(set1))

#count frequency of characters in a string.
word={"name":"mahak"}
print(word.count("a"))