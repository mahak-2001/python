# variables:-
# swap two variables without third variable.
a=10
b=20
a,b=b,a
print(a,b)
#read name and age and print formatted output.
name=input("enter the name:")
age=int(input("enter the age:"))
#calculate area of rectangle.
l=90
b=80
area=l*b
print("area of rectangle is:",area)

#string:
#count vowel:
str="my name is mahak"
count=0
for i in str:
 if i in ("aeiou"):
    count=count+1
print(count)

#reverse string.
str1="this is python program"
print(str1[::-1])
# check palindrome:
name="maam"
if(name==name[::-1]):
    print("this is palindrome")
else:
    print("this is not palindrome")
#count words:
str2="this is basic test question"
words=str2.split()
print(len(words))
#replace space with hyphens:
text="hello world python"
print(text.replace(" ","-"))

# lists
#sum list
list=[1,6,8,4,3]
print(sum(list))
#largest/smallest no.
print(max(list))
print(min(list))
#remove duplicates.
list1=[1,1,2,3,4,3,2,1]
list2=set(list1)
print(list2)
#second largest no.
list.sort()
print(list[-2])
#merge two list:
x=[1,2,3]
y=[4,5,6]
x.extend(y)
print(x)
# print(x+y) (other method)

#tuple
#count occurance
tuple=(1,2,3,4,3,2,1,1,1,1,4)
print(tuple.count(1))
#convert tuple to list and append
new=list(tuple)
new.append(7)
print(max(new))
print(new)

#set
#union/intersection:
set={1,2,3,4,5,4,3}
set1={3,5,6,7}
print(set.intersection(set1))
print(set.union(set1))
# difference
print(set.difference(set1))
#check subset:
print(set1.issubset(set))

#dictionaries


