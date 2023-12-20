
# Indice degli argomenti

- Componenti
- Motivazioni
- Obiettivi
- Raccolta dei dati
- Schemi

# Progetto VRoomA
## Componenti del gruppo  

| Nome | Cognome | Matricola | Mail |
| -------- | -------- | --------- | ------------------------------------- |
| Leonardo | Ascenzi | 0310858 | leonardo.ascenzi@students.uniroma2.eu |
| Franco | Salvucci | 0306604 | franco.salvucci@students.uniroma2.eu |
| Nicolò | Spadoni | 0311175 | nicolo.spadoni@students.uniroma2.eu | | | | |
## Motivazioni

Il database che stiamo realizzando è incentrato all'implementazione di un software dedicato all'organizzazione di viaggi tramite taxi.
## Obiettivi

L'obiettivo principale di questo sistema è permettere agli utenti di organizzare gli spostamenti tramite taxi a seconda delle proprie esigenze, del tipo di veicolo scelto e del costo della tratta scelta.

Da un punto di vista societario, gli obiettivi sono quelli di valutare la qualità del lavoro degli autisti tramite i feedback forniti dai clienti e migliorare dove possibile il servizio.

## Raccolta dei dati

### Analisi dei requisiti

I **ruoli aziendali** sono i seguenti:
- Addetti Marketing
- Autisti
- Manutentori

Gli **addetti al marketing** possono inserire, previa autorizzazione da parte degli amministratori della società, delle **promo** che prevedono sconti sulle corse per gli utenti del sistema.

Gli **autisti** potranno scegliere se accettare o rifiutare la corsa, specificando in questo caso la motivazione del rifiuto.
Inoltre potranno lasciare un **feedback** all'utente riguardo il comportamento prima e durante la corsa.
Ogni **autista** ha la propria macchina privata, e può contattare i manutentori aziendali in caso di guasto del veicolo.
Ad ogni **autista** sono assegnati uno o più **turni** di lavoro, con il vincolo che il singolo autista non può essere assegnato a due turni lavorativi che hanno orario inizio e orario fine uguali.

I **manutentori** possono ricevere richieste di assistenza da parte degli autisti e contattare le officine convenzionate per effettuare il lavoro di assistenza.
Le **officine** non fanno parte della società.

Le tipologie di **veicolo** disponibili sono le seguenti:
- Base: 4 posti disponibili
- Plus: 7 posti disponibili, adibito a trasporto di carrozzine per disabili
- Premium: 12 posti disponibili, adibito a trasporto di carrozzine per disabili

Ogni **veicolo**, identificato in modo univoco dalla targa, per poter circolare, deve essere assicurato.

Quando si prenota una **corsa** (**tratta**) si possono scegliere due punti:
- Punto di Partenza, identificato come Punto di raccolta
- Punto di Arrivo, identificato come Punto di rilascio

Ogni **prenotazione** può essere accettata o rifiutata in base a determinate esigenze dell'**utente** (Es: prenotazione effettuata per errore) e dell'**autista** (Es: indisponibilità al servizio).
Ad ogni tratta completata è associato un feedback che può essere lasciato sia dall'**utente** che dall'**autista**.

Ogni **utente** ha diritto a ricevere **offerte** da poter usare al momento della prenotazione.
Può effettuare illimitate richieste di **prenotazione**, in base alle necessità personali (numero di passeggeri, persone con disabilità, punto di ritiro, punto di rilascio), con il vincolo di una corsa per volta.
A corsa completata l'**utente** può lasciare un **feedback** con un numero di stelle (da 1 a 5) e un commento.
Ogni **utente** deve aggiungere una **carta** con cui effettuare il pagamento relativo alla tratta effettuata, in un secondo momento potrà aggiungere altri metodi di pagamento secondo le proprie esigenze.
Ogni **utente** può aggiungere alla lista dei preferiti ua qualunque delle tratte effettuate da lui, scegliendo se aggiungere solo la tratta o anche l'autista.
Ogni **utente** può accedere alla cronologia delle prenotazioni effettuate.

### Glossario delle entità


| Entità | Descrizione | Attributi | Relazioni Coinvolte |
| ---------------------- | ----------------------------------------------------------------- | ------------------------- | --------------------------------------------------------------------------------- |
| Personale | Membri totali della società | **ID**, Nome, Cognome, DDN, Numero di Telefono, Email | Addetti Marketing, Manutentori, Autisti |
| Patente | Descrive tutte le info riguardanti la patente degli autisti | **Numero Patente**, DDS, Categoria | Autisti |
| Offerte | Serie di offerte che vengono proposte al singolo utente | **ID**, Promo Code, Info Offerta, | Utenti, Addetti Marketing |
| Manutentori | Addetti alla manutenzione delle auto degli autisti | **ID**, Qualifica | Personale, Autisti |
| Autisti | Personale che svolge il ruolo di autista delle auto nella società | **ID**, Stipendio | Patente, Manutentori, Veicoli, Turni, Richiesta Prenotazione, Personale, Feedback |
| Veicoli | Auto utilizzate per il servizio di taxi | **Targa**, Marca, Modello, Posti disponibili | Autisti, Assicurazione |
| Turni | Turni lavorativi che riguardano gli autisti | **ID**, Orario inizio, Orario fine | Autisti |
| Richiesta Prenotazione | Richieste di prenotazioni effettuate da parte dall'utente | **ID**, Punto di raccolta, Punto di rilascio, Orario richiesta, Numero Passeggeri | Autisti, Utenti, Tratte Complete, Tratte Rifiutate |
| Utenti | Utenti utilizzatori del servizio taxi | **ID**, Nome, Cognome, Email, Password, Abbonamento | Carta, Richiesta Prenotazione, Offerte, Feedback, Tratte completate |
| Feedback | Recensioni lasciate dall'utente e dagli autisti | **ID**, Stelle, Commento, Data | Tratte Completate, Utenti, Autisti |
| Tratte Completate | Corse effettuate portate a termine con successo | **ID**, Costo | Richiesta Prenotazione, Feedback, Carta, Utenti |
| Tratte Rifiutate | Corse rifiutate da parte dell'autista per determinati motivi | **ID**, Motivazione | Richiesta Prenotazione |
| Carta | Carta di credito personale dell'utente | **Numero Carta**, Data di Scadenza, CVV | Utenti, Tratte completate |
| Assicurazione | Dati dell'assicurazione associata al singolo veicolo | **ID**, Data di scandenza, Tipo | Veicoli |
| Addetti Marketing | Personale addetto al reparto marketing della società | **ID**, Ruolo | Offerte, Personale |

### Glossario dei termini

| Entità | Descrizione | Sinonimi | 
| ---------------------- | ----------------------------------------------------------------- | ------------------------- | 
| Personale | Membri totali della società | Organigramma |  
| Patente | Descrive tutte le info riguardanti la patente degli autisti | Licenza di Guida |  |
| Offerte | Serie di offerte che vengono proposte al singolo utente | Promozioni |  |
| Manutentori | Addetti alla manutenzione delle auto degli autisti | Meccanici, Operai |  |
| Autisti | Personale che svolge il ruolo di autista delle auto nella società | Driver |   |
| Veicoli | Auto utilizzate per il servizio di taxi | Automobili |  |
| Turni | Turni lavorativi che riguardano gli autisti | Orario Lavorativo |  |
| Richiesta Prenotazione | Richieste di prenotazioni effettuate da parte dall'utente | Prenotazioni |  |
| Utenti | Utenti utilizzatori del servizio taxi | Persone |  |
| Feedback | Recensioni lasciate dall'utente e dagli autisti | Recensioni |  |
| Tratte Completate | Corse effettuate portate a termine con successo | Corse |  |
| Tratte Rifiutate | Corse rifiutate da parte dell'autista per determinati motivi | Corse Annullate |  |
| Carta | Carta di credito personale dell'utente | Metodo di pagamento |  |
| Assicurazione | Dati dell'assicurazione associata al singolo veicolo | RCA, Polizza assicurativa |  |
| Addetti Marketing | Personale addetto al reparto marketing della società | Advertiser |  |

### Glossario delle relazioni

| Relazione                    | Descrizione                                                                                                                                     | Entità                                      |
| ---------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------- |
| VeicoloPossiedeAssicurazione | Relazione che dice che ogni veicolo ha una propria assicurazione                                                                                | Veicoli (1,1), Assicurazione (1,1)          |
| AutistaGuidaVeicolo          | Relazione che dice che ogni autista guida la propria autovettura                                                                                | Autisti (1,1), Veicoli (1,1)                |
| AutistaPossiedePatente       | Relazione che dice che ogni autista, per poter guidare, necessita di una patente                                                                | Autisti (1,1), Patente (1,1)                |
| ContattaPerGuasto            | Relazione che dice che ogni autista può (non necessariamente) contattare un manutentore per un guasto al veicolo                                | Autisti (0,N), Manutentori (0,N)            |
| AutistaLasciaFeedback        | Relazione che dice che ogni autista può lasciare uno o più feedback relativio a tutti gli aspetti della corsa effettuata                        | Autisti (1,N), Feedback (1,1)               |
| AssegantoA                   | Relazione che dice che ogni autista viene assegnato ad una richiesta di prenotazione, in base a determinate circostanze                         | Autisti (1,1), Richiesta Prenotazione (1,1) |
| AggiungeOfferta              | Relazione che dice che un addetto marketing può aggiungere una o più offerte per gli utenti                                                     | Addetti Marketing (1,N), Offerte (1,1)      |
| UtenteHaOfferta              | Relazione che dice che ogni utente può avere (non necessariamente) una o più offerte attive                                                     | Utenti (1,1), Offerte (1,N)                 |
| UtentePossiedeCarta          | Relazione che dice che ogni utente deve possedere almeno una carta con cui effettuare i pagamenti                                               | Utenti (1,N), Carta (1,1)                   |
| EffettuaPrenotazione         | Relazione che dice che ogni utente effettua una o più prenotazioni                                                                              | Utenti (1,N), Richiesta Prenotazioni (1,1)  |
| UtenteLasciaFeedback         | Relazione che dice che ogni utente può lasciare uno o più feedback relativi alle corse da lui effettuate                                        | Utenti (1,N), Feedback (1,1)                |
| CartaPagaTratta              | Relazione che dice che ogni utente, tramite la propria carta, deve pagare le tratte da lui effettuate                                           | Carta (1,N), Tratte Completate (1,1)        |
| TrattaAvereFeedback          | Relazione che dice che ogni tratta completata può avere (non necessariamente) un solo feedback, che viene lasciato dagli utenti e dagli autisti | Tratte Completate (0,1), Feedback (1,1)     |
|  AutistaAvereTurni | Ogni autista ha un proprio turno lavorativo, ad ogni turno lavorativo vengono assegnati uno o più autisti | Autisti (1,1), Turni (1,N) |                                                                                                                                                                              |                                             |

## Schemi

### Schemi di relazione

Le chiave primarie sono identificate in **grassetto**, mentre le chiavi secondarie (o esterne) sono scritte in stile _Italic_

- Personale (**ID_Personale**, Nome, Cognome, NumeroTelefono, Email)
- Autisti (**ID_Autista**, Stipendio, _NumeroPatente_, _Targa_, _ID_Turno)
- Manutentori (**ID_Manutentore**, Qualifica)
- Addetti Marketing (**ID_Addetto**, Ruolo)
- ContattaPerGuasto (_ID_Manutentore_, _ID_Autista_)
- Patente (**NumeroPatente**, DDS, Categoria)
- Turni (**ID_Turno**, OrarioInizio, OrarioFine)
- Veicoli (**Targa**, Marca, Modello, PostiDisponibili, _ID_Assicurazione_)
- Assicurazione (**ID_Assicurazione**, DataDiScadenza, Tipo)
- Offerte (**ID_Offerta**, PromoCode, InfoOfferta, _ID_Addetto_)
- Utenti (**ID_Utente**, Nome, Cognome, Email, Abbonamento, PSW, _ID_Offerta_)
- Carta (**NumeroCarta**, DataScadenza, CVV, _ID_Utente_)
- Richiesta Prenotazione (**ID_Richiesta**, OrarioRichiesta, NumeroPasseggeri, PuntoRaccolta, PuntoRilascio, _ID_Utente_, _ID_Autista_)
- Tratte Complete (**ID_Tratta**, Costo, _NumeroCarta_)
- Tratte Rifiutate (**ID_Tratta**, Motivazione)
- Feedback (**ID_Feedback**, Stelle, Commento, Data, _ID_Tratta_)
### Schema Logico

![[Schema-Logico.jpg|center]]

#### Normalizzazione

Di seguito si discutono le forme normali dello schema logico:

- **1NF**: tutti gli schemi di relazione nello schema logico sopra riportato sono in **1NF**, poiché tutti gli attributi sono semplici, ovvero contengono soltanto valori atomici indivisibili.
- **2NF**: tutti gli schemi di relazione dello schema logico sono anche già in **2NF**, poiché sono già in **1NF** e nessun attributo presenta alcuna dipendenza parziale. Tutti gli attributi dipendono funzionalmente solo dalla chiave primaria della stessa tabella.
- **3NF**: tutti gli schemi di relazione sono anche in **3NF** perché già in **2NF**, ed inoltre, tutti gli attributi delle tabelle dipendono funzionalmente e direttamente dalla chiave primaria, senza transitività.
### Schema Fisico

Abbiamo distinto le frecce che vanno dalle entità figlie a quelle padre mettendole in blu. 

Nelle entità, le chiavi secondarie sono indentificate con il pallino grigio, mentre quelle primarie sono identificate con il pallino nero.

![[Schema-Fisico.jpg|center]]

#### Generalizzazione

Una generalizzazione rappresenta un legame logico tra un’entità genitore e una o più entità figlie, in questo caso le entità genitore sono “Personale” e "Richiesta Prenotazione", ognuna con le rispettive entità figlie, che sono:

1) **Personale**
	1) Autisti
	2) Addetti Marketing
	3) Manutentori
2) **Richiesta prenotazione**
	1) Tratte completate
	2) Tratte rifiutate


Abbiamo tre metodi per rappresentare una generalizzazione a livello fisico:

- Accorpamento del padre nelle entità figlie
- Accorpamento delle entità figlie nel padre
- Sostituzione della generalizzazione con relazioni

Tra questi metodi abbiamo scelto il terzo in quanto da noi considerato il più adeguato. Infatti, il primo metodo avrebbe portato ad una ridondanza di relazioni. 

Il secondo metodo necessita dell’aggiunta di un attributo nelle entità "Personale" e "Richiesta Prenotazioni", con il compito di specificare il ruolo del lavoratore (Es. Autisti = 1, Manutentori = 2, etc..), e il tipo di prenotazione (Es. Completata = 1 e Rifiutata = 2), in più si sarebbe dovuto scegliere se perdere informazioni (attributi) dei figli o inserire le informazioni nel padre, quindi aggiungere attributi dei figli al padre. La seconda scelta avrebbe portato ad una quantità non indifferente di valori NULL. 

### Implementazione Database - MySQL
#### Creazione delle tabelle

```SQL
CREATE TABLE Personale(
	ID int not null ,
	Nome varchar(50) not null,
	Cognome varchar(50) not null,
	DDN date not null,
	NumeroDiTelefono int not null,
	Email varchar(255),
	PRIMARY KEY (ID)
);

CREATE TABLE AddettiMarketing (
	ID_Addetto int not null,
	Ruolo varchar(50),
	PRIMARY KEY (ID_Addetto),
	FOREIGN KEY (ID_Addetto) REFERENCES Personale(ID)
);

CREATE TABLE Patente (
	NumeroPatente varchar(255) not null,
	DDS date not null,
	Categoria varchar(50),
	PRIMARY KEY (NumeroPatente)
);

CREATE TABLE Offerte (
	ID_Offerta int not null ,
	PromoCode int not null,
	InfoOfferta varchar(50) not null,
	ID_Addetto int not null,
	PRIMARY KEY (ID_Offerta),
	FOREIGN KEY (ID_Addetto) REFERENCES AddettiMarketing(ID_Addetto)
);

CREATE TABLE Manutentori (
	ID_Manutentore int not null ,
	Qualifica varchar(50) not null,
	PRIMARY KEY (ID_Manutentore),
	FOREIGN KEY (ID_Manutentore) REFERENCES Personale (ID)
);

CREATE TABLE Assicurazione (
	ID_Assicurazione int not null,
	DataScadenza date not null,
	Tipo varchar(50) not null,
	PRIMARY KEY (ID_Assicurazione)
);

CREATE TABLE Veicoli (
	Targa varchar(50) not null,
	Marca varchar(50) not null,
	Modello varchar(50) not null,
	PostiDisponibili int not null,
	Assicurazione int not null,
	PRIMARY KEY (Targa),
	FOREIGN KEY (Assicurazione) REFERENCES Assicurazione(ID_Assicurazione)
);

CREATE TABLE Turni (
	ID_Turno int not null ,
	OrarioInizio int not null,
	OrarioFine int not null,
	PRIMARY KEY (ID_Turno)
);

CREATE TABLE Autisti (
	ID_Autista int not null ,
	NumeroPatente varchar(255) not null,
	Turno int not null,
	Targa varchar(50) not null,
	Stipendio int not null,
	PRIMARY KEY (ID_Autista),
	FOREIGN KEY (ID_Autista) REFERENCES Personale (ID),
	FOREIGN KEY (NumeroPatente) REFERENCES Patente(NumeroPatente),
	FOREIGN KEY (Turno) REFERENCES Turni(ID_Turno),
	FOREIGN KEY (Targa) REFERENCES Veicoli(Targa)
);

CREATE TABLE Utenti (
	ID_Utente int not null ,
	Nome varchar(50) not null,
	Cognome varchar(50) not null,
	Email varchar(255) not null,
	Password varchar(255) not null,
	ID_Offerta int not null,
	Abbonamento varchar(50) not null,
	PRIMARY KEY (ID_Utente),
	FOREIGN KEY (ID_Offerta) REFERENCES Offerte (ID_Offerta)
);

CREATE TABLE RichiestePrenotazioni (
	ID_Richiesta int not null ,
	PuntoDiRaccolta varchar(50) not null,
	PuntoDiRilascio varchar(50) not null,
	DataRichiesta date not null,
	OrarioRichiesta varchar(50) not null,
	NumeroPasseggeri int not null,
	ID_Utente int not null,
	ID_Autista int not null,
	PRIMARY KEY (ID_Richiesta),
	FOREIGN KEY (ID_Utente) REFERENCES Utenti(ID_Utente),
	FOREIGN KEY (ID_Autista) REFERENCES Autisti(ID_Autista)
);

CREATE TABLE Carta (
	NumeroCarta varchar(50) not null,
	DataScadenza date not null,
	CVV int not null,
	ID_Utente int not null,
	PRIMARY KEY (NumeroCarta),
	FOREIGN KEY (ID_Utente) REFERENCES Utenti(ID_Utente)
);

CREATE TABLE TratteCompletate (
	ID_TrattaC int not null ,
	Costo int not null,
	NumeroCarta varchar(50) not null,
	PRIMARY KEY (ID_TrattaC),
	FOREIGN KEY (ID_TrattaC) REFERENCES RichiestePrenotazioni (ID_Richiesta),
	FOREIGN KEY (NumeroCarta) REFERENCES Carta (NumeroCarta)
);

CREATE TABLE Feedback (
	ID_Feedback int not null ,
	StelleUtente int not null,
	CommentoUtente varchar(255) not null,
	StelleAutista int not null,
	CommentoAutista varchar(255) not null,
	Data date not null,
	ID_TrattaCompletata int not null,
	PRIMARY KEY (ID_Feedback),
	FOREIGN KEY (ID_TrattaCompletata) REFERENCES TratteCompletate (ID_TrattaC)
);

CREATE TABLE TratteRifiutate (
	ID_TrattaR int not null ,
	Motivazione varchar(255) not null,
	PRIMARY KEY (ID_TrattaR),
	FOREIGN KEY (ID_TrattaR) REFERENCES RichiestePrenotazioni (ID_Richiesta)
);

CREATE TABLE ContattaPerGuasto (
	ID_Manutentore int not null,
	ID_Autista int not null,
	Motivo varchar(255) not null,
	FOREIGN KEY (ID_Manutentore) REFERENCES Manutentori (ID_Manutentore),
	FOREIGN KEY (ID_Autista) REFERENCES Autisti (ID_Autista)
);
```

#### Inserimenti Manuali

```SQL
INSERT INTO Personale (ID,Nome,Cognome,DDN,NumeroTelefono,Email) VALUES ();
```

