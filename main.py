import callhub

# --------------------------------------------------------------
# CONSTANTS
# --------------------------------------------------------------
CONTACT_FILE = "kontakte.txt"  # file to store contacts


# --------------------------------------------------------------
# MENU / INTERFACE FUNCTION
# --------------------------------------------------------------

def main_interface() -> str:
    """
    Displays the main menu and returns the users choice.
    """
    print("\n=== Contact Book ===")
    print("(1) Create contact")
    print("(2) Delete contacts")
    print("(3) Edit contacts")
    print("(4) Search contacts")
    print("(5) Call")
    print("(6) Exit contact book")
    return input("Enter a number between 1 - 6: ").strip()



# --------------------------------------------------------------
# Create contact FUNCTION
# --------------------------------------------------------------

def create_contact():
    return print("Funktion noch nicht Programmiert!")



# --------------------------------------------------------------
# Delete contact FUNCTION
# --------------------------------------------------------------

def delete_contacts():
    return print("Funktion noch nicht Programmiert!")


# --------------------------------------------------------------
# Edit contact FUNCTION
# --------------------------------------------------------------

def edit_contacts():
    return print("Funktion noch nicht Programmiert!")


# --------------------------------------------------------------
# Search contact FUNCTION
# --------------------------------------------------------------

def search_contacts():
    return print("Funktion noch nicht Programmiert!")


# --------------------------------------------------------------
# Calls FUNCTION
# --------------------------------------------------------------



# --------------------------------------------------------------
# MAIN PROGRAM LOOP
# --------------------------------------------------------------
def main() -> None:
    """
    Main program loop:
    keeps showing the menu until the user chooses to exit.
    """
    while True:
        choice = main_interface()

        if choice == "1":
            create_contact()
        elif choice == "2":
            delete_contacts()
        elif choice == "3":
            edit_contacts()
        elif choice == "4":
            search_contacts()
        elif choice == "5":
            callhub.call_interface()
        elif choice == "6":
            print("Exiting. Bye!")
            break
        else:
            print("Pick 1 - 6.")


# --------------------------------------------------------------
# ENTRY POINT
# --------------------------------------------------------------
if __name__ == "__main__":
    main()
