name = input("Enter name: ")          # string
m1 = float(input("Enter mark 1: "))   # float
m2 = float(input("Enter mark 2: "))
m3 = float(input("Enter mark 3: "))
m4 = float(input("Enter mark 4: "))

classes = int(input("Classes attended: "))   # integer

# calculations
average = (m1 + m2 + m3 + m4) / 4
attendance = (classes / 60) * 100

# boolean condition
passed = (average >= 40) and (attendance >= 80)

# output using f-string
print(f"Name: {name}")
print(f"Average: {average}")
print(f"Attendance: {attendance}%")

# if-else
if passed:
    print("Result: Pass")
else:
    print("Result: Fail")
