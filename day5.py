appointments = []
while True:
    print("1. Book Appointment")
    print("2. View Appointment")
    print("3. Search Appointment")
    print("4. Update Appointment")
    print("5. Delete Appointment")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1" :
        name = input("Enter Your Name: ")
        age = int(input("Enter Your Age: "))
        phone = input("Enter Phone No: ")
        doctor = input("Enter doctor's name: ")
        treatment = input("Enter treatment name: ")

        appointment = {
            "name": name,
            "age": age,
            "phone": phone,
            "doctor": doctor,
            "treatment": treatment
        }

        appointments.append(appointment)
        print("\nAppointment Booked Successfully!")

    elif choice == "2":
        if len(appointments) == 0 :
            print("No Appointment Found")

        else:
            for patient in appointments:
                print("==== Appointments =====")
                print("-------------------------")
                print("=== Patient Information ===")
                print("Name: ",patient["name"])
                print("Age: ",patient["age"])
                print("Phone: ",patient["phone"])
                print("Doctor: ",patient["doctor"])
                print("Treatment: ",patient["treatment"])
    
    elif choice == "3":
        phone = input("Enter Phone Number:")

        found = False

        for patient in appointments:

            if patient["phone"] == phone:
                print("\nAppointment Found")
                print(patient)

                found True
                break
        if not found:
            print("Appintment Not Found")    

    elif choice == "4":
        phone = input("Enter Phone Number")

        found = False
        for patient in appointments:

            if patient["phone"] == phone:
                new_treatment = input("New Treatment: ")
                patient["treatment"] = new_treatment
                print("Appointment Updated")
                found = True
                break
        if not found:

            print("Appointment Not Found")    

 
    elif choice == "5":
        phone = input("Enter Phone Number: ")

        found = False

        for patient in appointments:
            if patient["phone"] == phone:
                appointments.remove(patient)
                print("Appointment Deleted")

                found = True
                break
        if not found:
            print("Appointment Not Found")    
    
    elif choice == "6":
        print("Thank You!")
        break
    else:
        print("Invalid Choice")     