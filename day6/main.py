from menu import show_menu
from appointment import book_appointment
from appointment import view_appointments

while True:

    show_menu()

    choice = input("Choose Option: ")
    if choice == "1":

        book_appointment()

    elif choice == "2":
        view_appointments()

    elif choice == "3":
        print("Thank You")
        break

    else:

        print("Invalid Option")
        