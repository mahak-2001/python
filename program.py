# Student Result Management Program

students = []

# Number of students
n = int(input("Enter the number of students: "))

for i in range(n):
    print(f"\nEnter details of Student {i + 1}")

    name = input("Enter Name: ")
    roll_no = input("Enter Roll No: ")

    marks = []

    # Taking 5 subject marks
    for j in range(5):
        while True:
            mark = int(input(f"Enter marks of Subject {j + 1} (0-100): "))

            if 0 <= mark <= 100:
                marks.append(mark)
                break
            else:
                print("Invalid marks! Please enter marks between 0 and 100.")

    total = sum(marks)
    average = total / 5

    # Finding Grade
    if average >= 90:
        grade = "A+"
    elif average >= 80:
        grade = "A"
    elif average >= 70:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 40:
        grade = "D"
    else:
        grade = "Fail"

    # Store data in a list
    student = [name, roll_no, marks, total, average, grade]
    students.append(student)

# Display Result
print("\n========== STUDENT REPORT ==========")

for student in students:
    print("\n-----------------------------------")
    print("Name      :", student[0])
    print("Roll No   :", student[1])
    print("Marks     :", student[2])
    print("Total     :", student[3])
    print("Average   :", round(student[4], 2))
    print("Grade     :", student[5])



#count frequency of each word in a sentence
sentence = input("Enter a sentence: ")
words = sentence.lower().split()
frequency = {}
for word in words:
    frequency[word] = frequency.get(word, 0) + 1
print("\nWord Frequency:")
for word, count in frequency.items():
    print(f"{word} : {count}")