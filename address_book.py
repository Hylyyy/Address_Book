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
            print("Entry number: ", edit, "First Name: ", first_name[index], "\nLast Name: ", last_name[index])
            print("Address: ", address[index], "\nPhone Number: ", phone_number[index])

    # The user will edit the adress if he/she inputed letter c.
        elif change_option == "c":
            index = entry_number.index(edit)
            new_address = input("\nPlease enter the new Address: ")
            address[index] = new_address
            print("\nEntry number: ", edit, "\nFirst Name: ", first_name[index], "\nLast Name: ", last_name[index])
            print("Address: ", address[index], "\nPhone Number: ", phone_number[index])
            