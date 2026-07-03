appointments = []

while True:

    print("\n===== Himal Dental Hospital =====")
    print("1. Book Appointment")
    print("2. View Appointments")
    print("3. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        print("Booking Appointment...")

    elif choice == "2":
        print("Viewing Appointments...")

    elif choice == "3":
        print("Thank you!")
        break
    
    else:
        print("Invalid Option")