import random
from faker import Faker 
import string

def generateEmail():
    dummy = Faker('it_IT')
    
    name = dummy.first_name_male()
    surname = dummy.last_name()
    domain = dummy.domain_name()

    return f"{name}.{surname}@{domain}"

def get_random_string(length):
    # choose from all lowercase letter
    result_str = ''.join(random.choice(string.ascii_letters) for i in range(length))
    return result_str

def insertUtenti():
    fake = Faker('it_IT')
    #name = ["Franco","Leonardo","Nicolò","Alessandro","Marco","Luca","Gianni","Giulio","Matteo"]
    #surname = ["Salvucci","Spadoni","Ascenzi","Rossi","Verdi","Bianchi"]

    for i in range(3000):
        name = fake.first_name_male()
        surname = fake.last_name()
        domain = fake.domain_name()
        email = f"{name}.{surname}@{domain}"
        query = "INSERT INTO Utenti (Nome,Cognome,Email,Psw,Ruolo) VALUES ('"+str(name)+"','"+str(surname)+"','"+str(email)+"','"+str(get_random_string(15))+"','"+str(random.randint(2,3))+"');"
        print(query)
    
insertUtenti()
#random_mail = generateEmail()
#print(random_mail)
