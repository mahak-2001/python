text="I am mahak"
count=0
for i in text:
    if i in ("aeiou,AEIUO"):
        count+=1
        print(count)

print(text[::-1])
word="wow"
if (word==word[::-1]):
    print("it's a palindrome")
else:
      print("it's not a palindrome")

text="i am mahak. and i am here to learning python."
print(text.replace(" ","-"))
text1=text.split()
print(len(text1))

a=[1,2,3,4,5,6,7,8,9,10,1,2,3]
c=[11,12]
print(sum(a))
print(max(a))
print(min(a))
b=set(a)
a=list(b)
print(a)
d=a+c
print(d)

x=(1,2,3,7,4,3,1,9,54,2,5,8,9)
print(x.count(1))
print(max(x))
print(min(x))
y=list(x)
y.append(44)
print(y)

p={1,2,3,4,5,1,1}
q={1,2,3,4,5,6,7,8}
print(p.union(q))
print(p.intersection(q))
print(p.difference(q))
print(p.issubset(q))


marks={
     "math":50,
     "hindi":56,
     "english":57
}
mark1={
     "sci.":30,
     "ss":56,
     "eng.":54
}
# average=sum(marks.values())/len(marks)
# print(average,marks)
marks.update(mark1)
print(marks)
name=["mahak","anju","bhumi"]
name.sort()
print(name)
student=[("name","mahak"),("cousre","BCA")]
student1=[("name1","bhumi"),("class","12th")]
student_list=dict(student)
student_list1=dict(student1)
print(student_list,student_list1)
student_list.update(student_list1)
print(student_list)
text="mahak jiya teena neha mahak"
words=text.split()
unique=set(words)
print(len(unique))

for i in ("mahak"):
     print(i)