# Kontaktbuch-Manager

Willkommen zu unserem Programierprojekt

Diese Anwendung dient als einfaches Verwaltungstool für Kontakte und ermöglicht es Nutzern, ihre persönlichen sowie geschäftlichen Kontaktinformationen zentral zu organisieren. Nutzer können neue Kontakte mit Angaben wie Name, Telefonnummer und E-Mail-Adresse hinzufügen, bestehende Einträge bearbeiten oder löschen und ihre gespeicherten Daten gezielt durchsuchen. Alle Kontaktinformationen werden dauerhaft lokal in Dateien gespeichert, sodass sie jederzeit zuverlässig verfügbar sind. 

Die Anwendung richtet sich an Nutzer, die ihre persönlichen oder geschäftlichen Kontakte digital speichern, verwalten und schnell wiederfinden möchten. 

---------------------------------------------------------------------------------------------------------------------------------------------

# Hauptfunktionen und Benutzerablauf 

# Funktionsübersicht
Daten speichern und Programm beenden Kontakte speichern:Alle Daten werden dauerhaft in einer Datei abgelegt. 
Hinzufügen: Neue Kontakte mit Namen, Telefonnummer, E-Mail eintragen. 
Entfernen: Kontakte anhand einer eindeutigen ID, Telefonnummer oder E-Mail-Adresse löschen. 
Bearbeiten: Bestehende Kontakte ändern, ohne sie neu anlegen zu müssen  
Suchen: Kontakte nach Namen, Telefonnummer oder E-Mail-Adresse finden (auch Teiltreffer). 
Auflisten: Alle gespeicherten Kontakte anzeigen, sortiert nach Namen oder E-Mail. (Filtern) 
Anrufe: Anrufe tätigen über Eingabe von Kontakt oder Telefonnummer. Vergangene Anrufe werden abgespeichert und können abgerufen werden. 

---------------------------------------------------------------------------------------------------------------------------------------------
# Programmablauf

Programmstart → HAUPTMENÜ (zeigt Optionen 1-5 an) 

       ↓ 

Benutzer wählt Option → Ausführung der gewählten Funktion 

       ↓ 

Anzeige von Ergebnissen / Bestätigung 

       ↓ 

Rückkehr zum HAUPTMENÜ (Schleife läuft bis zum Beenden) 

       ↓ 
       
Speichern aller Daten → Programmende 

---------------------------------------------------------------------------------------------------------------------------------------------

# Technische Anforderungen

Das Projekt verwendet folgende Python-Konzepte: 

Datentypen: Strings, Floats, Integers, Listen, Dictionaries 

Kontrollstrukturen: if/elif/else, while-Schleifen (Menü), for-Schleifen (Kontaktsuche) 

Funktionen: Separate Funktionen für jede Hauptfunktion (create_contact, check_contact, show_contacts, etc.) 

Dateiverarbeitung: open(), read(), write() 

Exception-Handling: try-except für Eingabevalidierung und Dateioperationen 

String-Operationen: Formatierung, E-Mail- und Telefonnummer-Validierung 

---------------------------------------------------------------------------------------------------------------------------------------------
