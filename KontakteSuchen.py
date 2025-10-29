# Kontakte nach Namen, Telefonnummer oder E-Mail-Adresse finden (auch Teiltreffer). 

def search_contact ():

    try:
        search = input('\nSuche Kontakt: ').lower() 
        with open ('kontakte.txt', 'r') as datei:

            found = False 

            contact_id  = datei.readline()
            firstname = datei.readline()
            lastname = datei.readline()
            phonenumber = datei.readline()

#wird nur ausgeführt wenn wir einen Kontakt gefunden haben
            if(search in firstname.lower() or search in lastname.lower()):

                if
        
    except FileNotFoundError as e:
        print("Contact not found.")

