
# Kontaktbuch-Manager

Gruppenmitglieder: Arthur Saryan, David Kopp, Numana Sajid, Naomi Uwensuyi

Dozierede: Härer Felix, Grieder Hermann

Willkommen zu unserem Programmierprojekt

Diese Anwendung dient als einfaches Verwaltungstool für Kontakte und ermöglicht es den Nutzern, ihre persönlichen sowie geschäftlichen Kontaktinformationen zentral zu organisieren. Nutzer können neue Kontakte mit Angaben wie Vorname und Nachname, Telefonnummer und E-Mail-Adresse erstellen, bestehende Einträge bearbeiten oder löschen und ihre gespeicherten Daten gezielt durchsuchen. Alle Kontaktinformationen werden dauerhaft lokal in Dateien gespeichert und sind dadurch jederzeit zuverlässig verfügbar. 

---------------------------------------------------------------------------------------------------------------------------------------------

# Hauptfunktionen und Benutzerablauf 

# Funktionsübersicht

- Create_contact: Neue Kontakte mit Vorname, Nachname, Telefonummer und E-mail Adresse erfasst. 

- Delete_Contact: Kontakte können über eine eindeutige ID, Telefonnummer oder E-Mail-Adresse gelöscht werden. 

- Edit_Contact: Bestehende Kontakte können geändert werden, ohne sie neu anlegen zu müssen. 

- Search_Contact: Kontakte können nach Vorname, Telefonnummer oder E-Mail-Adresse gesucht werden. Auch Teiltreffer sind möglich, z.b bei der Eingabe des Buchstabens "A" werden alle Vornamen angezeigt, die mit "A" beginnen. 

- Results.sort(): Diese Funktion ermöglicht die alphabetische Sortierung der Suchergebnisse nach Vornamen. 

- Calls: Anrufe können über Eingabe des Kontakts oder der Telefonnummer getätigt werden. Vergangene Anrufe werden gespeichert und können später eingesehen werden.  

- Speicher und Beenden: Alle Kontaktdaten werden dauerhaft in der Datei "kontakte.txt" gespeichert, auch nach dem Beenden des Programms. 

---------------------------------------------------------------------------------------------------------------------------------------------
# Programmablauf

Beim Programmstart erscheint ein menügesteuertes Hauptmenü mit verschiedenen Optionen von 1-6. 
Nach der Auswahl einer Option wird die gewünschte Funktion ausgeführt, das Ergebnis angezeigt und anschliessend zum Hauptmenü zurückgekehrt. Das Programm läuft, bis der Benutzer es beendet, wobei alle Daten gespeichert werden. 

# Datenspeicherung

- kontakte.txt: Speichert alle Kontakte mit Benutzer-ID, Vorname, Nachname, Telefonnummer und E-mail Adresse. Die Datei wird beim Programmstart automatisch geladen. 

- calls.txt: Speichert alle vergangenen Anrufe mit Datum, Zeit, Telefonnummer und Vorname. 

Die Anwendung verwendet dann ausschliesslich lokale Dateien, sodass alle Kontaktinformationen unabhängig von externen Diensten dauerhaft verfügbar bleiben.

---------------------------------------------------------------------------------------------------------------------------------------------

# Installation und Start

Voraussetzung für die Verwendung dieses Programms ist die Installation von Python 3.12 oder höher. 
Die Projektdateien main.py, kontakte.txt und calls.txt müssen sich im selben Projektordner befinden. 

Das Programm kann im Terminal mit "python main.py" oder über den Play Button in der main.py gestartet werden.

Im Hauptmenü wird anschliessend die gewünschte Funktion per Zahleneingabe ausgewählt, und der Nutzer folgt den Eingabeaufforderungen.

---------------------------------------------------------------------------------------------------------------------------------------------

# Technische Umsetzung

Das Projekt verwendet folgende Python-Konzepte: 

- Datentypen: Strings, Floats, Integers, Listen, Dictionaries 

- Kontrollstrukturen: if/elif/else, while-Schleifen (Menü), for-Schleifen (z.b für die Kontaktsuche) 

- Funktionen: Separate Funktionen für jede Hauptfunktion (create_contact, edit_contact, show_contacts, etc.) 

- Dateiverarbeitung: open(), read(), write() 

- Exception-Handling: try-except für Eingabevalidierung und Dateioperationen 

- String-Operationen: Formatierung, E-Mail- und Telefonnummer-Validierung 

---------------------------------------------------------------------------------------------------------------------------------------------

# Zielgruppe

Die Anwendung richtet sich an Nutzer, die ihre persönlichen oder geschäfltichen Kontakte lokal und ohne komplexe Software speichern, verwalten und schnell wiederfinden möchten. 
Durch das einfache Konsolenmenü und die dauerhafte Datenspeicherung eignet sich das Programm besonders gut als Lernprojekt für den Einstieg in Python und die praktische Arbeit mit Dateien und Datenstrukturen.