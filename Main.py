# ------------------------------------------------------------------------ #
# Title: Assignment 09
# Description: Working with Modules

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 9
# DAlbano,3.15.22,Modified code to complete assignment 9
# ------------------------------------------------------------------------ #
# TODO: Import Modules
if __name__ == "__main__":
    from DataClasses import Employee as Emp
    from ProcessingClasses import FileProcessor as Fp
    from IOClasses import EmployeeIO as Eio
else:
    raise Exception("This file was not created to be imported")

# Main Body of Script  ---------------------------------------------------- #
# TODO: Add Data Code to the Main body
# Load data from file into a list of employee objects when script starts
# Show user a menu of options
# Get user's menu option choice
    # Show user current data in the list of employee objects
    # Let user add data to the list of employee objects
    # let user save current data to file
    # Let user exit program

# Main Body of Script  ---------------------------------------------------- #

lstTable = []

try:
    lstFileData = Fp.read_data_from_file("EmployeeData.txt")
    lstTable.clear()
    for line in lstFileData:
        lstTable.append(Emp(line[0], line[1], line[2].strip()))

    while True:
        # Show user a menu of options
        Eio.print_menu_items()
        # Get user's menu option choice
        strChoice = Eio.input_menu_options()

        if strChoice.strip() == '1':
            # Show user current data in the list of employee rows
            Eio.print_current_list_items(lstTable)
            continue

        elif strChoice.strip() == '2':
            # Let user add data to the list of employees
            lstTable.append(Eio.input_employee_data())
            continue

        elif strChoice.strip() == '3':
            # Let user save current data to file
            Fp.save_data_to_file("EmployeeData.txt", lstTable)
            continue

        elif strChoice.strip() == '4':
            print("Goodbye")
            break

except Exception as e:
    print("There was an error!")
    print(e, e.__doc__, type(e), sep='\n')