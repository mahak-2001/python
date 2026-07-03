# dictionaries are used to store data values in key:value pairs.
# they are unordered,mutable &don't allow duplicate key.
 #syntax:
#dict={
#   key:value     }
#key cannot be duplicate if dulplicate so new key overhide its previous value and in elements(values) duplication is allow. 
person={
    "name":"mahak",
     "age":20,
     "course":"python"}
print(person)
print(len(person))
#method for empty dict
name=dict()
print(name)
print(type(name))
#without method
no_value={}
print(no_value)
#if we make dict with method so in key we cannot use double quotes
person1=dict(name="mahak",
             course="BCA",
             rollno=3)   
print(person1)
#convert any other data type into dict.
values=[("name","mahak"),("rollno",3),("language","python"),("value",True)]
value1=dict(values)
print(value1)
# mix=["mahak",3,True]
# mix1=dict(mix)
# print(mix1)
#for accessing
print(person["course"])
#discard replace with get in dict
print(person.get("email"))
person.get("email")
print(person)
#we also do provide a default value:
print(person.get("email","email not availabe"))
#adding new element
person["city"]="kanina"
person["citycode"]=123027
print(person)
#update method
person.update({
    "email":"mahak@gmail.com",
    "number":5768088674
})
print(person)
#pop method
print(person.pop("city"))
print(person)
#pop item
person.pop()
print(person)
#print(person.keys("name"))
#print(person.value("name"))
#print(person.item("name"))
#del,clear,nested dict