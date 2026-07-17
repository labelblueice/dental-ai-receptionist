from menu import show_menu
from appointment import book_appointment
from appointment import view_appointments
import appointment as appt

while True:

    show_menu()

    choice = input("Choose Option: ")
    if choice == "1":

        book_appointment()

    elif choice == "2":
        view_appointments()

    elif choice == "3":
        
        appt.search_appointment()
    

    elif choice == "4":

        appt.delete_appointment()

    elif choice == "5":

        print("Thank You!")
        break    
    else:

        print("Invalid Option")
        