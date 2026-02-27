contacts = {}

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    if name in contacts: 
        print("The contact already exists.")
    else:
        contacts[name] = phone
        print("Contact added successfully.")

def delete_contact():
    name = input("Enter name: ")
    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully.")
    else:
        print("This contact does not exist.")

def update_contact():
    name = input("Enter name: ")
    for contact in contacts:
        if contact==name:
            phone = input("Enter the new phone number: ")
            contacts[name] = phone
            print("Contact updated successfully.")
            break
        else:
            print("This contact does not exist.")

def search_contact():
    name = input("Enter name: ")
    for contact in contacts:
        if contact.lower() == name.lower():
            print("Contact found")
            print(contact,contacts[contact])
            break
        else:
            print("Contact not found.")

def display_contacts():
    if contacts == {}:
        print("There are no contacts. ")
    else:
        print("Contact list:")
        for name, phone in contacts.items():
            print(name, phone)

while True:
    print("\nContact book menu:")
    print("1. Add contact")
    print("2. Delete contact")
    print("3. Update contact")
    print("4. Search contact")
    print("5. Display contact")
    print("6. Exit")

    choice = int(input("Enter your choice (1-6): "))

    if choice == 1:
        add_contact()

    elif choice == 2:
        delete_contact()

    elif choice == 3:
        update_contact()

    elif choice == 4:
        search_contact()

    elif choice == 5:
        display_contacts()

    elif choice == 6:
        print("Exiting contact book. Goodbye!")
        break

    else:
        print("Invalid choice. Plrase enter a number between these:")