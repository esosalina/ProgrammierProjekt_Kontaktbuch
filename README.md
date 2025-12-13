
# Kontaktbuch-Manager

Gruppenmitglieder: Arthur Saryan, David Kopp, Numana Sajid, Naomi Uwensuyi
Dozierede: Härer Felix, Grieder Hermann

Willkommen zu unserem Programmierprojekt

Diese Anwendung dient als einfaches Verwaltungstool für Kontakte und ermöglicht es Nutzern, ihre persönlichen sowie geschäftlichen Kontaktinformationen zentral zu organisieren. Nutzer können neue Kontakte erstelle mit Angaben wie Name, Telefonnummer und E-Mail-Adresse, bestehende Einträge bearbeiten oder löschen und ihre gespeicherten Daten gezielt durchsuchen. Alle Kontaktinformationen werden dauerhaft lokal in Dateien gespeichert, sodass sie jederzeit zuverlässig verfügbar sind. 

---------------------------------------------------------------------------------------------------------------------------------------------

# Hauptfunktionen und Benutzerablauf 

# Funktionsübersicht

- Create_contact: Hier werden neue Kontakte mit Vorname, Nachname, Telefonummer und E-mail adresse erfasst. 

- Delete_Contact: Kontakte könne über eine eindeutige ID, Telefonnummer oder E-Mail-Adresse gelöscht werden. 

- Edit_Contact: Bestehende Kontakte können geändert werden, ohne sie neu anlegen zu müssen. 

- Search_Contact: Kontakte können nach Vornamen, Telefonnummer oder E-Mail-Adresse gefunden werden. Auch Teiltreffer sind möglich, z.b man gibt nur den Buchstaben "A" ein und es werden alle Vornamen aufgelistet die mit dem Buchstaben "A" beginnen. 

- Results.sort(): Mit dieser Funktion sind die Teiltreffer möglich und werden Alphabetisch nach dem Vornamen sortiert. 

- Calls: Es können Anrufe über Eingabe von Kontakt oder Telefonnummer. Vergangene Anrufe werden abgespeichert und können abgerufen werden. 

- Speicher und Beenden: Alle Kontaktdaten werden dauerhaft in der Datei "kontakte.txt" gespeichert, auch nach dem das Programm beendet wurde. 

---------------------------------------------------------------------------------------------------------------------------------------------
# Programmablauf

Beim Programmstart erscheint ein menügesteuertes Hauptmenü mit mehreren Optionen von 1-6. Nach der Auswahl einer Option wird die gewünschte Funktion ausgeführt, das Ergebnis angezeigt und anschliessend zum Hauptmenü zurückgekehrt, bis der Benutzer das Programm beendet und alle Daten gespeichert werden.

#Datenspeicherung

- kontakte.txt: Speichert alle Kontakte mit User-ID, Vorname, Nachname, Telefonnummer und E-mail Adresse. Die Datei wird beim Programmstart geladen. 

- calls.txt: Speichert alle vergangenen Anrufe mit Datum, Zeit,Telefonnummer und Voramen

Die Anwendung verwendet dann ausschliesslich lokale Dateien, sodass die Kontaktinformationen unabhängig von externen Diensten dauerhaft verfügbar bleiben.

---------------------------------------------------------------------------------------------------------------------------------------------

# Installation und Start

Voraussetzung für die Verwendung dieses Programms ist die Installation von Python 3.2 oder höher. 
Die Projektdateien main.py, kontakte.txt und calls.txt in einem gemeinsamen Projektordner ablegen

Danach das Programm im Terminal starten mit python main.py oder den play Button in der main.py.

Im Hauptmenü dann die gewünschte Funktion per Zahleneingabe auswählen und den Eingabeaufforderungen folgen.

---------------------------------------------------------------------------------------------------------------------------------------------

# Technische Umsetzung

Das Projekt verwendet folgende Python-Konzepte: 

Datentypen: Strings, Floats, Integers, Listen, Dictionaries 

Kontrollstrukturen: if/elif/else, while-Schleifen (Menü), for-Schleifen (Kontaktsuche) 

Funktionen: Separate Funktionen für jede Hauptfunktion (create_contact, check_contact, show_contacts, etc.) 

Dateiverarbeitung: open(), read(), write() 

Exception-Handling: try-except für Eingabevalidierung und Dateioperationen 

String-Operationen: Formatierung, E-Mail- und Telefonnummer-Validierung 

---------------------------------------------------------------------------------------------------------------------------------------------

# Zielgruppe

Die Anwendung richtet sich an Nutzer, die ihre persönlichen oder geschäfltichen Kontakte lokal und ohne komplexe Software speichern, verwalten und schnell wiederfinden möchte. Durch das einfache Konsolenmenü und die dauerhafte Datenspeicherung eigent sich das Programm besonders als Lernprojekt für den Einstieg in Python und praktische Datenverarbeitung.n 