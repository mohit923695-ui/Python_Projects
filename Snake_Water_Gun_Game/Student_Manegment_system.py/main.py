students = []

def add_student():
    name = input("Enter student name: ")
    age = int(input("Enter age: "))
    course = input("Enter course: ")

    student = {
        "name": name,
        "age": age,
        "course": course
    }

    students.append(student)
    print("✅ Student added successfully!\n")


def view_students():
    if not students:
        print("❌ No students found.\n")
        return

    print("\n--- Student List ---")
    for i, student in enumerate(students, start=1):
        print(f"{i}. Name: {student['name']}")
        print(f"   Age: {student['age']}")
        print(f"   Course: {student['course']}")
        print()


def search_student():
    name = input("Enter student name to search: ")

    for student in students:
        if student["name"].lower() == name.lower():
            print("\n✅ Student Found!")
            print(f"Name: {student['name']}")
            print(f"Age: {student['age']}")
            print(f"Course: {student['course']}\n")
            return

    print("❌ Student not found.\n")


def delete_student():
    name = input("Enter student name to delete: ")

    for student in students:
        if student["name"].lower() == name.lower():
            students.remove(student)
            print("✅ Student deleted successfully!\n")
            return

    print("❌ Student not found.\n")


while True:
    print("===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        delete_student()

    elif choice == "5":
        print("Thank you! 👋")
        break

    else:
        print("❌ Invalid choice. Please try again.\n")