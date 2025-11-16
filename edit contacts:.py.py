def edit_contact(contacts):  
    print("\n--- Kontakt bearbeiten ---")  # Überschrift ausgeben

    search = input("ID, Telefonnummer oder E-Mail eingeben: ").strip()  # Nutzer gibt Suchbegriff ein, um Kontakt zu finden

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
            print("❌ Telefonnummer muss nur Zahlen enthalten!")  # Fehlermeldung ausgeben
            return  # Abbrechen, weil Telefonnummer ungültig
        found["telefon"] = new_tel  # Neue Telefonnummer speichern

    elif choice == "4":  # Falls Nutzer E-Mail ändern will
        new_email = input("Neue E-Mail: ").strip()  # Neue E-Mail abfragen
        if "@" not in new_email or "." not in new_email:  # Überprüfen, ob Format einer E-Mail entspricht
            print("❌ Ungültige E-Mail-Adresse!")  # Fehlermeldung
            return  # Abbrechen, weil E-Mail ungültig
        found["email"] = new_email  # Neue E-Mail speichern

    elif choice == "5":  # Falls Nutzer abbrechen möchte
        print("Änderung abgebrochen.")  # Meldung ausgeben
        return  # Funktion verlassen

    print(" Kontakt wurde aktualisiert!")  # Erfolgsmeldung nach Bearbeitung

