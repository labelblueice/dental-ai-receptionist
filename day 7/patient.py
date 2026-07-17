class Patient:

    def __init__(self,name,phone,treatment,doctor,age):

        self.name = name
        self.phone = phone
        self.treatment = treatment
        self.doctor = doctor
        self.status = "Booked"
        self.age = age

    def display(self):

        print("Name :", self.name)
        print("Phone :", self.phone)
        print("Treatment :", self.treatment)
        print("Doctor :", self.doctor)
        print("Status :", self.status)

    def complete(self):
        self.status = "Completed"  
        print(self.status)  
        