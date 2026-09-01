from contact_manager import ContactManager


def main():
    contact_manager = ContactManager()
    # We should call load_contacts before we show the menu
    # so they are loaded at the beginning of our program
    contact_manager.load_contacts()




    while True:
        menu_choice = display_menu()

        if menu_choice == "1":
            display_contacts(contact_manager)

        elif menu_choice == "2":
            add_new_contact(contact_manager)

        elif menu_choice == "3":
            update_contact(contact_manager)

        elif menu_choice == "4":
            delete_contact(contact_manager)

        elif menu_choice == "5":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please try again.")


def display_menu():
    print("\nOptions:")
    print("1. Display contacts")
    print("2. Add new contact")
    print("3. Update contact")
    print("4. Delete contact")
    print("5. Exit")
    choice = input("Enter your choice: ")
    return choice


def display_contacts(contact_manager: ContactManager):
    """
    display_contacts function just prints out the dictionaries directly.

    Bonus: Make it display something nicely. You might include a library
    like `rich` to print out the contacts in a nice table or something,
    or to print them in color
    """
    contacts = contact_manager.load_contacts()
    print("Contacts:")
    for contact in contacts:
        print(str(contact))


def add_new_contact(contact_manager: ContactManager):
    """
    Prompts the user for the fields for a new contact
    Then adds it to the contact manager

    Bonus: Check each input for valid values
    """
    id = input("Enter contact ID: ")
    name = input("Enter name: ")
    email = input("Enter email: ")
    phone = input("Enter phone: ")
    contact = {"id": id, "name": name, "email": email, "phone": phone}
    contact_manager.add_contact(contact)


def update_contact(contact_manager: ContactManager):
    """
    Prompts the user for the fields for a contact to update

    Bonus: Check each input for valid values
    """
    id = input("Enter the ID of the contact to update: ")
    name = input("Enter name: ")
    email = input("Enter email: ")
    phone = input("Enter phone: ")
    contact_to_update = {
        "id": id,
        "name": name,
        "email": email,
        "phone": phone,
    }
    contact_manager.update_contact(contact_to_update)


def delete_contact(contact_manager: ContactManager):
    """
    Deletes a contact by prompting the user for the id

    Bonus: Make the code work when the user inputs an invalid id
    """
    id = input("Enter the ID of the contact to delete: ")
    contact_manager.delete_contact(id)


if __name__ == "__main__":
    main()
