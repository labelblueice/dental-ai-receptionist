# Dental AI

# clinic_name = "Himal Dental Hospital"

# doctor_name = "Dr. Sharma"

# patient_name = "Ram Sharma"

# age = 25

# phone = "9840234565"

# print(clinic_name)
# print(doctor_name)
# print(patient_name)
# print(age)
# print(phone)


#creating a test dictionary to store patient data
# patient = {
#     "name": "Baldev Bhatt",
#     "age": 41,
#     "phone": "9801547864",
#     "treatment": "Cleaning"
# }

# print(patient)

#creating a appointment booking function 

# def book_appointment(name,phone,treatment):
#     print("Appointment Booked")

#     print(name)

#     print(phone)
    
#     print(treatment)

# book_appointment("Bhuwan Bhatta","9846753465","cleaning")    

#appointments = []

# def book(name, phone, treatment, doctor,appointment_date):
#     patient = {
#         "name": name,
#         "phone": phone,
#         "treatment": treatment,
#         "doctor": doctor,
#         "appointment_date": appointment_date
#     }
#     appointments.append(patient)

# book("Ram","1234","Reading","Hari","2026-02-12")
# book("Shyam","12344","Studying","Baldev","2025-02-12")
# print(appointments)


appointments = []
def appointed_doctor(name,doctor_name,date):
    patient = {
        "name": name,
        "doctor": doctor_name,
        "date": date
    }
    appointments.append(patient)

appointed_doctor("Bhuwan","Dr. Baldev","2026-01-09")
print(appointments)    