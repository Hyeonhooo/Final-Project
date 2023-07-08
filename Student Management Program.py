class Student:
    def __init__(self, id):
        self.id = id

arr = []

while True:
    print("1. Add Student ID")
    print("2. Delete Student ID")
    print("3. Insert Student ID at a given position or index")
    print("4. Search Student ID")
    print("5. Update Student ID")
    print("6. Display Student IDs")
    print("7. Exit")
    choice = int(input("Enter your choice: "))


    if choice == 1:  # Add a Student ID
        id = int(input("Enter Student ID: "))
        arr.append(Student(id))

    elif choice == 2:  # Delete Student ID
        id = int(input("Enter Student ID to delete: "))
        found = False
        for j in range(len(arr)):
            if arr[j].id == id:
                del arr[j]
                found = True
                break
        if found:
            print("Student ID deleted")
        else:
            print("Student ID not found")

    elif choice == 3:  # Insert Student ID at a given position or index
        id = int(input("Enter Student ID: "))
        position = int(input("Enter position: "))
        if position >= 0 and position <= len(arr):
            arr.insert(position, Student(id))
        else:
            print("Invalid position")
            

    elif choice == 4:  # Search Student ID
        id = int(input("Enter Student ID to search: "))
        found = False
        for j in range(len(arr)):
            if arr[j].id == id:
                print(f"Student ID found at position {j}")
                found = True
                break
        if not found:
            print("Student ID not found")

    elif choice == 5:  # Update Student ID
        id = int(input("Enter existing Student ID to update: "))
        new_id = int(input("Enter new Student ID: "))
        found = False
        for j in range(len(arr)):
            if arr[j].id == id:
                arr[j].id = new_id
                print("Student ID updated")
                found = True
                break
        if not found:
            print("Student ID not found")


    elif choice == 6:  # Display Student IDs
        print("Student IDs:")
        for student in arr:
            print(student.id)

    elif choice == 7:  # Exit
        print("The programming is over.")
        break

    else:
        print("Invalid option. Please choose a valid option.")