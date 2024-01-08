import random
from faker import Faker
import string
import decimal
import datetime

fake = Faker("it_IT")

#Funzione Rand.DDN
def genRandomDate():
    start_date = datetime.date(1975, 1, 1)
    end_date = datetime.date(2001, 12, 30)
    num_days = (end_date - start_date).days
    rand_days = random.randint(1, num_days)
    random_date = start_date + datetime.timedelta(days=rand_days)

    return random_date

#Funzione Rand.DA
def genRandomInsuranceDate():
    start_date = datetime.date(2023, 1, 1)
    end_date = datetime.date(2025, 1, 1)
    num_days = (end_date - start_date).days
    rand_days = random.randint(1, num_days)
    random_date = start_date + datetime.timedelta(days=rand_days)

    return random_date

#Funzione Rand.CD
def genRandomCardDate():
    start_date = datetime.date(2027, 1, 1)
    end_date = datetime.date(2034, 12, 30)
    num_days = (end_date - start_date).days
    rand_days = random.randint(1, num_days)
    random_date = start_date + datetime.timedelta(days=rand_days)

    return random_date

#Funzione Rand.PD
def genRandomLicenceDate():
    start_date = datetime.date(2025, 1, 1)
    end_date = datetime.date(2035, 12, 30)
    num_days = (end_date - start_date).days
    rand_days = random.randint(1, num_days)
    random_date = start_date + datetime.timedelta(days=rand_days)

    return random_date

#Funzione Rand.DDR
def genRandomRequestDate():
    start_date = datetime.date(2022, 1, 1)
    end_date = datetime.date(2023, 12, 30)
    num_days = (end_date - start_date).days
    rand_days = random.randint(1, num_days)
    random_date = start_date + datetime.timedelta(days=rand_days)

    return random_date

#Funzione Rand.Mail
def generateEmail(name, surname):
    
    domain = fake.domain_name()

    return f"{name}.{surname}@{domain}"

#Funzione Rand.T
def generateTarga():
    SYMBOLS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    NUMBERS = "0123456789"
    start = "".join(random.choice(SYMBOLS) for i in range(2))
    mezzo = "".join(random.choice(NUMBERS) for i in range(3))
    fine = "".join(random.choice(SYMBOLS) for i in range(2))

    return start+mezzo+fine

#Funzione Rand.PSW
def generatePsw():
    ALL = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    psw = "".join(random.choice(ALL) for i in range(9))
    return psw
#Funzione Rand.CN
def generateCardNumber():
    NUMBERS = "0123456789"
    number = "".join(random.choice(NUMBERS) for i in range(16))
    return number
#Funzione Rand.Star
def checkStelleUtenti(stelle):
    if stelle == 1:
        return 1
    elif stelle == 2:
        return 2
    elif stelle == 3:
        return 3
    elif stelle == 4:
        return 4
    elif stelle == 5:
        return 5

print("Inizio esecuzione...")

print("L'ORDINE DI ESECUZIONE DEI FILE È 1.txt,2.txt,etc...")

print("Inizio Creazione 1.txt")

SYMBOLS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
NUMBERS = "0123456789"
ALL_SYMBOLS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
f = open("1.txt", "w+")
print("--------------- Inizio Inserimento Personale\n")
random_id = ""
unique_Personale = ["''"]

values = []
for i in range(6000):
    data = genRandomDate()
    surname = fake.last_name()
    name = fake.first_name()
    email = str(generateEmail(name, surname))

    random_id = str(i)
    unique_Personale.append(random_id)
    
    query = "('" + random_id + "','"+ name+ "','"+ surname+ "','"+ str(data)+ "','"+ fake.phone_number()+ "','"+ email+ "')"
    values.append(query)
f.write(
    "INSERT INTO Personale (ID,Nome,Cognome,DDN,NumeroDiTelefono,Email) VALUES" + ",\n".join(values) + ";"
)    
f.write("\n")
print("--------------- Fine Inserimento Personale\n")
f.close()

print("1.txt Done")

print("Inizio Creazione 2.txt")

f = open("2.txt","w+")

print("--------------- Inizio Inserimento Addetti Marketing\n")

unique_AddMark = ["''"]

ruoli = ["Responsabile", "Analista", "Coordinatore"]
values_marketing = []
for i in range(3000):
   
    random_ruolo = random.choice(ruoli)
    random_id = unique_Personale[i]
    
    query = "('"+ random_id+ "','"+ random_ruolo+ "')"
    unique_AddMark.append(random_id)
    values_marketing.append(query)
f.write(
    "INSERT INTO AddettiMarketing (ID_Addetto,Ruolo) VALUES"+",\n".join(values_marketing)+";"
)
f.write("\n")

print("--------------- Fine Inserimento Addetti Marketing\n")
f.write("\n")
print("--------------- Inizio Inserimento Patente\n")

patenti = ["B","BE","B96"]
unique_Patente = ["''"]
values_patenti = []
for i in range(2900):
    data = genRandomLicenceDate()
    random_numpatente = "".join(random.choice(ALL_SYMBOLS) for i in range(9))
    categoria = "".join(random.choice(patenti) for i in range(1))
    unique_Patente.append(random_numpatente)
    
    query = "('"+ random_numpatente+ "','"+ str(data)+ "','"+ categoria+ "')"
    
    values_patenti.append(query)
f.write(
    "INSERT INTO Patente (NumeroPatente,DDS,Categoria) VALUES "+",\n".join(values_patenti)+";"
)
f.write("\n")
print("--------------- Fine Inserimento Patente\n")
f.write("\n")
print("--------------- Inizio Inserimento Turni\n")

unique_Turno = ["''"]
ora_inizio = ['9','10','11','14','15','16']
ora_fine = ['14','15','16','20','21','22']
values_turni = []
for i in range(5):
    
    random_turno = "".join(random.choice(NUMBERS) for i in range(1))
    inizio = "".join(random.choice(ora_inizio))
    fine = "".join(random.choice(ora_fine))
    unique_Turno.append(random_turno)
    query = "('"+ random_turno+ "','"+ inizio+ "','"+ fine+ "')"
    
    values_turni.append(query)
f.write(
    "INSERT INTO Turni (ID_Turno,OrarioInizio,OrarioFine) VALUES "+",\n".join(values_turni)+";"
)
f.write("\n")
print("--------------- Fine Inserimento Turni\n")
f.write("\n")
print("--------------- Inizio Inserimento Assicurazione\n")

unique_Assicurazione = ["''"]
values_assicurazione = []
tipo_assicurazione=["Kasko","Furto","Incendio","Base"]
for i in range(2901):
    random_id = str(i)
    data = genRandomInsuranceDate()
    tipo = random.choice(tipo_assicurazione)
    query = "('"+ str(random_id)+ "','"+ str(data)+ "','"+ str(tipo)+ "')"
    unique_Assicurazione.append(random_id)
    values_assicurazione.append(query)
f.write(
    "INSERT INTO Assicurazioni (ID_Assicurazione,DataScadenza,Tipo) VALUES "+",\n".join(values_assicurazione)+";"
)
f.write("\n")
print("--------------- Fine Inserimento Assicurazione\n")
f.write("\n")
print("--------------- Inizio Inserimento Veicoli\n")
unique_Veicolo = ["''"]
values_veicolo = []
l_marca = ["Fiat","BMW","Audi","Range Rover","Seat"]
l_modello = ["Punto","Panda","Q8","RS7"]
for i in range(2901):
    random_targa = generateTarga()
    random_assicurazione = unique_Assicurazione[i]
    query = "('"+ str(random_targa)+ "','"+ str(random.choice(l_marca))+ "','"+ str(random.choice(l_modello))+ "','"+str(random.randint(1,12))+"','"+str(random_assicurazione)+"')"
    unique_Veicolo.append(random_targa)
    values_veicolo.append(query)

f.write(
    "INSERT INTO Veicoli (Targa,Marca,Modello,PostiDisponibili,ID_Assicurazione) VALUES "+",\n".join(values_veicolo)+";"
)
f.write("\n")
print("--------------- Fine Inserimento Veicoli\n")
f.write("\n")
print("--------------- Inizio Inserimento Autisti\n")

unique_Autisti = ["''"]
values_autisti = []
stipendio = ["1200","1500","1350"]
for i in range(2901):
    random_id = unique_Personale[3000+i]
    random_patente = unique_Patente[i]
    random_Turno = random.choice(unique_Turno[1:])
    random_targa = random.choice(unique_Veicolo)
    query = "('"+ random_id+ "','"+ random_patente+ "','"+ random_Turno+ "','"+random_targa+"','"+random.choice(stipendio)+"')"
    unique_Autisti.append(random_id)
    values_autisti.append(query)
f.write(
    "INSERT INTO Autisti (ID_Autista,NumeroPatente,Turno,Targa,Stipendio) VALUES "+",\n".join(values_autisti)+";"
)
f.write("\n")
print("--------------- Fine Inserimento Autisti\n")
f.write("\n")
print("--------------- Inizio Inserimento Manutentori\n")

unique_Manutentori = ["''"]
values_manutentori = []
qualifica = ["Gommista","Elettrauto","Meccanico","Carrozziere"]
for i in range(100):
    random_id = unique_Personale[5900+i]
    
    query = "('"+ random_id+ "','"+ random.choice(qualifica)+ "')"
    unique_Manutentori.append(random_id)
    values_manutentori.append(query)
f.write(
    "INSERT INTO Manutentori (ID_Manutentore,Qualifica) VALUES "+",\n".join(values_manutentori)+";"
)
f.write("\n")
print("--------------- Fine Inserimento Manutentori\n")
f.write("\n")
print("--------------- Inizio Inserimento ContattaPerGuasto\n")

unique_Contatto = ["''"]
values_contatto = []
motivi = ["Gomma Bucata","Spia dell motore accesa","Radiatore bucato","Batteria scarica"]
for i in range(100):
    random_manutentore = random.choice(unique_Manutentori)
    random_autista = random.choice(unique_Autisti)

    query = "('"+ random_manutentore+ "','"+ random_autista+ "','"+random.choice(motivi)+"')"
    unique_Contatto.append((random_manutentore,random_autista))
    values_contatto.append(query)
f.write(
    "INSERT INTO ContattaPerGuasto (ID_Manutentore,ID_Autista,Motivo) VALUES "+",\n".join(values_contatto)+";"
)
f.write("\n")
print("--------------- Fine Inserimento ContattaPerGuasto\n")

print("2.txt Done")
f.close()

print("Inizio Creazione 3.txt")
f = open("3.txt","w+")

f.write("--------------- Inizio Inserimento Offerte\n")
unique_Offerta = ["''"]
offerta = ["Sconto 10%","Sconto 15%","Sconto 20%","Credito 5€","Credito 10€"]
values_offerta = []
for i in range(15):
    random_id = str(i)
    promo = "".join(str(random.randint(1,9)) for i in range(6))
    random_addetto = random.choice(unique_AddMark)
    query = "('"+ random_id+ "','"+ promo+ "','"+ random.choice(offerta)+ "','"+random_addetto+"')"
    unique_Offerta.append(random_id)
    values_offerta.append(query)
f.write(
    "INSERT INTO Offerta (ID_Offerta,PromoCode,InfoOfferta,ID_Addetto) VALUES "+",\n".join(values_offerta)+";"
)
f.write("\n")
print("--------------- Fine Inserimento Offerte\n")
f.write("\n")
print("--------------- Inizio Inserimento Utenti\n")

unique_Utenti = ["''"]
values_utenti = []
abbonamento = ["Trimestrale","Semestrale","Annuale"]
for i in range(10000):
    random_id = str(i)
    surname = fake.last_name()
    name = fake.first_name()
    email = str(generateEmail(name, surname))
    psw = generatePsw()
    id_off = random.choice(unique_Offerta)
    query = "('"+ random_id+ "','"+ name+ "','"+ surname+ "','"+email+"','"+psw+"','"+id_off+"','"+random.choice(abbonamento)+"')"
    unique_Utenti.append(random_id)
    values_utenti.append(query)
f.write(
    "INSERT INTO Utenti (ID_Utente,Nome,Cognome,Email,Password,ID_Offerta,Abbonamento) VALUES "+",\n".join(values_utenti)+";"
)
f.write("\n")
print("--------------- Fine Inserimento Utenti\n")
f.write("\n")
print("--------------- Inizio Inserimento Carte\n")

unique_Carta = ["''"]
values_carta = []

utente_carta = []
for i in range(10000):
    
    numero_Carta = str(random.randint(4,5))+"".join(str(random.randint(0,9)) for i in range(3))+" "+"".join(str(random.randint(0,9)) for i in range(4))+" "+"".join(str(random.randint(0,9)) for i in range(4))+" "+"".join(str(random.randint(0,9)) for i in range(4))
    data_scadenza = genRandomCardDate()
    cvv = "".join(str(random.randint(0,9)) for i in range(3))
    utente = unique_Utenti[i]
    query = "('"+ numero_Carta+ "','"+ str(data_scadenza)+ "','"+ cvv+ "','"+utente+"')"
    unique_Carta.append(numero_Carta)
    values_carta.append(query)
    
    utente_carta.append((utente,numero_Carta))
f.write(
    "INSERT INTO Carta (NumeroCarta,DataScandenza,CVV,ID_Utente) VALUES "+",\n".join(values_carta)+";"
)
print("--------------- Fine Inserimento Carte\n")

print(utente_carta)

print("3.txt Done")
f.close()
print("Inizio creazione 4.txt")
f = open("4.txt","w+")

print("--------------- Inizio Inserimento RichiestaPrenotazioni\n")

unique_RichPren = ["''"]
values_ricpren = []
raccolta = ["Anagnina","Termini","Centocelle","Eur","Tor Vergata","Colosseo"]
rilascio = ["Finocchio","Garbatella","Ostia","San Lorenzo","Primavalle","San Basilio"]
date = []
ora = ['9','10','11','14','15','16','20','21','22']
id_carta_utente = []
for i in range(10000):
    random_id = str(i)
    passeggeri = str(random.randint(1,12))
    
    utente = utente_carta[i][0]
    
    autista = random.choice(unique_Autisti)
    data = genRandomRequestDate()
    orario = random.choice(ora)
    query = "('"+ random_id+ "','"+ str(random.choice(raccolta))+ "','"+ str(random.choice(rilascio))+ "','"+str(data)+"','"+str(orario)+"','"+str(passeggeri)+"','"+str(utente)+"','"+str(autista)+"')"
    unique_RichPren.append(random_id)
    values_ricpren.append(query)
    date.append(data)
f.write(
    "INSERT INTO RichiestePrenotazioni (ID_Richiesta,PuntoDiRaccolta,PuntoDiRilascio,DataRichiesta,OrarioRichiesta,NumeroPasseggeri,ID_Utente,ID_Autista) VALUES "+",\n".join(values_ricpren)+";"
)
f.write("\n")
print("--------------- Fine Inserimento RichiestaPrenotazioni\n")
f.write("\n")
print("--------------- Inizio Inserimento TratteCompletate\n")

unique_TrattaC = ["''"]
values_trattac = []
costo = ["25€","65€","115€","35€","50€"]
for i in range(7000):
    random_id = unique_RichPren[i]
    costi = random.choice(costo)
    
    numcarta = utente_carta[i][1]
    query = "('"+ random_id+ "','"+ str(costi)+ "','"+ str(numcarta)+ "')"
    unique_TrattaC.append(random_id)
    values_trattac.append(query)
f.write(
    "INSERT INTO TratteCompletate (ID_TrattaC,Costo,NumeroCarta) VALUES "+",\n".join(values_trattac)+";"
)
f.write("\n")
print("--------------- Fine Inserimento TratteCompletate\n")
f.write("\n")
print("--------------- Inizio Inserimento Feedback\n")

unique_Feed = ["''"]
values_feed = []
feedback_utente = {
                    1: "Non lo prenderò mai più!",
                    2: "Non mi è piaciuto lo stile di guida",
                    3: "Nulla di particolare",
                    4: "Veicolo molto pulito e comodo.",
                    5: "Autista veramente cordiale",
                   }

feedback_autisti = {
                    1: "Utente scortese!",
                    2: "Utente ritardatario",
                    3: "Nulla di particolare",
                    4: "Utente rispettoso.",
                    5: "Utente veramente genuino",
                   }

for i in range(7000):
    random_id = str(i)
    
    stelle_random_ut = random.choice(list(feedback_utente.keys()))
    
    commento_ut = str(feedback_utente[stelle_random_ut])

    
    stelle_random_aut = checkStelleUtenti(stelle_random_ut)
    
    commento_aut = str(feedback_autisti[stelle_random_aut])
    random_trattac = random.choice(unique_TrattaC)
    query = "('"+ random_id+ "','"+ str(stelle_random_ut)+ "','"+ str(commento_ut)+ "','"+str(stelle_random_aut)+"','"+str(commento_aut)+"','"+str(date[i])+"','"+str(random_trattac)+"')"

    unique_Feed.append(random_id)
    values_feed.append(query)

f.write(
    "INSERT INTO Feedback (ID_Feedback,StelleUtente,CommentoUtente,StelleAutista,CommentoAutista,Data,ID_TrattaCompletata) VALUES "+",\n".join(values_feed)+";"
)
f.write("\n")
print("--------------- Fine Inserimento Feedback\n")
f.write("\n")
print("--------------- Inizio Inserimento TratteRifiutate\n")

unique_TrattaR = ["''"]
values_trattar = []
motivi = ["Problema generale","Indisponibilità al servizio","Troppo lontano"]
for i in range(3000):
    random_id = unique_RichPren[7000+i]
    motivo = random.choice(motivi)
    query = "('"+ random_id+ "','"+ str(motivo)+ "')"
    unique_TrattaR.append(random_id)
    values_trattar.append(query)
f.write(
    "INSERT INTO TratteRifiutate (ID_TrattaR,Motivazione) VALUES "+",\n".join(values_trattar)+";"
)
f.write("\n")
print("--------------- Fine Inserimento TratteRifiutate\n")
print("4.txt Done")
f.close()
