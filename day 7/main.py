from patient import Patient
patients = []

patients.append(Patient("ram","984444","Cleaning","Dr. sharma","12"))
patients.append(Patient("sita","984444","Cleaning","Dr. sharma","32"))

# print(patient1.name)
# print(patient1.phone)
for patient in patients:
    patient.display()
    patient.complete()
    print("\n")

   
