#loops:excute a block of code repeatedly until a condition become false.
#for loop
for i in range(0,20,3):
    print(i)

names=["mahak","jiya","teena","jaanvi"]
for name in names:
    print(name)
#range
for x in range(5):
    print(x)

words="mahak"
for x in words:
    print(x)

#while loop
count = 0
while count<5:
    print(count)
    count +=1


password=""
while password.strip() !="secret":
    password=input("enter your password: ")
    
print("access granted")
    
sum of 1,20 no. using for loop.
sum = 0
for i in range(1,21):
    sum=sum+i
    print(sum)

#break and continue.
for i in range(1,6):
    if i==3:
        break
    print(i)

total=0
number=int(input("enter a number: "))

while number!=0:
    total+=number
    number=int(input("enter another number: "))
print("total",total)

secret_number=7
guess=0
while guess !=secret_number:
    guess=int(input("guess the number:"))
print("correct number!")

number=[1,2,3,4,5]
for i in number:
    if i %2 == 0:
        continue
    print(i)