def add_contact():
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
        print(" Fehler beim Hinzufügen des Kontakt:", e)