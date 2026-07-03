appointments = []

# while True:

#     print("\n===== Himal Dental Hospital =====")
#     print("1. Book Appointment")
#     print("2. View Appointments")
#     print("3. Exit")

#     choice = input("Choose option: ")

#     if choice == "1":
#         print("Booking Appointment...")

#     elif choice == "2":
#         print("Viewing Appointments...")

#     elif choice == "3":
#         print("Thank you!")
#         break
    
#     else:
#         print("Invalid Option")


#working menu system for dental services

while True:

    print("\n===== Himal Dental Hospital =====")
    print("1. Book Appointment")
    print("2. View Appointments")
    print("3. Total Appointments")
    print("4. Exit")

    choice = input("Choose option: ")
    print("\n")
    if choice == "1":
        name = input("Patient Name: ")
        phone = input("Phone: ")
        treatment = input("Treatment: ")
        doctor = input("Doctor: ")

        appointment = {
            "name": name,
            "phone": phone,
            "treatment": treatment,
            "doctor": doctor
        }

        appointments.append(appointment)
        print("Appointment Booked Successfully!")

    elif choice == "2":
        if len(appointments) == 0:
            print("No Appointment Found.")

        else:
            for patient in appointments:
                print("=== Patient Information ===")
                print("----------------------------")

                print("Patient :",patient["name"])
                print("Phone :",patient["phone"])
                print("Treatment :",patient["treatment"])
                print("Doctor :",patient["doctor"])
    

    elif choice == "3":
        print("Total Appointments : " + str(len(appointments)))

    elif choice == "4":
        print("Thank you!")
        break
    
    else:
        print("Invalid Option")