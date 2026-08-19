# Function to write attendance records to a file
def write_attendance(records):
    with open("attendance_register.txt", "w") as file:
        for student in records:
            file.write(
                f"Name: {student['name']}, "
                f"Reg No: {student['reg_no']}, "
                f"Status: {student['status']}\n"
            )


# Function to read and display attendance records
def read_attendance():
    with open("attendance_register.txt", "r") as file:
        print("\nAttendance Records")
        print("-------------------")
        print(file.read())


# Empty list to store student dictionaries
attendance_records = []

# Enter details for 3 students
for i in range(3):
    print(f"\nEnter details for Student {i + 1}")

    name = input("Enter student name: ")
    reg_no = input("Enter registration number: ")

    # Validate attendance status
    while True:
        status = input("Enter attendance status (Present/Absent): ")

        if status.lower() == "present":
            status = "Present"
            break
        elif status.lower() == "absent":
            status = "Absent"
            break
        else:
            print("Invalid status. Please enter Present or Absent.")

    # Store details in a dictionary
    student = {
        "name": name,
        "reg_no": reg_no,
        "status": status
    }


    attendance_records.append(student)

# Write records to the file
write_attendance(attendance_records)

# Read and display records
read_attendance()