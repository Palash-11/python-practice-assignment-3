def add_employee(name, emp_id, salary):
    with open("employees.txt", "a") as file:
        file.write(f"{name} | {emp_id} | {salary}\n")
    print("Employee information saved successfully!\n")


def display_employees():
    print("\n--- All Employee Records ---")
    try:
        with open("employees.txt", "r") as file:
            records = file.readlines()
            if not records:
                print("No employee records found.")
            else:
                for record in records:
                    print(record.strip())
    except FileNotFoundError:
        print("No employee file found yet.")
    print("-" * 28 + "\n")


def main():
    while True:
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Exit")
        
        choice = input("Enter your choice (1-3): ")
        
        if choice == '1':
            name = input("Enter Employee Name: ")
            emp_id = input("Enter Employee ID: ")
            salary = input("Enter Salary: ")
            add_employee(name, emp_id, salary)
            
        elif choice == '2':
            display_employees()
            
        elif choice == '3':
            print("Exiting program. Thank you!")
            break
        else:
            print("Invalid choice! Please enter 1, 2, or 3.\n")

if __name__ == "__main__":
    main()