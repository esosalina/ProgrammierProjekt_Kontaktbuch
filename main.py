
import re
from datetime import datetime

# --------------------------------------------------------------
# CONSTANTS
# --------------------------------------------------------------
CONTACT_FILE = "kontakte.txt"  # file to store contacts
CALLS_FILE = "calls.txt"  # file to store call logs
PHONE_REGEX = r"0041 \d{2} \d{2} \d{2}"  # Swiss phone format (0041 00 00 00)


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
# MENU / INTERFACE FUNCTION
# --------------------------------------------------------------
def call_interface() -> str:
    """
    Displays the main call menu and returns the users choice.
    """
    print("\n=== Call Interface ===")
    print("(1) Enter phonenumber")
    print("(2) Search contacts")
    print("(3) Display last calls")
    print("(4) Exit call interface")
    return input("Enter a number between 1 - 4: ").strip()


# --------------------------------------------------------------
# OUTGOING CALL FUNCTION
# --------------------------------------------------------------
def outgoing_call() -> None:
    """
    Asks user for a phone number, validates format,
    and logs the call if the format is correct.
    """
    number = input("Enter phonenumber (0041 00 00 00): ").strip()
    
    # Validate the number format using regex
    if not re.fullmatch(PHONE_REGEX, number):
        print("Invalid format. Use: 0041 00 00 00")
        return
    
    print(f"Calling {number} ...")
    _log_call(f"OUT {number}")  # Log the outgoing call


# --------------------------------------------------------------
# CONTACT SEARCH FUNCTION
# --------------------------------------------------------------
def search_contacts() -> None:
    """
    Lets the user search by name or user ID.
    This is currently a demo placeholder (no real contact DB).
    """
    query = input("Search (Enter Name or UserID): ").strip()
    
    if not query:
        print("Empty search. Try again.")
        return
    
    print(f"Searching for '{query}' ... (demo)")
    _log_call(f"SEARCH '{query}'")  # Log that a search was performed


# --------------------------------------------------------------
# LAST CALLS FUNCTION
# --------------------------------------------------------------
def last_calls() -> None:
    """
    Displays the content of the calls.txt file, which holds
    all previous logged calls or searches.
    """
    try:
        with open(CALLS_FILE, "r", encoding="utf-8") as f:
            data = f.read().strip()
            print("\n=== Last Calls ===")
            print(data if data else "(no calls yet)")
    except FileNotFoundError:
        print("\n=== Last Calls ===")
        print("(no calls yet)")


# --------------------------------------------------------------
# INTERNAL LOG FUNCTION (PRIVATE)
# --------------------------------------------------------------
def _log_call(entry: str) -> None:
    """
    Appends a new log entry with timestamp to calls.txt.
    Used internally by outgoing_call() and search_contacts().
    """
    ts = datetime.now().isoformat(timespec="seconds")
    with open(CALLS_FILE, "a", encoding="utf-8") as f:
        f.write(f"{ts} {entry}\n")


# --------------------------------------------------------------
# MAIN PROGRAM LOOP
# --------------------------------------------------------------
def main_call() -> None:
    """
    Main program loop:
    keeps showing the menu until the user chooses to exit.
    """
    while True:
        choice = call_interface()

        if choice == "1":
            outgoing_call()
        elif choice == "2":
            search_contacts()
        elif choice == "3":
            last_calls()
        elif choice == "4":
            print("Exiting. Bye!")
            break
        else:
            print("Pick 1 - 4.")


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
            main_call()
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
