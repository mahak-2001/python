age=18
if age>=18:
    print("you are adult.")
else:
    print("you are not adult.")

marks=77
if(marks>=60):
    if (marks>=80):
     print("good grades")
    else:
       print("okay grades")
else:
     print("grade is very low")

#operator(comparison operator)
# and operators:
age=17
has_ticket=False
if age>=18 and has_ticket:
 print("entry allowed.")
else:
    print("entry denied.")

#or operator.
age=18
has_ticket=False
if age>=18 or has_ticket:
 print("entry allowed.")
else:
    print("entry denied.")
#or operator
day="saturday"
if day=="saturday" or day=="sunday":
   print("it is weekend!")
else:
      print("it is weekday!")

#not comperison operator
is_raining=False
if not is_raining:
   print("let's go outside.")


age=15
has_license=True
has_car=False
if age>=18 and (has_license or has_car):
   print("you can drive somewhere")
else:
   print("you need a licence or a car first.")

#input 
username="admin"
password="1234"
entered_username=input("username:")
entered_password=input("password:")
if entered_username==username and entered_password==password:
   print("login successful")
else:
   print("incorrect username or password")

score=int(input("enter your score:"))
attended_class=True
if score>=60:
   if attended_class:
    print("you passed with attendence credit.")
   else:
     print("you passed, but attendence is missing.")
else:
   print("you did not passed")
   