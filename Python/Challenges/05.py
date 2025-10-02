# Write a class Agenda that uses a HashMap to store
# contacts. Each contact must be represented by a Contact class,
# which has attributes for name, phone number, and email address.

# The Agenda class must contain the following methods:

# addContact(String name, String phone, String email): Adds a
# new contact to the agenda.

# removeContact(String name): Removes a contact from the agenda by name.

# searchContact(String name): Returns the contact information (phone
# and email) of a contact by name.

# listContacts(): Returns a list of all contacts in the agenda.

class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

class Agenda:
    def __init__(self):
        self.contacts = {}

    def addContact(self, name, phone, email):
        self.contacts[name] = Contact(name, phone, email)

    def removeContact(self, name):
        if name in self.contacts:
            del self.contacts[name]

    def searchContact(self, name):
        if name in self.contacts:
            c = self.contacts[name]
            print(f"Name: {c.name}, Phone: {c.phone}, Email: {c.email}")
        else:
            print("Contact not found.")

    def listContacts(self):
        for key in self.contacts:
            c = self.contacts[key]
            print(f"Name: {c.name}, Phone: {c.phone}, Email: {c.email}")

agenda = Agenda()

agenda.addContact("Alice", "123-456-7890", "Alice@example.com")
agenda.addContact("Bob", "987-654-3210", "bob@example.com")

agenda.searchContact("Bob")

agenda.removeContact("Alice")
agenda.listContacts()