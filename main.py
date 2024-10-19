import random

def is_valid_contact(contact):
    return contact.isdigit() and len(contact) == 10

def is_valid_email(email):
    return "@" in email and "." in email

def generate_random_alumni(alumni):
    first_names = ["John", "Jane", "David", "Emily", "Michael", "Sarah", "Chris", "Anna"]
    last_names = ["Doe", "Smith", "Brown", "Davis", "Johnson", "Taylor", "Lee", "Martin"]
    occupations = ["Software Engineer", "Data Scientist", "Product Manager", "Marketing Director", "Sales Executive"]
    streets = ["Elm St", "Oak St", "Pine St", "Maple St", "Birch St"]

    current_count = len(alumni)
    target_count = random.randint(5, 10)
    num_alumni_needed = target_count - current_count
    
    for _ in range(num_alumni_needed):
        adm = str(random.randint(10000, 99999))
        while adm in alumni:
            adm = str(random.randint(10000, 99999))
        
        name = f"{random.choice(first_names)} {random.choice(last_names)}"
        yoa = random.randint(2005, 2015)
        yog = yoa + 4
        contact = str(random.randint(6000000000, 9999999999))
        email = f"{name.split()[0].lower()}@example.com"
        occupation = random.choice(occupations)
        address = f"{random.randint(100, 999)} {random.choice(streets)}"

        alumni[adm] = {
            'Name': name,
            'Year of Admission': yoa,
            'Year of Graduation': yog,
            'Contact No.': contact,
            'E-mail Address': email,
            'Occupation': occupation,
            'Address': address
        }
    
    print(f"\nGenerated {num_alumni_needed} random alumni data successfully!\n")

def add_alumni_data(alumni):
    n = int(input("Number of students whose data you want to add: "))
    for _ in range(n):
        adm = input("Enter admission number (5 digits): ")
        while not (adm.isdigit() and len(adm) == 5):
            print("Admission number must be 5 digits.")
            adm = input("Enter a valid 5-digit admission number: ")
            
        name = input("Enter name of the alumni: ")
        yoa = int(input("Enter Year of Admission: "))
        yog = int(input("Enter Year of Graduation: "))
        contact = input("Enter Contact number: ")
        
        while not is_valid_contact(contact):
            print("Entered contact number is invalid")
            contact = input("Enter a valid contact number: ")
        
        email = input("Enter registered e-mail address: ")
        while not is_valid_email(email):
            print("This email address is not valid")
            email = input("Enter a valid e-mail address: ")
        
        occupation = input("Enter current occupation: ")
        address = input("Enter current address: ")

        alumni[adm] = {
            'Name': name,
            'Year of Admission': yoa,
            'Year of Graduation': yog,
            'Contact No.': contact,
            'E-mail Address': email,
            'Occupation': occupation,
            'Address': address
        }
    print("Alumni data added successfully!")

def check_alumni_details(alumni):
    x = int(input("Number of students whose data you want to check: "))
    for _ in range(x):
        adm = input("Enter Admission number: ")
        if adm in alumni:
            print(f"\nName: {alumni[adm]['Name']}")
            print(f"Year of Admission: {alumni[adm]['Year of Admission']}")
            print(f"Year of Graduation: {alumni[adm]['Year of Graduation']}")
            print(f"Contact No.: {alumni[adm]['Contact No.']}")
            print(f"E-mail Address: {alumni[adm]['E-mail Address']}")
            print(f"Occupation: {alumni[adm]['Occupation']}")
            print(f"Address: {alumni[adm]['Address']}\n")
        else:
            print("Entered admission number is not registered in 'Alumni Information System'")

def update_alumni_data(alumni):
    adm = input("Enter Admission number to update: ")
    if adm in alumni:
        print(f"Updating data for {alumni[adm]['Name']}:")
        
        new_contact = input("Enter new contact number (or press Enter to skip): ")
        if new_contact:
            while not is_valid_contact(new_contact):
                print("Invalid contact number. Please try again.")
                new_contact = input("Enter a valid contact number: ")
            alumni[adm]['Contact No.'] = new_contact
        
        new_email = input("Enter new email address (or press Enter to skip): ")
        if new_email:
            while not is_valid_email(new_email):
                print("Invalid email. Please try again.")
                new_email = input("Enter a valid email address: ")
            alumni[adm]['E-mail Address'] = new_email 

        new_occupation = input("Enter new occupation (or press Enter to skip): ")
        if new_occupation:
            alumni[adm]['Occupation'] = new_occupation
        
        new_address = input("Enter new address (or press Enter to skip): ")
        if new_address:
            alumni[adm]['Address'] = new_address
        
        print("Alumni data updated successfully!")
    else:
        print("This admission number is not found in the system.")

def delete_alumni_data(alumni):
    adm = input("Enter Admission number to delete: ")
    if adm in alumni:
        del alumni[adm]
        print(f"Alumni data for Admission number {adm} has been deleted.")
    else:
        print("This admission number is not found in the system.")

def list_all_alumni(alumni):
    if len(alumni) < 5:
        generate_random_alumni(alumni)

    print(f"\nTotal number of alumni: {len(alumni)}")

    print("\nList of all alumni:")
    for adm, details in alumni.items():
        print(f"\nAdmission Number: {adm}")
        print(f"Name: {details['Name']}")
        print(f"Year of Admission: {details['Year of Admission']}")
        print(f"Year of Graduation: {details['Year of Graduation']}")
        print(f"Contact No.: {details['Contact No.']}")
        print(f"E-mail Address: {details['E-mail Address']}")
        print(f"Occupation: {details['Occupation']}")
        print(f"Address: {details['Address']}")
    
def main():
    alumni = {
        "10345": {
            'Name': 'John Doe',
            'Year of Admission': 2010,
            'Year of Graduation': 2014,
            'Contact No.': '1234567890',
            'E-mail Address': 'john@example.com',
            'Occupation': 'Software Engineer',
            'Address': '123 Elm St'
        },
        "10489": {
            'Name': 'Jane Smith',
            'Year of Admission': 2009,
            'Year of Graduation': 2013,
            'Contact No.': '0987654321',
            'E-mail Address': 'jane@example.com',
            'Occupation': 'Data Scientist',
            'Address': '456 Oak St'
        },
        "10987": {
            'Name': 'David Brown',
            'Year of Admission': 2011,
            'Year of Graduation': 2015,
            'Contact No.': '5551234567',
            'E-mail Address': 'david@example.com',
            'Occupation': 'Product Manager',
            'Address': '789 Pine St'
        }
    }
    
    print("Welcome to the Alumni Information System")
    
    while True:
        print("\nOptions:")
        print("1. Add Alumni Data")
        print("2. Check Alumni Details")
        print("3. Update Alumni Data")
        print("4. Delete Alumni Data")
        print("5. List All Alumni")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == '1':
            add_alumni_data(alumni)
        elif choice == '2':
            check_alumni_details(alumni)
        elif choice == '3':
            update_alumni_data(alumni)
        elif choice == '4':
            delete_alumni_data(alumni)
        elif choice == '5':
            list_all_alumni(alumni)
        elif choice == '6':
            print("Thank you for using the Alumni Information System. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

if _name_ == "_main_":
    main()
