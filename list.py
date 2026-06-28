#list is build-in-data type that stores set of values
#it can store elements of different types(int,float,string,etc.)
#it is ordered,mutable collection of items.it can hold elements of different data types,and it allow duplicate value
#key properties:
  #ordered-items have a defined position(index),and that order is preserved.
  #mutable-you can change,add,remove items after the list is created.
  #heterogeneous-a single list can mix data types.
  #allow duplicates-the same value can apper multipe times
marks=[39.6,75.6,85.6,75.8,86.7]
print(marks)
#type
print(type(marks))
#length
print(len(marks))

#indexing value
print(marks[3])
print(marks[0])

#list store different types of elements:
student=["karan",85,"delhi"]
print(student)

#change any index element
student[0]="mahak"
print(student)

#list slicing
number=[46,67,78,47,76,93]
print(number[1:5])
print(number[-4:-1])

#methods
list=[64.76,94,63,84,99,77,55]
list.append(88)#add one element at the end
print(list)

print(list.sort())#sort in ascending order
print(list)
list.sort(reverse=True)#sort in descending order
print(list)

#reverse the number
b=[3,4,2,5,1,6]
b.reverse()
print(b)

#insert a new value (variable,insert(index,element))
a=[8,4,3,3,9,5,5]
a.insert(2,7)
print(a)

#remove an element(var.remove(element))
a.remove(5)
print(a)
#pop an element(var.pop(index))
a.pop(5)
print(a)