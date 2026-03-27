name = input("Enter name: ")

m1 = float(input("Enter mark 1: "))
m2 = float(input("Enter mark 2: "))
m3 = float(input("Enter mark 3: "))
m4 = float(input("Enter mark 4: "))

classes = int(input("Classes attended: "))

# calculations
average = (m1 + m2 + m3 + m4) / 4
attendance = (classes / 70) * 100

# pass condition (boolean)
passed = (average >= 40) and (attendance >= 80)

# grade using if-else
if average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 50:
    grade = "D"
elif average >= 40:
    grade = "E"
else:
    grade = "F"

# output
print(f"Name: {name}")
print(f"Average: {average}")
print(f"Attendance: {attendance}%")
print(f"Grade: {grade}")

# result
if passed:
    print("Result: Pass")
else:
    print("Result: Fail")
