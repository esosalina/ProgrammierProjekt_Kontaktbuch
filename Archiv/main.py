
import re
from datetime import datetime

# --------------------------------------------------------------
# CONSTANTS
# --------------------------------------------------------------
CONTACT_FILE = "kontakte.txt"  # file to store contacts
CALLS_FILE = "calls.txt"  # file to store call logs
PHONE_REGEX = r"0041 \d{2} \d{2} \d{2}"  # Swiss phone format (0041 00 00 00)
CONTACT_SEPERATOR = "=======" #trennt die Kontakte von einander in kontakte.txt (übersichtlicher)
CONTACT_ID_MIN = 2800
CONTACT_ID_MAX = 3200


# --------------------------------------------------------------
# HELPER FUNCTIONS (INPUT VALIDATION)
# --------------------------------------------------------------

def input_phone(prompt="Phonenumber (numbers only): "):
   
    while True:
        number = input(prompt).strip()  # Leerzeichen entfernen
        if number.isdigit():            # Prüfen ob nur Zahlen
            return number               # Gültige Eingabe zurückgeben
        print("Error: Phonenumber must be numbers only.")

def input_email_letters_only(prompt="E-Mail (letter only, @ and .): "):
    
    while True:
        email = input(prompt).strip()  # Leerzeichen entfernen
        if all(c.isalpha() or c in "@." for c in email):  # Prüfen jedes Zeichen
            return email               # Gültige Eingabe zurückgeben
        print(" Fehler: E-Mail darf nur Buchstaben, @ und . enthalten.")

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
# Unique Contact-ID FUNCTION
# --------------------------------------------------------------
def unique_id(contact_id: str) -> bool:
    """
    Tests, if the new Contact ID already exists in kontakte.txt
    """
    try: 
        with open(CONTACT_FILE, "r", encoding="utf-8") as datei:
            while True:
                cid = datei.readline()
                if not cid: 
                    break
                cid = cid.strip()
                firstname = datei.readline().strip()
                lastname = datei.readline().strip()
                phonenumber = datei.readline().strip()
                email= datei.readline().strip()
                sep = datei.readline()

                if cid == contact_id:
                    return True
    except FileNotFoundError:
        return False

    return False


def load_contacts() -> list:
    """
    Reads all contacts from CONTACT_FILE and returns them as dicts.
    """
    contacts = []
    try:
        with open(CONTACT_FILE, "r", encoding="utf-8") as datei:
            while True:
                cid = datei.readline()
                if not cid:
                    break
                cid = cid.strip()
                firstname = datei.readline().strip()
                lastname = datei.readline().strip()
                phonenumber = datei.readline().strip()
                email = datei.readline().strip()
                sep = datei.readline()
                if cid:
                    contacts.append({
                        "id": cid,
                        "firstname": firstname,
                        "lastname": lastname,
                        "phonenumber": phonenumber,
                        "email": email,
                    })
    except FileNotFoundError:
        pass
    return contacts


def save_contacts(contacts: list) -> None:
    """
    Persists the given contact list sorted by numeric Contact-ID.
    """
    def sort_key(contact: dict):
        try:
            return int(contact["id"])
        except ValueError:
            return contact["id"]

    contacts_sorted = sorted(contacts, key=sort_key)
    with open(CONTACT_FILE, "w", encoding="utf-8") as datei:
        for contact in contacts_sorted:
            datei.write(f"{contact['id']}\n")
            datei.write(f"{contact['firstname']}\n")
            datei.write(f"{contact['lastname']}\n")
            datei.write(f"{contact['phonenumber']}\n")
            datei.write(f"{contact['email']}\n")
            datei.write(CONTACT_SEPERATOR + "\n")
# --------------------------------------------------------------
# Create contact FUNCTION
# --------------------------------------------------------------
def create_contact():
    """
    Creates a new contact ensuring ID is unique and within the allowed range.
    """
    try:
        while True:
            contact_id = input(f"Contact-ID ({CONTACT_ID_MIN} - {CONTACT_ID_MAX}): ").strip()
            if not contact_id:
                print("Contact-ID cannot be empty.")
                continue

            if not contact_id.isdigit() or len(contact_id) != 4:
                print("Contact-ID must consist of exactly four digits.")
                continue

            cid_value = int(contact_id)
            if not CONTACT_ID_MIN <= cid_value <= CONTACT_ID_MAX:
                print(f"Contact-ID must be between {CONTACT_ID_MIN} and {CONTACT_ID_MAX}.")
                continue

            if unique_id(contact_id):
                print("This Contact-ID already exists. Please choose another ID.")
            else:
                break

        firstname = input("Firstname: ").strip()
        lastname = input("Lastname: ").strip()

        phonenumber = input("Phonenumber (0041 00 00 00): ").strip()
        if phonenumber and not re.fullmatch(PHONE_REGEX, phonenumber):
            print("Invalid format. Use: 0041 00 00 00")
            return

        email = input("E-Mail: ").strip()
        if email and ("@" not in email or "." not in email):
            print("Invalid E-Mail address.")
            return

        if not phonenumber and not email:
            print("Please provide at least a phonenumber or an email.")
            return

        contacts = load_contacts()
        contacts.append({
            "id": contact_id,
            "firstname": firstname,
            "lastname": lastname,
            "phonenumber": phonenumber,
            "email": email,
        })
        save_contacts(contacts)

        print(f"\nContact '{firstname} {lastname}' was added successfully.")

    except Exception as e:
        print("Error while adding contact. Please try again:", e)

# --------------------------------------------------------------
# Delete contact FUNCTION
# --------------------------------------------------------------

def delete_contact():

    """
    The user is able to delete existing contacts from kontakte.txt
    """
    
    print("\n--- Delete Contact ---")  # Überschrift ausgeben
    search = input("Enter ID, Phonenumber or E-Mail: ").strip()  # Nutzer gibt Suchbegriff ein, um passenden Kontakt zu finden
    try:
        with open(CONTACT_FILE, "r", encoding="utf-8") as datei:
            lines = datei.readlines()
    except FileNotFoundError:
        print("Data was not found.")
        return
    
    if not lines: 
        print("Data does not exist.")
        return
    
    contacts = []
    buffer = []

    for line in lines:
        line = line.strip()
        if not line:
                continue

        if line == CONTACT_SEPERATOR:
            if len(buffer) == 5:
                cid, firstname, lastname, phonenumber, email = buffer
                contact = {
                    "id": cid,
                    "firstname": firstname,
                    "lastname": lastname,
                    "phonenumber": phonenumber,
                    "email": email
                }
                contacts.append(contact)
            buffer = []
            continue

        buffer.append(line)

# letzter Kontakt ohne ==== wird eingelesen
    if len(buffer) == 5:
        cid, firstname, lastname, phonenumber, email = buffer
        contact = {
            "id": cid,
            "firstname": firstname,
            "lastname": lastname,
            "phonenumber": phonenumber,
            "email": email
        }
        contacts.append(contact)

    found = None
    for c in contacts:
        if c["id"] == search or c["phonenumber"] == search or c["email"] == search:  # Prüfen, ob Eingabe zu diesem Kontakt passt
            found = c
            break

    if not found:
        print("Contact was not found.")
        return
        
    print(f"Found Contact:")  # Kontakt anzeigen
    print(f"{found['id']} – {found['firstname']} {found['lastname']} – {found['phonenumber']} – {found['email']}")  # Details ausgeben

    confirm = input("Do you really want to delete this contact (yes/no): ").strip().lower()  # Nutzer muss Löschung bestätigen

    if confirm != "yes":  # Wenn Nutzer „ja“ eingibt
        print("Process Canclled.")  # Meldung wenn nicht gelöscht wird
        return
        
        #Kontakt löschen
    contacts.remove(found)
    print("Contact has been deleted.") # Meldung, falls kein Kontakt zur Eingabe passt

# Überarbeitete Kontakte zurück in die Datei schreiben
    with open(CONTACT_FILE, "w", encoding="utf-8") as datei:
        for c in contacts:
            datei.write(f"{c['id']}\n")
            datei.write(f"{c['firstname']}\n")
            datei.write(f"{c['lastname']}\n")
            datei.write(f"{c['phonenumber']}\n")
            datei.write(f"{c['email']}\n")
            datei.write(CONTACT_SEPERATOR + "\n")
            
    print("Data is being updated.")


# --------------------------------------------------------------
# Edit contact FUNCTION
# --------------------------------------------------------------

def edit_contact():  
    """
    The user is able to edit single elements from kontakte.txt
    """
    print("\n--- Edit Contact ---")  # Überschrift ausgeben

    search = input("Enter ID, Phonenumber or E-Mail: ").strip()  # Nutzer gibt Suchbegriff ein, um Kontakt zu finden
    try:
        with open(CONTACT_FILE, "r", encoding="utf-8") as datei:
            lines = datei.readlines()
    except FileNotFoundError:
        print("Data does not exist.")
        return
    
    if not lines:
        print("No Contacts found.")
        return
    
    contacts = []
    buffer = []

    for line in lines:
        line = line.strip()
        if not line:
            continue

        if line == CONTACT_SEPERATOR:

            if len(buffer) == 5:
                cid, firstname, lastname, phonenumber, email = buffer
                contact = {
                    "id": cid,
                    "firstname": firstname,
                    "lastname": lastname,
                    "phonenumber": phonenumber,
                    "email": email
            }
            contacts.append(contact)
            buffer = []
            continue

        buffer.append(line)
    
    if len(buffer) == 5:
        cid, firstname, lastname, phonenumber, email = buffer
        contact = {
            "id": cid,
            "firstname": firstname,
            "lastname": lastname,
            "phonenumber": phonenumber,
            "email": email
        }
        contacts.append(contact)

    found = None  # Variable für später gespeicherten gefundenen Kontakt
    for c in contacts:  # Schleife geht durch alle Kontakte
        if c["id"] == search or c["phonenumber"] == search or c["email"] == search:  # Prüft, ob Eingabe zu einem Kontakt passt
            found = c  # Kontakt in Variable speichern
            break  # Schleife abbrechen, weil Kontakt gefunden wurde

    if not found:  # Wenn kein Kontakt gefunden wurde
        print("Contact was not found.")  # Fehlermeldung anzeigen
        return  # Funktion verlassen

    print(f"Contact found: ")  # Kontaktübersicht anzeigen
    print(f"{found['id']} – {found['firstname']} {found['lastname']} – {found['phonenumber']} – {found['email']}")  # Kontaktinformationen ausgeben

    print("What do you want to change?")  # Bearbeitungsmenü anzeigen
    print("1 - Firstname")
    print("2 - Lastname")
    print("3 - Phonenumber")
    print("4 - E-Mail")
    print("5 - Cancel")

    choice = input("Option: ")  # Nutzer wählt, welches Feld er bearbeiten will

    if choice == "1":  # Falls Nutzer Vorname ändern möchte
        found["firstname"] = input("New Firstname: ").strip()  # Neuer Name wird gespeichert

    elif choice == "2":  # Falls Nutzer Nachname ändern möchte
        found["lastname"] = input("New Lastname: ").strip()  # Neuer Vorname wird gespeichert

    elif choice == "3":  # Falls Nutzer Telefonnummer ändern will
        new_tel = input("New Phonenumber (0041 00 00 00): ").strip()
        if not re.fullmatch(PHONE_REGEX, new_tel):
            print("Invalid format. Use: 0041 00 00 00")
            return
        found["phonenumber"] = new_tel

    elif choice == "4":  # Falls Nutzer E-Mail ändern will
        new_email = input("Neue E-Mail: ").strip()  # Neue E-Mail abfragen
        if "@" not in new_email or "." not in new_email:  # Überprüfen, ob Format einer E-Mail entspricht
            print("Ungültige E-Mail-Adresse!")  # Fehlermeldung
            return  # Abbrechen, weil E-Mail ungültig
        found["email"] = new_email  # Neue E-Mail speichern

    elif choice == "5":  # Falls Nutzer abbrechen möchte
        print("Changes Cancelled.")  # Meldung ausgeben
        return  # Funktion verlassen
    else: 
        print("Invalid Option.")
        return
    print(" Contact was updated!")  # Erfolgsmeldung nach Bearbeitung

    #schreibt die Datei zurück in kontakte.txt
    with open(CONTACT_FILE, "w", encoding="utf-8") as datei:
        for c in contacts:
            datei.write(f"{c['id']}\n")
            datei.write(f"{c['firstname']}\n")
            datei.write(f"{c['lastname']}\n")
            datei.write(f"{c['phonenumber']}\n")
            datei.write(f"{c['email']}\n")
            datei.write(CONTACT_SEPERATOR + "\n")
    
    print("Date is being updated.")
        
            

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
    Lets the user search by name or user ID
    """
    try:
        search = input('\nSearch Contact (Enter name or ID): ').strip()
        if not search:
            print("Please enter a value to search.")
            return
        results = [] #sammelt die Treffer
        

        with open (CONTACT_FILE,'r', encoding="utf-8") as datei:

            while True:
                contact_id  = datei.readline()
                if not contact_id:
                    break
                
                contact_id = contact_id.strip()
                firstname = datei.readline().strip()
                lastname = datei.readline().strip()
                phonenumber = datei.readline().strip()
                email = datei.readline().strip()
                sep = datei.readline()

                if len(search) == 1 and search.isalpha():
                    if firstname.upper().startswith(search.upper()):
                        results.append((contact_id, firstname, lastname, phonenumber, email))
                else:
                    term = search.lower()
                    if (
                        term in contact_id.lower() or
                        term in firstname.lower() or 
                        term in lastname.lower() or 
                        term in phonenumber.lower() or 
                        term in email.lower()
                    ):
                        results.append((contact_id, firstname, lastname, phonenumber, email))
        
        results.sort(key=lambda contact: contact[1].upper())
        if results:
            print('\n=== SEARCH RESULTS  ===')
            for contact in results:
                cid, firstname, lastname, phonenumber, email = contact
                print(f"\nID: {cid}")
                print(f"Firstname: {firstname}")
                print(f"Lastname: {lastname}")
                print(f"Phonenumber: {phonenumber}")
                print(f"Email: {email}")

        else: 
                print("No contact found.")
        
    except FileNotFoundError as e:
        print("File not found.")


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
            delete_contact()
        elif choice == "3":
            edit_contact()
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
    """
    This is the entry point of the program.
    """
if __name__ == "__main__":
    main()
