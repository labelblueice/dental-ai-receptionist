
appointments = []


print("==== Himal Dental Hospital ====")




#getting famalier with input()
name = input("Enter patient Name: ")
phone = input("Enter phone Number: ")
treatment = input("Treatment: ")
doctor = input("Doctor Name: ")
date = input("Appointment Date(YYYY-MM-DD): ")
age = input("Enter Age: ")
gender = input("Enter gender: ")


#dictionary

appointment = {
    "name": name,
    "phone": phone,
    "treatment": treatment,
    "doctor": doctor,
    "date": date,
    "age": age,
    "gender": gender
}


#creating a list

appointments.append(appointment)

#printing results

print("\nAppointment Booked Successfully\n")
print("\n")
print("==== Appointment ====")
print("\n")
print("Patient: " + appointments[0]["name"])
print("\n")
print("Phone: " + appointments[0]["phone"])
print("\n")
print("Treatment: " + appointments[0]["treatment"])
print("\n")
print("Doctor: " + appointments[0]["doctor"])
print("\n")
print("Date: " + appointments[0]["date"])
print("\n")
print("Age: " + appointments[0]["age"])
print("\n")
print("Gender: " + appointments[0]["gender"])
