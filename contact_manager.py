import json
import io

"""
Note: This is designed to hold a list of contacts as a list of dictionaries.
An alternative approach is to build a "Contact" class to represent a contact.
If you would like to do that as a Bonus exercise, that would be 5good way
to practice using OOP and composition!
"""


class ContactManager:
    """Class to do CRUD operations on the list of contacts"""

    def __init__(self, file="data.json"):
        self.file = file
        self.contacts = []

    def load_contacts(self):
        """Loads contacts from a JSON file and converts them to a list of
        dictionaries

        Bonus: What should happen if the file isn't there?
                What should happen if the file has invalid JSON in it?
        """
        try:
            with io.open(self.file, 'r') as file:
                self.contacts = json.load(file)
        except (FileNotFoundError):
            self.contacts = []
        except (json.JSONDecodeError):
            self.contacts = []

        return self.contacts

    def add_contact(self, contact):
        """Adds a contact to the list, and saves the file"""
        self.contacts.append(contact)
        with io.open(self.file, 'w') as file:
            json.dump(self.contacts, file)

    def update_contact(self, contact_to_update):
        """
        Updates a contact an saves the file

        Bonus: What happens when the id doesn't exist?
        """
        for index, contact in enumerate(self.contacts):
            if contact["id"] == contact_to_update["id"]:
                self.contacts[index] = contact_to_update

                with io.open(self.file, 'w') as file:
                    json.dump(self.contacts, file)
                return
        print(f'Contact with ID {contact_to_update} not found.')
        return

    def delete_contact(self, id_to_delete):
        """
        Deletes a contact and saves the file

        Bonus: What happens when the id doesn't exist?
        """
        for index, contact in enumerate(self.contacts):
            if contact['id'] == id_to_delete:
                del self.contacts[index]
                with io.open(self.file, 'w') as file:
                    json.dump(self.contacts, file)
                return
        else:
            print(f'Contact with ID {id_to_delete} not found.')