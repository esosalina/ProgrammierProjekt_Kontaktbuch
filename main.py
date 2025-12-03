
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
    try:
        # Eingaben des Benutzers
        contact_id = input("Kontakt-ID: ").strip()
        vorname = input("Vorname: ").strip()
        nachname = input("Nachname: ").strip()
        telefonnummer = input("Telefonnummer: ").strip()
        email = input("E-Mail: ").strip()

        # Öffnet die Datei im Anhängemodus (fügt neuen Kontakt hinzu)
        with open("kontakte.txt", "a", encoding="utf-8") as file:
            file.write(contact_id + "\n")
            file.write(vorname + "\n")
            file.write(nachname + "\n")
            file.write(telefonnummer + "\n")
            file.write(email + "\n")

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
        with open(CONTACT_FILE, "r", encoding="utf-8") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print("Kontaktdatei nicht gefunden.")
        return
    if not lines: 
        print("Kontaktdatei nicht vorhanden")
        return
    
    contacts = []

    for i in range(0, len(lines), 4):  # Durch alle Kontakte iterieren
        try: 
            cid = lines[i].strip()
            vorname = lines[i+1].strip()
            name = lines [i+2].strip()
            telefon = lines [i+3].strip()
        except:
            continue # skips damaged entries
        contact = {

            "id": cid,
            "vorname": vorname,
            "name": name,
            "telefon": telefon,
            "email": ""
        }
        contacts.append(contact)
    
    for c in contacts:
        if c["id"] == search or c["telefon"] == search or c["email"] == search:  # Prüfen, ob Eingabe zu diesem Kontakt passt
            print(f"\Gefundener Kontakt:")  # Kontakt anzeigen
            print(f"{c['id']} – {c['name']} {c['vorname']} – {c['telefon']} – {c['email']}")  # Details ausgeben

            confirm = input("Wirklich löschen? (ja/nein): ").lower()  # Nutzer muss Löschung bestätigen

            if confirm == "ja":  # Wenn Nutzer „ja“ eingibt
                contacts.remove(c)  # Kontakt aus Liste löschen
                print("Kontakt wurde gelöscht.")  # Bestätigung ausgeben
            else:
                print("Löschen abgebrochen.")  # Meldung wenn nicht gelöscht wird
            break
    else:

        print("Kontakt nicht gefunden.") # Meldung, falls kein Kontakt zur Eingabe passt
        return
# Überarbeitete Kontakte zurück in die Datei schreiben

    with open(CONTACT_FILE, "w", encoding="utf-8") as f:
        for c in contacts:
            f.write(f"{c['id']}\n")
            f.write(f"{c['vorname']}\n")
            f.write(f"{c['name']}\n")
            f.write(f"{c['telefon']}\n")
            
    print("Datei wird aktualisiert.")


# --------------------------------------------------------------
# Edit contact FUNCTION
# --------------------------------------------------------------

def edit_contact():  
    print("\n--- Kontakt bearbeiten ---")  # Überschrift ausgeben

    search = input("ID, Telefonnummer oder E-Mail eingeben: ").strip()  # Nutzer gibt Suchbegriff ein, um Kontakt zu finden
    try:
        with open(CONTACT_FILE, "r", encoding="utf-8") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print("Kontaktdatei existiert nicht.")
        return
    
    if not lines:
        print("Keine Kontakte vorhanden.")
        return
    
    contacts = []
    
    for i in range(0, len(lines), 4):
        try:
            cid = lines[i].strip()
            vorname = lines[i+1].strip()
            name = lines [i+2].strip()
            telefon = lines [i+3].strip()
        except:
            continue
        contact = {
             "id": cid,
            "vorname": vorname,
            "name": name,
            "telefon": telefon,
            "email": ""
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

    print(f"\Gefundener Kontakt:")  # Kontaktübersicht anzeigen
    print(f"{found['id']} – {found['name']} {found['vorname']} – {found['telefon']} – {found['email']}")  # Kontaktinformationen ausgeben

    print("\Was möchten Sie ändern?")  # Bearbeitungsmenü anzeigen
    print("1 - Name")
    print("2 - Vorname")
    print("3 - Telefonnummer")
    print("4 - E-Mail")
    print("5 - Abbrechen")

    choice = input("Auswahl: ")  # Nutzer wählt, welches Feld er bearbeiten will

    if choice == "1":  # Falls Nutzer Name ändern möchte
        found["name"] = input("Neuer Name: ").strip()  # Neuer Name wird gespeichert

    elif choice == "2":  # Falls Nutzer Vorname ändern möchte
        found["vorname"] = input("Neuer Vorname: ").strip()  # Neuer Vorname wird gespeichert

    elif choice == "3":  # Falls Nutzer Telefonnummer ändern will
        new_tel = input("Neue Telefonnummer: ").strip()  # Neue Telefonnummer abfragen
        if not new_tel.isdigit():  # Prüfen ob Nummer nur Zahlen enthält
            print("Telefonnummer muss nur Zahlen enthalten!")  # Fehlermeldung ausgeben
            return  # Abbrechen, weil Telefonnummer ungültig
        found["telefon"] = new_tel  # Neue Telefonnummer speichern

    elif choice == "4":  # Falls Nutzer E-Mail ändern will
        new_email = input("Neue E-Mail: ").strip()  # Neue E-Mail abfragen
        if "@" not in new_email or "." not in new_email:  # Überprüfen, ob Format einer E-Mail entspricht
            print("Ungültige E-Mail-Adresse!")  # Fehlermeldung
            return  # Abbrechen, weil E-Mail ungültig
        found["email"] = new_email  # Neue E-Mail speichern

    elif choice == "5":  # Falls Nutzer abbrechen möchte
        print("Änderung abgebrochen.")  # Meldung ausgeben
        return  # Funktion verlassen
    else: 
        print("Ungültige Auswahl.")
        return
    print(" Kontakt wurde aktualisiert!")  # Erfolgsmeldung nach Bearbeitung

    with open(CONTACT_FILE, "w", encoding="utf-8") as f:
        for c in contacts:
            f.write(f"{c['id']}\n")
            f.write(f"{c['vorname']}\n")
            f.write(f"{c['name']}\n")
            f.write(f"{c['telefon']}\n")
    
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
