def delete_contact(contacts):
    print("\n--- Kontakt löschen ---")  # Überschrift ausgeben
    search = input("ID, Telefonnummer oder E-Mail eingeben: ").strip()  # Nutzer gibt Suchbegriff ein, um passenden Kontakt zu finden

    for c in contacts:  # Durch alle Kontakte iterieren
        if c["id"] == search or c["telefon"] == search or c["email"] == search:  # Prüfen, ob Eingabe zu diesem Kontakt passt
            print(f"\Gefundener Kontakt:")  # Kontakt anzeigen
            print(f"{c['id']} – {c['name']} {c['vorname']} – {c['telefon']} – {c['email']}")  # Details ausgeben

            confirm = input("Wirklich löschen? (ja/nein): ").lower()  # Nutzer muss Löschung bestätigen

            if confirm == "ja":  # Wenn Nutzer „ja“ eingibt
                contacts.remove(c)  # Kontakt aus Liste löschen
                print("Kontakt wurde gelöscht.")  # Bestätigung ausgeben
            else:
                print("Löschen abgebrochen.")  # Meldung wenn nicht gelöscht wird
            return  # Funktion verlassen (egal ob gelöscht oder abgebrochen)

    print("Kontakt nicht gefunden.") # Meldung, falls kein Kontakt zur Eingabe passt
