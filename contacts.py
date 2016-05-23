contact = {}

choice = 0

while choice != 4:
	print(" ")
	print("Contacts")
	print(" ")
	print("Please select one of the following options.")
	print("Press (1) to add a Contact")
	print("Press (2) to search for a contact")
	print("Press (3) to see Contact library")
	print("Press (4) to leave contacts")
	print(" ") 
	
	choice = int(raw_input())
	
	if choice == 1:
		print(" ")
		print("New Contact Name:")
		print(" ")
		name = raw_input()	
		print(" ")
		print("New Contact Phone Number:")
		print(" ")
		number = raw_input()
		contact[name] = number
		print("New Contact Saved")

	elif choice == 2:
		print(" ")
		print("Search Contact")
		print(" ")
		print("Contact Name:")
		print(" ")
		name = raw_input()
		print(" ")
		print("Here's the number:")
		print(" ")
		print(contact[name])

	elif choice == 3:
		print(" ")
                print("Contact Library")
		print(" ")
                print(contact)
			
