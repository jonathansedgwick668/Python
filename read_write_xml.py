import xml.etree.ElementTree as ET

tree = ET.parse('customers.xml')
root = tree.getroot()

print("Customer Records:")
for customer in root.findall('customer'):
    print(f"ID: {customer.find('id').text}")
    print(f"First Name: {customer.find('first').text}")
    print(f"Last Name: {customer.find('last').text}")
    print(f"Address: {customer.find('address').text}")
    print(f"Phone: {customer.find('phone').text}")
    print(f"Email: {customer.find('email').text}")
    print()

add_record = input("Would you like to add a new customer? (yes/no): ").strip().lower()

if add_record == 'yes':
    customer_id = input("Enter customer ID: ")
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    address = input("Enter address: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")

    new_customer = ET.Element('customer')
    ET.SubElement(new_customer, 'id').text = customer_id
    ET.SubElement(new_customer, 'first').text = first_name
    ET.SubElement(new_customer, 'last').text = last_name
    ET.SubElement(new_customer, 'address').text = address
    ET.SubElement(new_customer, 'phone').text = phone
    ET.SubElement(new_customer, 'email').text = email

    root.append(new_customer)

    # Step 4: Write the updated XML back to the file
    tree.write('customers.xml')
    print("New customer added successfully!")