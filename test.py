python={"mahak","jiya","twinkle","jaanvi"}
sql={"preeti","deepika","mahak","rinku"}
print(python.intersection(sql))
person={
    "person_1":{
        "name":"mahak",
        "course":"BCA"
    },
    "person_2":{
        "name":"ram",
        "course":"BBA"
    }
}
print(person["person_1"]["name"])
print(person["person_2"].get("email","not found"))


a=10
b=40
c=80
a,b,c=b,a,c
print(a,b,c)

#reverse a string without slicing
str="mahak rajput"
print(str[::-1])

#count vowels and constants in a string
vowels=0
constants=0
for i in str:
    if i in "aeiouAEIOU":
        vowels += 1
    else:
        constants += 1
print("Vowels:", vowels)
print("Constants:", constants)

#check if a string is palindrome or not
str1="mahak"
str2=str1[::-1]
if str1==str2:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")

#find largest and smallest element in a list
list1=[10,20,30,40,50]
print("Largest element:", max(list1))
print("Smallest element:", min(list1))

#remove duplicates from a list
list2=[1,2,3,4,5,1,2,3]
new_list=set(list2)
print("List after removing duplicates:", list(new_list))

#find the second largest element in a list
value=[2,1,3,7,5,2,2,4,8,9]
value.sort(reverse=True)
print("Second largest element:", value[1])

#count frequency of each element using dictionary
list3=[1,2,3,4,5,1,2,3]
print("Frequency of each element:")
frequency={}    
for i in list3:
    frequency[i] = frequency.get(i, 0) + 1
print(frequency)


#merge two dictionaries
dict1={"a":1,"b":2} 
dict2={"c":3,"d":4}
dict1.update(dict2)
print("Merged dictionary:", dict1)

#find common elements between two sets.
set1={1,2,3,4}
set2={3,4,5,6}
print(set1.intersection(set2))

#store student details in tuple and display them
student_details=("mahak","BCA",20)
print("Student Name:", student_details[0])
print("Student Course:", student_details[1])
print("Student Age:", student_details[2])








