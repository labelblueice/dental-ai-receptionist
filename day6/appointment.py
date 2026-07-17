from data import appointments

def book_appointment():
    name = input("Patient Name: ")
    phone = input("Phone: ")
    treatment = input("Treatment: ")
    doctor = input("Doctor: ")

    patient = {
        "name": name,
        "phone": phone,
        "treatment": treatment,
        "doctor": doctor,
        "status": "Booked"
    }

    appointments.append(patient)
    print("Appointment Booked Successfully!")


def view_appointments():

    if(len(appointments) == 0):

        print("No Appointment Found.")
        return

    for patient in appointments:

        print("----------------------")
        print("Name :", patient["name"])
        print("Phone :", patient["phone"])
        print("Treatment :", patient["treatment"])
        print("Doctor :", patient["doctor"])
        print("Status :", patient["status"])


def search_appointment():

    phone = input("Phone No: ")
    found = False

    for patient in appointments:

        if patient["phone"] == phone:
            print("\nPatient Found!")
            print(patient)
        found = True
        break
    if not found:

        print("Appointment not Found")    



def delete_appointment():
    phone = input("Enter Phone Number: ")

    found = False

    for patient in appointments:
        if patient["phone"] == phone:
            confirm = input("Are you sure?(y/n)")
            if confirm == "y" or "Y":
                appointments.remove(patient)
                print("Appointment Deleted")

        found = True
        break
    if not found:
        print("Appointment Not Found")    

