
import re
from datetime import datetime

# --------------------------------------------------------------
# CONSTANTS
# --------------------------------------------------------------
CONTACT_FILE = "kontakte.txt"  # file to store contacts
CALLS_FILE = "calls.txt"  # file to store call logs
PHONE_REGEX = r"0041 \d{2} \d{2} \d{2}"  # Swiss phone format (0041 00 00 00)
CONTACT_SEPERATOR = "=======" #trennt die Kontakte von einander in kontakte.txt (übersichtlicher)


# --------------------------------------------------------------
# HELPER FUNCTIONS (INPUT VALIDATION)
# --------------------------------------------------------------

def input_phone(prompt="Telefonnummer (nur Zahlen): "):
   
    while True:
        number = input(prompt).strip()  # Leerzeichen entfernen
        if number.isdigit():            # Prüfen ob nur Zahlen
            return number               # Gültige Eingabe zurückgeben
        print("Fehler: Telefonnummer darf nur Zahlen enthalten.")

def input_email_letters_only(prompt="E-Mail (nur Buchstaben, @ und .): "):
    
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
# Create contact FUNCTION
# --------------------------------------------------------------

def create_contact():
    try:
        # Eingaben des Benutzers
        contact_id = input("Kontakt-ID: ").strip()
        vorname = input("Vorname: ").strip()
        nachname = input("Nachname: ").strip()
        telefonnummer = input_phone()
        email = input_email_letters_only()

        # Öffnet die Datei im Anhängemodus (fügt neuen Kontakt hinzu)
        with open("kontakte.txt", "a", encoding="utf-8") as datei:
            datei.write(contact_id + "\n")
            datei.write(vorname + "\n")
            datei.write(nachname + "\n")
            datei.write(telefonnummer + "\n")
            datei.write(email + "\n")
            datei.write(CONTACT_SEPERATOR + "\n")

        print(f"\n Kontakt '{vorname} {nachname}' wurde erfolgreich hinzugefügt.")

    except Exception as e:
        print(" Fehler beim Hinzufügen des Kontakts:", e)

# --------------------------------------------------------------
# Delete contact FUNCTION
# --------------------------------------------------------------

def delete_contact():
    print("\n--- Kontakt löschen ---")  # Überschrift ausgeben
    search = input("ID, Telefonnummer oder E-Mail eingeben: ").strip()  # Nutzer gibt Suchbegriff ein, um passenden Kontakt zu finden
    try:
        with open(CONTACT_FILE, "r", encoding="utf-8") as datei:
            lines = datei.readlines()
    except FileNotFoundError:
        print("Kontaktdatei nicht gefunden.")
        return
    
    if not lines: 
        print("Kontaktdatei nicht vorhanden")
        return
    
    contacts = []
    buffer = []

    for line in lines:
        line = line.strip()
        if not line:
                continue

        if line == CONTACT_SEPERATOR:
            if len(buffer) == 5:
                cid, vorname, nachname, telefon, email = buffer
                contact = {
                    "id": cid,
                    "vorname": vorname,
                    "nachname": nachname,
                    "telefon": telefon,
                    "email": email
                }
                contacts.append(contact)
            buffer = []
            continue

        buffer.append(line)

#letzter Kontakt ohne ==== wird eingelesen
    if len(buffer) == 5:
        cid, vorname, nachname, telefon, email = buffer
        contact = {
            "id": cid,
            "vorname": vorname,
            "nachname": nachname,
            "telefon": telefon,
            "email": email
        }
        contacts.append(contact)

    found = None
    for c in contacts:
        if c["id"] == search or c["telefon"] == search or c["email"] == search:  # Prüfen, ob Eingabe zu diesem Kontakt passt
            found = c
            break

    if not found:
        print("Kontakt nicht gefunden.")
        return
        
    print(f"Gefundener Kontakt:")  # Kontakt anzeigen
    print(f"{found['id']} – {found['vorname']} {found['nachname']} – {found['telefon']} – {found['email']}")  # Details ausgeben

    confirm = input("Wirklich löschen? (ja/nein): ").strip().lower()  # Nutzer muss Löschung bestätigen

    if confirm != "ja":  # Wenn Nutzer „ja“ eingibt
        print("Löschen abgebrochen.")  # Meldung wenn nicht gelöscht wird
        return
        
        #Kontakt löschen
    contacts.remove(found)
    print("Kontakt wurde gelöscht.") # Meldung, falls kein Kontakt zur Eingabe passt
# Überarbeitete Kontakte zurück in die Datei schreiben

    with open(CONTACT_FILE, "w", encoding="utf-8") as datei:
        for c in contacts:
            datei.write(f"{c['id']}\n")
            datei.write(f"{c['vorname']}\n")
            datei.write(f"{c['nachname']}\n")
            datei.write(f"{c['telefon']}\n")
            datei.write(f"{c['email']}\n")
            datei.write(CONTACT_SEPERATOR + "\n")
            
    print("Datei wird aktualisiert.")


# --------------------------------------------------------------
# Edit contact FUNCTION
# --------------------------------------------------------------

def edit_contact():  
    print("\n--- Kontakt bearbeiten ---")  # Überschrift ausgeben

    search = input("ID, Telefonnummer oder E-Mail eingeben: ").strip()  # Nutzer gibt Suchbegriff ein, um Kontakt zu finden
    try:
        with open(CONTACT_FILE, "r", encoding="utf-8") as datei:
            lines = datei.readlines()
    except FileNotFoundError:
        print("Kontaktdatei existiert nicht.")
        return
    
    if not lines:
        print("Keine Kontakte vorhanden.")
        return
    
    contacts = []
    buffer = []

    for line in lines:
        line = line.strip()
        if not line:
            continue

        if line == CONTACT_SEPERATOR:

            if len(buffer) == 5:
                cid, vorname, nachname, telefon, email = buffer
                contact = {
                    "id": cid,
                    "vorname": vorname,
                    "nachname": nachname,
                    "telefon": telefon,
                    "email": email
            }
            contacts.append(contact)
            buffer = []
            continue

        buffer.append(line)
    
    if len(buffer) == 5:
        cid, vorname, nachname, telefon, email = buffer
        contact = {
            "id": cid,
            "vorname": vorname,
            "nachname": nachname,
            "telefon": telefon,
            "email": email
        }
        contacts.append(contact)

    found = None  # Variable für später gespeicherten gefundenen Kontakt
    for c in contacts:  # Schleife geht durch alle Kontakte
        if c["id"] == search or c["telefon"] == search or c["email"] == search:  # Prüft, ob Eingabe zu einem Kontakt passt
            found = c  # Kontakt in Variable speichern
            break  # Schleife abbrechen, weil Kontakt gefunden wurde

    if not found:  # Wenn kein Kontakt gefunden wurde
        print("Kontakt wurde nicht gefunden.")  # Fehlermeldung anzeigen
        return  # Funktion verlassen

    print(f"Gefundener Kontakt:")  # Kontaktübersicht anzeigen
    print(f"{found['id']} – {found['vorname']} {found['nachname']} – {found['telefon']} – {found['email']}")  # Kontaktinformationen ausgeben

    print("\Was möchten Sie ändern?")  # Bearbeitungsmenü anzeigen
    print("1 - Vorname")
    print("2 - Nachname")
    print("3 - Telefonnummer")
    print("4 - E-Mail")
    print("5 - Abbrechen")

    choice = input("Auswahl: ")  # Nutzer wählt, welches Feld er bearbeiten will

    if choice == "1":  # Falls Nutzer Vorname ändern möchte
        found["vorname"] = input("Neuer Vorname: ").strip()  # Neuer Name wird gespeichert

    elif choice == "2":  # Falls Nutzer Nachname ändern möchte
        found["nachname"] = input("Neuer Nachname: ").strip()  # Neuer Vorname wird gespeichert

    elif choice == "3":  # Falls Nutzer Telefonnummer ändern will
        found["telefon"] = input_phone("Neue Telefonnummer: ")


    elif choice == "4":  # Falls Nutzer E-Mail ändern will
        found["email"] = input_email_letters_only("Neue E-Mail: ")


    elif choice == "5":  # Falls Nutzer abbrechen möchte
        print("Änderung abgebrochen.")  # Meldung ausgeben
        return  # Funktion verlassen
    else: 
        print("Ungültige Auswahl.")
        return
    print(" Kontakt wurde aktualisiert!")  # Erfolgsmeldung nach Bearbeitung

    #schreibt die Datei zurück in kontakte.txt
    with open(CONTACT_FILE, "w", encoding="utf-8") as datei:
        for c in contacts:
            datei.write(f"{c['id']}\n")
            datei.write(f"{c['vorname']}\n")
            datei.write(f"{c['nachname']}\n")
            datei.write(f"{c['telefon']}\n")
            datei.write(f"{c['email']}\n")
            datei.write(CONTACT_SEPERATOR + "\n")
    
    print("Datei wird akualisiert.")
        
            

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
if __name__ == "__main__":
    main()
