# Kontakte nach Namen, Telefonnummer oder E-Mail-Adresse finden (auch Teiltreffer). 

def search_contact ():
    """ 
    Lets the user search by name or user ID
    """
    try:
        search = input('\nSearch Contact: ').lower().strip() 

        with open ('kontakte.txt', 'r') as datei:
            found = False 

            while True:
                
                contact_id  = datei.readline().strip()

                if not contact_id:
                    break
                
                firstname = datei.readline().strip()
                lastname = datei.readline().strip()
                phonenumber = datei.readline().strip()

#wird nur ausgeführt wenn wir einen Kontakt gefunden haben
                if(search in firstname.lower() or search in lastname.lower() or search in phonenumber or search in contact_id):

                    if not found:
                        found = True
                        print('\n=== SEARCH RESULTS  ===')
                        found = True
                       
                        print(f"ID: {contact_id}")
                        print(f"Firstname: {firstname}")
                        print(f"Lastname: {lastname}")
                        print(f"Phonenumber: {phonenumber}")

            if not found:
                print("No contact found.")
        
    except FileNotFoundError as e:
        print("File not found.")

def contact_filter():
    
    with open("kontakte.txt", "r") as datei:
        contacts = datei.readlines()
        return contacts

#Programmstart
if __name__ == '__main__':
    search_contact()

