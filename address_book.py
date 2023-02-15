# This code is used to create an Adress Book that can contain 100 entries.

# These are the input, processing and outputs statements.
print("************  PROGRAMMED BY  ************")
print("********* HYDEE LYN C. PALISOC *********\n")

# The user will be ask, what he or she wanted to do.


def print_menu():
    print(
     """
-----------------------------------
|    What would you like to do?   |
|---------------------------------|
|    1. Add Contact               |
|    2. Edit Contact              |
|    3. Delete Contact            |
|    4. View Contacts             |
|    5. Search Address Book       |
|    6. Exit                      |
-----------------------------------
    """)


print_menu()

# These are the Lists
first_name = []
last_name = []
address = []
phone_number = []
entry_number = []

# The user will add a contact if he/she inputed 1.
if option == 1:
    print("1. ADD CONTACT")
    first_name.append(input("Please enter your first name: "))
    last_name.append(input("Please enter your last name: "))
    address.append(input("Please enter your address: "))
    phone_number.append(input("Please enter your phone number: "))

    print_menu()

# The user will edit a contact if he/she inputed 2.
elif option == 2:
    print("2. EDIT CONTACT")
    edit = int(input("Please enter the entry number you want to edit: "))
    if edit in entry_number:
        ind = int(entry_number.index(edit))
        print("Previous Contact Information: ")
        print("Full Name: ", first_name[ind], last_name[ind])
        print("Address: ", address[ind])
        print("Phone Number: ", phone_number[ind])

        print("""
        what would you like to edit?:
        a. First name
        b. Last name
        c. Address
        d. Phone number
        """)

        change_option = input("Please choose an option: ")
    
    # The user will edit the first name if he/she inputed letter a.
        if change_option == "a":
            index = entry_number.index(edit)
            new_first = input("Please enter the new First name: ")
            first_name[index] = new_first
            print("Entry number: ", edit, "First Name: ", first_name[index], "Last Name: ", last_name[index])
            print("Address: ", address[index], "Phone Number: ", phone_number[index])
            
    # The user will edit the last name if he/she inputed letter b.
        elif change_option == "b":
            index = entry_number.index(edit)
            new_last = input("Please enter the new Last Name: ")
            last_name[index] = new_last
            print("Entry number: ", edit, "First Name: ", first_name[index], "Last Name: ", last_name[index])
            print("Address: ", address[index], "Phone Number: ", phone_number[index])

    # The user will edit the adress if he/she inputed letter c.
        elif change_option == "c":
            index = entry_number.index(edit)
            new_address = input("Please enter the new Address: ")
            address[index] = new_address
            print("nEntry number: ", edit, "First Name: ", first_name[index], "Last Name: ", last_name[index])
            print("Address: ", address[index], "Phone Number: ", phone_number[index])

    # The user will edit the phone number if he/she inputed letter d.
        elif change_option == "d":
            index = entry_number.index(edit)
            new_number = input("Please enter the new Phone Number: ")
            phone_number[index] = new_number
            print("Entry number: ", edit, "First Name: ", first_name[index], "Last Name: ", last_name[index])
            print("Address: ", address[index], "Phone Number: ", phone_number[index])

        else:
            print("The entry does not exist.")

    else:
        print("The entry does not exist")
    print_menu()

# The user will delete a contact if he/she inputed number 3.
elif option == 3:
    print("3. DELETE CONTACT")
    entry_num = int(input("Enter the entry number you want to REMOVE: "))
    if entry_num in entry_number:
        index = entry_number.index(entry_num)
        print("The Entry number", entry_num)
        print("First name:", first_name.pop(index))
        print("Last name:", last_name.pop(index))
        print("Address:", address.pop(index))
        print("Phone number:", phone_number.pop(index), "is REMOVED")
    
    else:
        print("The entry does not exist.")
    print_menu()

# The program will show the contacts if he/she inputed number 4.
elif option == 4:
    print("VIEW CONTACTS")
    for i in range(len(entry_number)):
        print("  Entry number: ", entry_number[i])
        print("  First Name: ", first_name[i])
        print("  Last Name: ", last_name[i])
        print("  Address: ", address[i])
        print("  Phone Number: ", phone_number[i])
    print_menu()

# The user can search a specific contact if he/she inputed number 5.
elif option == 5:
    print("""
    (a) Search by FIRST NAME
    (b) Search by LAST NAME
    (c) Search by ADDRESS
    (d) Search by CONTACT NUMBER
    """)

# Searching using the first name if the user inputed letter a.
change_choice = input("Enter choice: ")
if change_choice == "a":
    search = input("Enter first name: ")
    print("Result/s:")
    for i in range(len(first_name)):
        if search in first_name[i]:
            print("Entry number", entry_number[i])
            print("First name:", first_name[i], "| Last name:", last_name[i])
            print("Address:", address[i], "Phone number:", phone_number[i])
    if search not in first_name:
        print("The entry does not exist.")

# Searching using the last name if the user inputed letter b.
elif change_choice == "b":
    search = input("Enter Last name: ")
    print("Result/s:")
    for i in range(len(last_name)):
        if search in last_name[i]:
            print("nEntry number", entry_number[i])
            print("First name:", first_name[i], "| Last name:", last_name[i])
            print("Address:", address[i], "Phone number:", phone_number[i])
    if search not in last_name:
        print("The entry does not exist.")

# Searching using the address if the user inputed letter c.
elif change_choice == "c":
    search = input("Enter Address: ")
    print("Result/s:")
    for i in range(len(address)):
        if search in address[i]:
            print("Entry number", entry_number[i])
            print("First name:", first_name[i], "| Last name:", last_name[i])
            print("Address:", address[i], "Phone number:", phone_number[i])
    if search not in address:
        print("The entry does not exist.")

# Searching using the phone number if the user inputed letter d.
elif change_choice == "d":
    search = input("Enter Phone number: ")
    print("Result/s:")
    for i in range(len(phone_number)):
        if search in phone_number[i]:
            print("Entry number", entry_number[i])
            print("First name:", first_name[i], "| Last name:", last_name[i])
            print("Address:", address[i], "Phone number:", phone_number[i])
    if search not in phone_number:
        print("The entry does not exist.")

# If the user chooses option 6, the program will exit.
elif option == 6:
    print("""
    Thank you for using the program!!!
    """)
    exit()
    break