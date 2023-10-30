import random
from faker import Faker 
import string
import datetime
from lorem_text import lorem


def generateEmail():
    dummy = Faker('it_IT')
    
    name = dummy.first_name_male()
    surname = dummy.last_name()
    domain = dummy.domain_name()

    return f"{name}.{surname}@{domain}"

def genCarLicens():
    pool_letter = "ABCDEFGHIJKLMOPQRSTUVWXYZ"
    pool_num = "0123456789"
    l1 = random.choice(pool_letter)
    l2 = random.choice(pool_letter)
    l3 = random.choice(pool_letter)
    l4 = random.choice(pool_letter)

    n1 = random.choice(pool_num)
    n2 = random.choice(pool_num)
    n3 = random.choice(pool_num)

    return l1+l2+""+n1+n2+n3+l3+l4

def genRandomDate():
    start_date = datetime.date(2020, 1, 1)
    end_date   = datetime.date(2024, 12, 30)
    num_days   = (end_date - start_date).days
    rand_days   = random.randint(1, num_days)
    random_date = start_date + datetime.timedelta(days=rand_days)
    return random_date

def get_random_string(length):
    # choose from all lowercase letter
    result_str = ''.join(random.choice(string.ascii_letters) for i in range(length))
    return result_str

def insertUtenti():
    '''
    Genera random gli utenti
    '''
    fake = Faker('it_IT')
    #name = ["Franco","Leonardo","Nicolò","Alessandro","Marco","Luca","Gianni","Giulio","Matteo"]
    #surname = ["Salvucci","Spadoni","Ascenzi","Rossi","Verdi","Bianchi"]

    for i in range(3000):
        name = fake.first_name()
        surname = fake.last_name()
        domain = fake.domain_name()
        email = f"{name}.{surname}@{domain}"
        query = "INSERT INTO Utenti (Nome,Cognome,Email,Psw,Ruolo) VALUES ('"+str(name)+"','"+str(surname)+"','"+str(email)+"','"+str(get_random_string(15))+"','"+str(random.randint(2,3))+"');"
        print(query)

print("-------------------------------------- Inizio insert utenti")    
insertUtenti()
print("-------------------------------------- Fine insert Utenti")
def insertVeicoli():
    '''
    Genera random i veicoli
    '''
    model = ["BMW","Audi","Mercedes"]
    model_m = ["RS7","Benz","R8"]
    cap = [3,6,9]
    # per impostare l'autista lanciare la query:
    # UPDATE Veicoli
	# SET ID_Autista = (
	#   SELECT IDU
	#   FROM Utenti
	#   WHERE Ruolo = 2
	#   ORDER BY RAND() -- Utilizza RANDOM() o equivalente per il tuo database
	#   LIMIT 1
	# )
	# WHERE ID_Autista IS NOT NULL;

    for i in range(3000):
        query = "INSERT INTO Veicoli (Targa,Modello,Marca,Capienza,ID_Autista) values ('"+str(genCarLicens())+"','"+str(random.choice(model))+"','"+str(random.choice(model_m))+"','"+str(random.choice(cap))+"',NULL);"
        #genCarLicens()
        print(query)
#random_mail = generateEmail()
#print(random_mail)
print("-------------------------------------- Inizio insert veicoli")
insertVeicoli()
print("-------------------------------------- Fine insert veicoli")
def insertFeedback():
    words = 10
    print(lorem.words(words))
    for i in range(3000):
        query  ="INSERT INTO Feedback (Stelle,Commento,Data,Id_Utente) values ('"+str(random.randint(1,5))+"','"+str(lorem.sentence())+"','"+str(genRandomDate())+"',NULL);"
        print(query)
print("-------------------------------------- Inizio insert feedback")
insertFeedback()
print("-------------------------------------- Fine insert feedback")
#help(insertUtenti)