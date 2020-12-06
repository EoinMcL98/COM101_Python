# This program will be an employee management tool


def header():
    print('Welcome, This is an employee management tool.')
    print('Program created by Eoin McLaughlin - B00650670')
    print('----------------------------------------------')


# Read in list
def emp_list():
    employees = []

    emps_list = open("Emp_Dataset.txt", "r")

    # For each string line in emps_list
    # Begin For loop
    for line in emps_list:
        if line[0] != "#":
            employees.append(line.rstrip("\n"))

    emps_list.close()
    return employees


# This menu will display the options you have
def MainMenu():
    print("\n 1. Print out a summary statement, which details the "
          "number of records successfully read into your program \n",
          "2. Print out a list of employees and their respective details \n",
          "3. Print a report detailing the total salary bill \n",
          "4. Print a report detailing the average salary bill"
          "based on the number of employees \n",
          "5. Add a new employee to the current list \n",
          "6. Print a report detailing the number of employees\n",
          "grouped by each position type \n",
          "7. Query the list by providing a salary threshold above\n",
          "which employees are returned \n",
          "8. Quit the program \n",
          "9. Help \n")


# This menu will print out a summary statement of records
# which have been successfully read into the program
def no_of_records(employees):
    for emp in employees:
        print(emp)
    MainMenu()
    if_statement_menu()


# Print out a list of employees and their details
def print_list(employees):
    print("EMP_NO : EMP_NAME : AGE : POSITION : SALARY : YRS_EMP")
    for emp in employees:
        print(emp)
    MainMenu()
    if_statement_menu()


# Print a report detailing the total salary bill
def total_salary_bill(employees):
    total_salary = 0
    for emp in employees:
        split_emp = emp.split(", ")

        total_salary += int(split_emp[4])

    print("The total salary is: £", format(total_salary, ".2f"), sep="")
    MainMenu()
    if_statement_menu()


# This function will print report detailing the average
# salary bill based on no. of employees
def average_salary_bill(employees):
    num_emp = len(employees)

    total_salary = 0
    for emp in employees:
        split_emp = emp.split(", ")

        total_salary += int(split_emp[4])

    avg_salary = total_salary / num_emp
    print("The Average salary is: £", format(avg_salary, ".2f"), sep="")
    MainMenu()
    if_statement_menu()


# This function will allow user to add new employee
# to the current list
def add_employee(employees):
    emp_data = employees
    add_emp_q = str(input("Would you like to add an employee (Y/N): "))
    if add_emp_q == 'y':
        add_emp = str(input("Enter new employee data: "))
        emp_data.append(add_emp)
    elif add_emp_q == 'Y':
        add_emp = str(input("Enter new employee data: "))
        emp_data.append(add_emp)
    elif add_emp_q == 'n':
        print("You will be returned to the Main Menu")
        MainMenu()
        if_statement_menu()
    elif add_emp_q == 'N':
        print("You will be returned to the Main Menu")
        MainMenu()
        if_statement_menu()


# This function will print a report detailing no. of
# employees grouped by each position type
def group_employees(employees):
    emps_columns = []

    for employee in employees:
        split_emp = employee.split(", ")
        emps_columns.append(split_emp)
        emps_columns.sort(key=lambda x: x[3])

    print("\n List of Employees - Grouped By Position")
    print("\n EMP_NO : EMP_NAME : AGE : POSITION : SALARY : YRS_EMP")

    for emp_group in emps_columns:
        string_emp = emp_group[0] + ", " + emp_group[1] + ", " + emp_group[2] + ", " + emp_group[3] + ", " + \
                     emp_group[4] + ", " + emp_group[5]

        print(string_emp)
    MainMenu()
    if_statement_menu()


# This function will query the list by providing a salary
# threshold  above which employees are returned
def salary_threshold(employees):
    print("The employees earning a salary above £35,000 will be listed.")
    salary = 35000
    for emp in employees:
        split_emp = emp.split(", ")
        if float(split_emp[4]) > salary:
            print(emp)
        elif float(split_emp[4]) < salary:
            print("You will be returned to the main menu")
    MainMenu()
    if_statement_menu()


# This function will quit the code when user selects
# option 8 on the menu
def quit_program():
    Quit_Program = str(input("Are you sure you want to quit the program (Y/N: "))
    if Quit_Program == 'y':
        quit()
    elif Quit_Program == 'Y':
        quit()
    elif Quit_Program == 'n':
        quit()
        MainMenu()
        if_statement_menu()
    elif Quit_Program == 'N':
        quit()
        MainMenu()
        if_statement_menu()


# This function will present the user with a question that
# will allow them to search for a specific employee
def search_employee(employees):
    Search_Emp = str(input("What is the number of the employee you're looking for: "))
    for line in employees:
        if Search_Emp in line:
            print(line)
    MainMenu()
    if_statement_menu()


# if Statement for main menu allowing the user
# to select what submenu they wish to access
def if_statement_menu():
    employees = emp_list()
    main_menu = str(input("What submenu would you like to select: "))
    if main_menu == '1':
        no_of_records(employees)
    elif main_menu == '2':
        print_list(employees)
    elif main_menu == '3':
        total_salary_bill(employees)
    elif main_menu == '4':
        average_salary_bill(employees)
    elif main_menu == '5':
        add_employee(employees)
    elif main_menu == '6':
        group_employees(employees)
    elif main_menu == '7':
        salary_threshold(employees)
    elif main_menu == '8':
        quit_program()
    elif main_menu == '9':
        search_employee(employees)


# Calling the header main menu function
header()
MainMenu()
if_statement_menu()
