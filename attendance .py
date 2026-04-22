students = {}

def add_student():
    name = input("Enter student name: ")
    if name not in students:
        students[name] = []
        print("Student added successfully!")
    else:
        print("Student already exists!")

def mark_attendance():
    name = input("Enter student name: ")
    if name in students:
        days = int(input("Enter number of days: "))
        for i in range(days):
            status = input(f"Day {i+1} (P/A): ").upper()
            if status in ['P', 'A']:
                students[name].append(status)
            else:
                students[name].append('A')
    else:
        print("Student not found!")

def calculate_percentage(name):
    total = len(students[name])
    present = students[name].count('P')
    if total == 0:
        return 0
    return (present / total) * 100

def display_report():
    print("\nAttendance Report:")
    for name in students:
        percentage = calculate_percentage(name)
        print(name, ":", round(percentage, 2), "%")

while True:
    print("\n1.Add Student\n2.Mark Attendance\n3.Display Report\n4.Exit")
    choice = input("Enter choice: ")
    
    if choice == '1':
        add_student()
    elif choice == '2':
        mark_attendance()
    elif choice == '3':
        display_report()
    elif choice == '4':
        break
    else:
        print("Invalid choice")