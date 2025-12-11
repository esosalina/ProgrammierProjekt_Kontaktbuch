import re

# Schweizer Telefonnummern-Regex: 0041 00 00 00
PHONE_REGEX = r"^0041 ?\d{2} ?\d{2} ?\d{2} ?\d{2}$"

def add_contact():
    try:
        contact_id = input("Kontakt-ID: ").strip()
        vorname = input("Vorname: ").strip()
        nachname = input("Nachname: ").strip()
        
        """
        Asks user for a phone number, validates format,
        and adds the number if the format is correct.
        """
        number = input("Enter phonenumber (0041 00 00 00): ").strip()

        # Validate the number format using regex
        if number and not re.fullmatch(PHONE_REGEX, number):
            print("Invalid format. Use: 0041 00 00 00")
            return
        
        email = input("E-Mail: ").strip()

        # Prüfung: Mindestens Telefonnummer ODER E-Mail muss ausgefüllt sein
        if not number and not email:
            print("\nFehler: Bitte mindestens Telefonnummer ODER E-Mail angeben.")
            return

        # Kontakt speichern
        with open("kontakte.txt", "a", encoding="utf-8") as file:
            file.write(contact_id + "\n")
            file.write(vorname + "\n")
            file.write(nachname + "\n")
            file.write(number + "\n")
            file.write(email + "\n")

        print(f"\nKontakt '{vorname} {nachname}' wurde erfolgreich hinzugefügt.")

    except Exception as e:
        print("Fehler beim Hinzufügen des Kontakts:", e)
