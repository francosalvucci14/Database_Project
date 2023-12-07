import random
from faker import Faker
import string
import decimal
import datetime

fake = Faker("it_IT")


def genRandomDate():
    start_date = datetime.date(1975, 1, 1)
    end_date = datetime.date(2001, 12, 30)
    num_days = (end_date - start_date).days
    rand_days = random.randint(1, num_days)
    random_date = start_date + datetime.timedelta(days=rand_days)

    return random_date


def generateEmail(name, surname):
    # dummy = Faker("it_IT")

    # name = dummy.first_name_male()
    # surname = dummy.last_name()
    domain = fake.domain_name()

    return f"{name}.{surname}@{domain}"


print("Inizio esecuzione...")

print("L'ORDINE DI ESECUZIONE DEI FILE È 1.txt,2.txt,etc...")

print("Inizio Creazione 1.txt")

SYMBOLS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
NUMBERS = "0123456789"
ALL_SYMBOLS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# random_name = ""
f = open("1.txt", "w+")
f.write("---------------Inizio Inserimento Personale---------------\n")
random_id = ""
unique_Personale = ["''"]


for i in range(6000):
    data = genRandomDate()
    surname = fake.last_name()
    name = fake.first_name()
    email = str(generateEmail(name, surname))
    #random_id = "".join(random.choice(NUMBERS) for i in range(3))
    random_id = str(i)
    unique_Personale.append(random_id)
    query = (
        "INSERT INTO Personale (ID,Nome,Cognome,DDN,NumeroDiTelefono,Email) VALUES ('"
        + random_id
        + "','"
        + name
        + "','"
        + surname
        + "','"
        + str(data)
        + "','"
        + fake.phone_number()
        + "','"
        + email
        + "');"
    )
    f.write(query)
    f.write("\n")

f.write("---------------Fine Inserimento Personale---------------\n")
f.write("---------------Inizio Inserimento Addetti Marketing---------------\n")
# parte addetti marketing
unique_AddMark = ["''"]

ruoli = ["Responsabile", "Analista", "Coordinatore"]

for i in range(3000):
    # random_name = "".join(random.choice(NUMBERS) for i in range(3))
    random_ruolo = random.choice(ruoli)
    random_id = unique_Personale[i]
    # print(random_name, end="\n")
    query = (
        "INSERT INTO AddettiMarketing (ID,Ruolo) VALUES ('"
        + random_id
        + "','"
        + random_ruolo
        + "');"
    )

    f.write(query)
    f.write("\n")
# fine parte addetti marketing
f.write("---------------Fine Inserimento Addetti Marketing---------------\n")
f.write("---------------Inizio Inserimento Patente---------------\n")

patenti = "ABCDE"
unique_Patente = ["''"]
for i in range(2900):
    data = genRandomDate()
    random_numpatente = "".join(random.choice(ALL_SYMBOLS) for i in range(9))
    categoria = "".join(random.choice(patenti) for i in range(1))
    unique_Patente.append(random_numpatente)
    query = (
        "INSERT INTO Patente (NumeroPatente,DDS,Categoria) VALUES ('"
        + random_numpatente
        + "','"
        + str(data)
        + "','"
        + categoria
        + "');"
    )
    f.write(query)
    f.write("\n")

f.write("---------------Fine Inserimento Patente---------------\n")

f.write("---------------Inizio Inserimento Turni---------------\n")

unique_Turno = ["''"]
ora_inizio = ['9','10','11','14','15','16']
ora_fine = ['14','15','16','20','21','22']
for i in range(5):
    
    random_turno = "".join(random.choice(NUMBERS) for i in range(1))
    inizio = "".join(random.choice(ora_inizio))
    fine = "".join(random.choice(ora_fine))
    unique_Turno.append(random_turno)
    query = (
        "INSERT INTO Turni (ID_Turno,OrarioInizio,OrarioFine) VALUES ('"
        + random_turno
        + "','"
        + inizio
        + "','"
        + fine
        + "');"
    )
    f.write(query)
    f.write("\n")

f.write("---------------Fine Inserimento Turni---------------\n")

f.write("---------------Inizio Inserimento Autisti---------------\n")

unique_Autisti = ["''"]

for i in range(2901):
    random_id = unique_Personale[3000+i]
    random_patente = unique_Patente[i]
    random_Turno = random.choice(unique_Turno[1:])
    query = (
        "INSERT INTO Autisti (ID,NumeroPatente,Turno) VALUES ('"
        + random_id
        + "','"
        + random_patente
        + "','"
        + random_Turno
        + "');"
    )
    f.write(query)
    f.write("\n")

f.write("---------------Fine Inserimento Autisti---------------\n")

print("1.txt Done")
f.close()
