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





