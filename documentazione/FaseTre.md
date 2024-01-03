
# Indice degli argomenti

- Componenti
- Motivazioni
- Obiettivi
- Raccolta dei dati
- Schemi

# Progetto VRoomA
## Componenti del gruppo

| Nome | Cognome | Matricola | Mail |
| ---- | ---- | ---- | ---- |
| Leonardo | Ascenzi | 0310858 | leonardo.ascenzi@students.uniroma2.eu |
| Franco | Salvucci | 0306604 | franco.salvucci@students.uniroma2.eu |
| Nicolò | Spadoni | 0311175 | nicolo.spadoni@students.uniroma2.eu |
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
| ---- | ---- | ---- |
| Personale | Membri totali della società | Organigramma |
| Patente | Descrive tutte le info riguardanti la patente degli autisti | Licenza di Guida |
| Offerte | Serie di offerte che vengono proposte al singolo utente | Promozioni |
| Manutentori | Addetti alla manutenzione delle auto degli autisti | Meccanici, Operai |
| Autisti | Personale che svolge il ruolo di autista delle auto nella società | Driver |
| Veicoli | Auto utilizzate per il servizio di taxi | Automobili |
| Turni | Turni lavorativi che riguardano gli autisti | Orario Lavorativo |
| Richiesta Prenotazione | Richieste di prenotazioni effettuate da parte dall'utente | Prenotazioni |
| Utenti | Utenti utilizzatori del servizio taxi | Persone |
| Feedback | Recensioni lasciate dall'utente e dagli autisti | Recensioni |
| Tratte Completate | Corse effettuate portate a termine con successo | Corse |
| Tratte Rifiutate | Corse rifiutate da parte dell'autista per determinati motivi | Corse Annullate |
| Carta | Carta di credito personale dell'utente | Metodo di pagamento |
| Assicurazione | Dati dell'assicurazione associata al singolo veicolo | RCA, Polizza assicurativa |
| Addetti Marketing | Personale addetto al reparto marketing della società | Advertiser |

### Glossario delle relazioni

| Relazione | Descrizione | Entità |
| ---- | ---- | ---- |
| VeicoloPossiedeAssicurazione | Relazione che dice che ogni veicolo ha una propria assicurazione | Veicoli (1,1), Assicurazione (1,1) |
| AutistaGuidaVeicolo | Relazione che dice che ogni autista guida la propria autovettura | Autisti (1,1), Veicoli (1,1) |
| AutistaPossiedePatente | Relazione che dice che ogni autista, per poter guidare, necessita di una patente | Autisti (1,1), Patente (1,1) |
| ContattaPerGuasto | Relazione che dice che ogni autista può (non necessariamente) contattare un manutentore per un guasto al veicolo | Autisti (0,N), Manutentori (0,N) |
| AutistaLasciaFeedback | Relazione che dice che ogni autista può lasciare uno o più feedback relativio a tutti gli aspetti della corsa effettuata | Autisti (1,N), Feedback (1,1) |
| AssegantoA | Relazione che dice che ogni autista viene assegnato ad una richiesta di prenotazione, in base a determinate circostanze | Autisti (1,1), Richiesta Prenotazione (1,1) |
| AggiungeOfferta | Relazione che dice che un addetto marketing può aggiungere una o più offerte per gli utenti | Addetti Marketing (1,N), Offerte (1,1) |
| UtenteHaOfferta | Relazione che dice che ogni utente può avere (non necessariamente) una o più offerte attive | Utenti (1,1), Offerte (1,N) |
| UtentePossiedeCarta | Relazione che dice che ogni utente deve possedere almeno una carta con cui effettuare i pagamenti | Utenti (1,N), Carta (1,1) |
| EffettuaPrenotazione | Relazione che dice che ogni utente effettua una o più prenotazioni | Utenti (1,N), Richiesta Prenotazioni (1,1) |
| UtenteLasciaFeedback | Relazione che dice che ogni utente può lasciare uno o più feedback relativi alle corse da lui effettuate | Utenti (1,N), Feedback (1,1) |
| CartaPagaTratta | Relazione che dice che ogni utente, tramite la propria carta, deve pagare le tratte da lui effettuate | Carta (1,N), Tratte Completate (1,1) |
| TrattaAvereFeedback | Relazione che dice che ogni tratta completata può avere (non necessariamente) un solo feedback, che viene lasciato dagli utenti e dagli autisti | Tratte Completate (0,1), Feedback (1,1) |
| AutistaAvereTurni | Ogni autista ha un proprio turno lavorativo, ad ogni turno lavorativo vengono assegnati uno o più autisti | Autisti (1,1), Turni (1,N) |

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

## Implementazione Database - MySQL
### Creazione delle tabelle

```SQL
CREATE TABLE Personale(
	ID int not null ,
	Nome varchar(50) not null,
	Cognome varchar(50) not null,
	DDN date not null,
	NumeroDiTelefono varchar(50) not null,
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
	NumeroPatente varchar(50) not null,
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
	NumeroPatente varchar(50) not null,
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

### Triggers

Abbiamo implementato dei triggers nel nostro sistema, per far rispettare i vincoli scritti sopra
(i.e. Un utente **NON** può prenotare più di una corsa nello stesso momento,etc...)

I triggers sono i seguenti

**Controlla Orario Richiesta**

```SQL
CREATE TRIGGER `ControllaOrarioRichiesta` BEFORE INSERT ON `RichiestePrenotazioni` FOR EACH ROW BEGIN

-- Controlla se l'orario richiesto esiste già nella tabella
	IF EXISTS (
		SELECT 1
		FROM RichiestePrenotazioni
		WHERE OrarioRichiesta = NEW.OrarioRichiesta AND ID_Utente = NEW.ID_Utente
	) THEN
	
	-- Se l'orario esiste già, interrompi l'inserimento
		SIGNAL SQLSTATE '45000'
		SET MESSAGE_TEXT = '[ERRORE],OGNI UTENTE NON PUÒ PRENOTARE PIÙ DI UNA CORSA NELLO STESSO ORARIO';
	END IF;

END
```

**Controlla Turno Lavorativo**

```SQL
CREATE TRIGGER `ControllaTurnoLavorativo` BEFORE INSERT ON `Autisti` FOR EACH ROW BEGIN

-- Controlla se l'autista è stato già assegnato al turno richiesto
	IF EXISTS (
		SELECT 1
		FROM Autisti a 
		WHERE Turno = NEW.Turno AND ID_Autista = NEW.ID_Autista
	) THEN
	
	-- Se si, interrompi l'inserimento
		SIGNAL SQLSTATE '45000'
		SET MESSAGE_TEXT = '[ERRORE],UN AUTISTA NON PUÒ ESSERE ASSEGNATO A DUE TURNI CHE HANNO LO STESSO ORARIO DI INIZIO E FINE';
	END IF;

END
```
### Inserimenti Manuali

**Personale**

```SQL
INSERT INTO Personale (ID,Nome,Cognome,DDN,NumeroDiTelefono,Email) 
VALUES 
('0','Vittorio','Biagi','1998-11-26','08844337321','Vittorio.Biagi@nolcini-turati.com'),
('1','Silvio','Mantegna','1996-10- 09','+39040631879','Silvio.Mantegna@piacentini.com'),
('2','Federico','Moretti','1992-05-30','+39078431820','Federico.Moretti@villarosa-capone.it'),
('3','Giosuè','Detti','1977-03-30','+39 3701978103','Giosuè.Detti@doria.it'),
('4','Guglielmo','Bettin','1976-08-08','+39 3447844894','Guglielmo.Bettin@cremonesi.it'),
('5','Delfino','Milanesi','1984-08-07','+39 3509792947','Delfino.Milanesi@guariento.eu'),
('6','Silvestro','Bignardi','1984-02-17','+39 0342650724','Silvestro.Bignardi@balbo.it'),
('7','Martina','Geraci','1984-07-31','+39 0713890514','Martina.Geraci@civaschi.it'),
('8','Ermanno','Alboni','1990-10-06','+39 078989004','Ermanno.Alboni@cortese.com'),
('9','Vito','Mascagni','1996-01-23','+39 05657458845','Vito.Mascagni@biagiotti.eu'),
('10','Piersanti','Pertile','1989-03-11','+39 346127109','Piersanti.Pertile@piccinni-polesel.com'),
('11','Roberta','Bosurgi','1997-03-12','03184279808','Roberta.Bosurgi@respighi.it'),
('12','Daniele','Agostinelli','1976-03-17','091700740','Daniele.Agostinelli@impastato.it'),
('13','Serena','Leblanc','1989-04-26','051355931','Serena.Leblanc@sagnelli-villadicani.com'),
('14','Edoardo','Antelami','1984-10-16','+39 04249450467','Edoardo.Antelami@balbi-bulzoni.it'),
('15','Lodovico','Rapisardi','1989-07-10','3421484171','Lodovico.Rapisardi@sgarbi-carfagna.it'),
('16','Lucrezia','Rosiello','1984-05-27','+39 07711000804','Lucrezia.Rosiello@giacconi.com'),
('17','Elena','Udinese','1996-07-18','+39 09311196404','Elena.Udinese@ajello.com'),
('18','Torquato','Luxardo','1991-02-08','0321438284','Torquato.Luxardo@satta.it'),
('19','Pasqual','Camanni','1986-12-04','+39 37830236960','Pasqual.Camanni@piacentini.it'),
('20','Lodovico','Giacometti','1982-02-26','3512617332','Lodovico.Giacometti@garibaldi.org'),
```

**Addetti Marketing**

```SQL
INSERT INTO AddettiMarketing (ID_Addetto,Ruolo) VALUES
('0','Analista'),
('1','Analista'),
('2','Analista'),
('3','Responsabile'),
('4','Analista'),
('5','Analista'),
('6','Responsabile'),
('7','Responsabile'),
('8','Coordinatore'),
('9','Analista'),
('10','Responsabile'),
('11','Coordinatore'),
('12','Analista'),
('13','Analista'),
('14','Responsabile'),
('15','Coordinatore'),
('16','Analista'),
('17','Analista'),
('18','Analista'),
('19','Coordinatore'),
('20','Coordinatore')
```

**Patente**

```SQL
INSERT INTO Patente (NumeroPatente,DDS,Categoria) VALUES ('811IS9GOK','2030-02-09','B96'),
('X2RXRX5RX','2033-09-15','B'),
('AOW966E87','2027-09-20','BE'),
('ZA21GZQPM','2026-04-01','BE'),
('ZLLVLBWR6','2033-12-08','B'),
('GFWT5M7G9','2029-03-20','BE'),
('W1QH79Y70','2031-07-31','BE'),
('T8OE4G2RQ','2033-10-15','BE'),
('1DUHQ91X2','2026-03-10','BE'),
('4PGZ3IMDG','2035-04-29','B'),
('UPNF9SHB3','2029-04-29','BE'),
('ADXA003H4','2033-08-13','B96'),
('RTPHTKBKU','2029-08-23','B'),
('X8PEGJZZP','2030-05-09','BE'),
('5FQHACMFA','2030-07-28','BE'),
('JF4FWNAKM','2033-08-10','B'),
('54A2JHN28','2031-04-20','BE'),
('8CDO00ZTN','2026-12-15','B'),
('3BXT58QYK','2034-05-07','B96'),
('DFP7OBM0C','2028-10-05','BE')
```

**Turni**

```SQL
INSERT INTO Turni (ID_Turno,OrarioInizio,OrarioFine) VALUES ('2','11','22'),
('3','10','22'),
('9','9','21'),
('1','14','15'),
('5','9','14');
```

**Assicurazione**

```SQL
INSERT INTO Assicurazione (ID_Assicurazione,DataScadenza,Tipo) VALUES ('0','1985-01-07','Furto'),
('1','1987-09-05','Incendio'),
('2','1977-11-04','Kasko'),
('3','1998-11-23','Kasko'),
('4','1991-04-24','Furto'),
('5','1983-04-15','Incendio'),
('6','1980-08-07','Incendio'),
('7','2000-11-08','Base'),
('8','2000-12-21','Kasko'),
('9','1993-12-07','Base'),
('10','1998-05-15','Furto'),
('11','1992-07-04','Base'),
('12','1979-11-07','Incendio'),
('13','1987-07-09','Kasko'),
('14','1997-11-29','Base'),
('15','2000-09-20','Furto'),
('16','1989-12-16','Furto'),
('17','1978-10-05','Base'),
('18','2000-06-30','Kasko'),
('19','1988-12-20','Furto')
```

**Veicoli**

```SQL
INSERT INTO Veicoli (Targa,Marca,Modello,PostiDisponibili,Assicurazione) VALUES 
('QN808TI','Audi','RS7','1','0'),
('VE980PG','Range Rover','Punto','11','1'),
('UM351XT','Seat','Panda','9','2'),
('OA879OZ','BMW','RS7','3','3'),
('IM934EY','Fiat','Q8','3','4'),
('FL196OJ','Audi','Punto','4','5'),
('LI807ZJ','Seat','Punto','2','6'),
('DI856GR','Audi','Punto','1','7'),
('NH665WN','Fiat','RS7','3','8'),
('VO082WV','Fiat','Punto','8','9'),
('IP612ED','Seat','Q8','10','10'),
('AE374ON','Fiat','Punto','5','11'),
('GG507WX','Audi','Panda','11','12'),
('WE984WS','Fiat','Q8','10','13'),
('XJ201SN','Fiat','Panda','2','14'),
('CC265IG','Seat','RS7','4','15'),
('FW316JZ','Seat','Punto','1','16'),
('HF694UL','Fiat','RS7','9','17'),
('XG478RG','Fiat','RS7','1','18'),
('YR250TN','Audi','RS7','9','19'),
('LY356XH','Range Rover','Punto','1','20'),
('JU851RZ','BMW','RS7','2','21'),
```

**Autisti**

```SQL
INSERT INTO Autisti (ID_Autista,NumeroPatente,Turno,Targa,Stipendio) VALUES 
('3000','811IS9GOK','3','YR908OS','1350'),
('3001','X2RXRX5RX','2','DM221CA','1350'),
('3002','AOW966E87','2','VU882WG','1350'),
('3003','ZA21GZQPM','9','RC808KO','1350'),
('3004','ZLLVLBWR6','5','MQ075IS','1500'),
('3005','GFWT5M7G9','9','XD626IB','1350'),
('3006','W1QH79Y70','1','YH332SE','1500'),
('3007','T8OE4G2RQ','1','CZ013WH','1200'),
('3008','1DUHQ91X2','3','YW568KE','1350'),
('3009','4PGZ3IMDG','3','YA289WV','1200'),
('3010','UPNF9SHB3','9','MT795ZI','1500'),
('3011','ADXA003H4','2','RS792GT','1350'),
('3012','RTPHTKBKU','9','FJ209LV','1200'),
('3013','X8PEGJZZP','1','OO372ZO','1350'),
('3014','5FQHACMFA','2','ZU002JQ','1350'),
('3015','JF4FWNAKM','9','YV668FM','1350'),
('3016','54A2JHN28','2','GQ771DU','1200'),
('3017','8CDO00ZTN','5','QC080ZE','1500'),
('3018','3BXT58QYK','5','LB808EI','1350'),
```

**Manutentori**

```SQL
INSERT INTO Manutentori (ID_Manutentore,Qualifica) VALUES ('5899','Gommista'),
('5900','Elettrauto'),
('5901','Elettrauto'),
('5902','Elettrauto'),
('5903','Carrozziere'),
('5904','Meccanico'),
('5905','Meccanico'),
('5906','Meccanico'),
('5907','Carrozziere'),
('5908','Gommista'),
('5909','Elettrauto'),
('5910','Elettrauto'),
('5911','Carrozziere'),
('5912','Elettrauto'),
('5913','Carrozziere'),
('5914','Elettrauto'),
('5915','Elettrauto'),
```

**ContattaPerGuasto**

```SQL
INSERT INTO ContattaPerGuasto (ID_Manutentore,ID_Autista,Motivo) VALUES ('5903','3045','Radiatore bucato'),
('5913','3084','Batteria scarica'),
('5977','3393','Gomma Bucata'),
('5941','5563','Spia dell motore accesa'),
('5924','4156','Batteria scarica'),
('5900','4842','Gomma Bucata'),
('5955','4855','Batteria scarica'),
('5942','4731','Radiatore bucato'),
('5931','4943','Radiatore bucato'),
('5932','4952','Gomma Bucata'),
('5944','4726','Spia dell motore accesa'),
('5934','5207','Batteria scarica'),
('5914','4665','Spia dell motore accesa'),
('5972','5622','Batteria scarica'),
('5937','4022','Batteria scarica'),
('5959','3095','Batteria scarica'),
('5900','5118','Batteria scarica'),
('5949','5472','Radiatore bucato'),
```

**Offerta**

```SQL
INSERT INTO Offerta (ID_Offerta,PromoCode,InfoOfferta,ID_Addetto) VALUES ('0','247722','Sconto 15%','1546'),
('1','262516','Credito 5€','2320'),
('2','527888','Credito 10€','1738'),
('3','978138','Sconto 10%','1739'),
('4','584959','Sconto 10%','856'),
('5','119611','Credito 5€','2862'),
('6','784568','Credito 5€','42'),
('7','378627','Credito 10€','1200'),
('8','758473','Sconto 20%','2279'),
('9','439829','Sconto 20%','2156'),
('10','939732','Credito 10€','2042'),
('11','833129','Sconto 15%','1732'),
('12','569732','Credito 10€','1375'),
('13','562421','Sconto 20%','2653'),
('14','374879','Sconto 20%','2360');
```

**Utenti**

```SQL
INSERT INTO Utenti (ID_Utente,Nome,Cognome,Email,Password,ID_Offerta,Abbonamento) VALUES ('0','Pellegrino','Verdi','Pellegrino.Verdi@battisti-tognazzi.eu','DWL5FP0UK','6','Annuale'),
('1','Paloma','Argan','Paloma.Argan@benussi.it','b45C7MVUr','14','Trimestrale'),
('2','Giorgia','Gioberti','Giorgia.Gioberti@catalano.it','fqFf2k6Ga','6','Semestrale'),
('3','Carla','Musatti','Carla.Musatti@stradivari-schiavo.com','UzndLYFhK','1','Trimestrale'),
('4','Fulvio','Toninelli','Fulvio.Toninelli@martinelli.net','aPdqN1XDa','4','Trimestrale'),
('5','Dina','Schiavone','Dina.Schiavone@saffi.com','2V8Fg3WOK','14','Trimestrale'),
('6','Gabriella','Capecchi','Gabriella.Capecchi@alboni.eu','VQYRsjeIO','1','Semestrale'),
('7','Donatella','Cassarà','Donatella.Cassarà@serlupi-boito.com','J26x1U2tw','8','Trimestrale'),
('8','Rosario','Gentili','Rosario.Gentili@pareto.eu','dfkvKraDa','2','Semestrale'),
('9','Donna','Renault','Donna.Renault@stoppani.com','lddQZFKgp','7','Semestrale'),
('10','Filippa','Scamarcio','Filippa.Scamarcio@mozart.net','EKQMTK0rX','13','Trimestrale'),
('11','Michelangelo','Antonelli','Michelangelo.Antonelli@quasimodo.it','I1C8ETBDv','10','Trimestrale'),
('12','Rosalia','Piccinni','Rosalia.Piccinni@abba-toninelli.net','knkXGZPts','8','Semestrale'),
('13','Eugenia','Giusti','Eugenia.Giusti@pisacane-boiardo.it','WrJe7jaBQ','3','Annuale'),
('14','Pomponio','Lattuada','Pomponio.Lattuada@mengolo.it','7y1UtYypS','4','Annuale'),
('15','Sergius','Ungaretti','Sergius.Ungaretti@cimarosa.com','noFAkGOuw','7','Semestrale'),
('16','Aurora','Sanudo','Aurora.Sanudo@eco.it','ZDYYLbpWJ','7','Annuale'),
('17','Gastone','Scarlatti','Gastone.Scarlatti@leonardi.it','5Q9zXBkAi','9','Trimestrale'),
('18','Michelangelo','Trombetta','Michelangelo.Trombetta@falier.it','GwniduJ67','10','Annuale'),
('19','Melania','Tomasini','Melania.Tomasini@correr-falier.com','cvwqBzLSa','7','Semestrale'),
('20','Leopoldo','Ziani','Leopoldo.Ziani@gravina.net','ptICTrH0F','0','Annuale'),
```

**Carta**

```SQL
INSERT INTO Carta (NumeroCarta,DataScandenza,CVV,ID_Utente) VALUES
('4021 5251 9472 2623','2030-01-20','381','0'),
('5306 0663 5975 0160','2031-02-01','154','1'),
('4428 0462 8456 2803','2034-05-21','061','2'),
('5251 0666 5448 0858','2031-08-10','948','3'),
('4648 1318 0001 4806','2034-01-22','407','4'),
('5605 6136 7858 0631','2029-12-22','211','5'),
('4928 1718 1319 8851','2029-12-16','667','6'),
('4038 7150 0970 1075','2028-05-09','978','7'),
('4312 1724 2346 5637','2032-12-01','850','8'),
('5227 1723 2353 3768','2029-06-10','707','9'),
('4766 9223 9703 0345','2032-10-01','979','10'),
('4413 0943 2406 5945','2033-06-18','732','11'),
('4480 0086 9661 9894','2028-09-18','220','12'),
('4079 6293 7799 0605','2028-11-14','325','13'),
('4735 1862 2184 9691','2029-09-24','702','14'),
('5464 9412 6647 7245','2031-06-09','191','15'),
('5351 3979 8589 3638','2031-04-11','958','16'),
('4104 6668 7541 6500','2032-10-20','473','17'),
('4747 6784 2884 1440','2034-08-30','618','18'),
('5625 9569 7806 3052','2031-06-10','755','19'),
('4761 2452 7651 2307','2034-03-21','780','20'),
('4303 4079 1312 8349','2034-10-21','883','21'),
```

**Richieste Prenotazioni**

```SQL
INSERT INTO RichiestePrenotazioni (ID_Richiesta,PuntoDiRaccolta,PuntoDiRilascio,DataRichiesta,OrarioRichiesta,NumeroPasseggeri,ID_Utente,ID_Autista) VALUES 
('1','Centocelle','Garbatella','2022-07-01','16','4','0','4980'),
('2','Tor Vergata','Garbatella','2022-05-13','9','6','1','4401'),
('3','Termini','Finocchio','2022-05-19','10','6','2','5682'),
('4','Colosseo','Finocchio','2023-02-12','10','11','3','4044'),
('5','Anagnina','Finocchio','2023-01-18','20','9','4','3877'),
('6','Anagnina','Finocchio','2023-08-13','11','2','5','4704'),
('7','Anagnina','San Basilio','2022-12-05','16','12','6','4363'),
('8','Colosseo','Finocchio','2022-11-26','14','9','7','4776'),
('9','Anagnina','Garbatella','2023-02-05','20','10','8','4043'),
('10','Centocelle','Ostia','2022-05-26','11','7','9','3992'),
('11','Colosseo','Finocchio','2023-04-04','15','1','10','5472'),
('12','Tor Vergata','Ostia','2023-06-16','16','2','11','5507'),
('13','Termini','Finocchio','2023-11-13','21','10','12','5840'),
('14','Termini','San Lorenzo','2022-02-09','20','10','13','3696'),
('15','Colosseo','San Basilio','2023-05-04','10','8','14','5258'),
('16','Termini','Garbatella','2022-09-04','15','1','15','3671'),
('17','Anagnina','Ostia','2023-10-20','9','5','16','4473'),
('18','Colosseo','San Lorenzo','2022-12-11','20','10','17','4643'),
('19','Eur','San Basilio','2023-10-15','15','3','18','4987'),
('20','Anagnina','Primavalle','2022-10-12','15','3','19','5660'),
```

**Tratte Completate**

```SQL
INSERT INTO TratteCompletate (ID_TrattaC,Costo,NumeroCarta) VALUES 
('0','65€','4021 5251 9472 2623'),
('1','50€','5306 0663 5975 0160'),
('2','50€','4428 0462 8456 2803'),
('3','65€','5251 0666 5448 0858'),
('4','25€','4648 1318 0001 4806'),
('5','50€','5605 6136 7858 0631'),
('6','115€','4928 1718 1319 8851'),
('7','50€','4038 7150 0970 1075'),
('8','65€','4312 1724 2346 5637'),
('9','115€','5227 1723 2353 3768'),
('10','65€','4766 9223 9703 0345'),
('11','35€','4413 0943 2406 5945'),
('12','50€','4480 0086 9661 9894'),
('13','115€','4079 6293 7799 0605'),
('14','25€','4735 1862 2184 9691'),
('15','25€','5464 9412 6647 7245'),
('16','115€','5351 3979 8589 3638'),
('17','25€','4104 6668 7541 6500'),
('18','50€','4747 6784 2884 1440'),
('19','35€','5625 9569 7806 3052'),
('20','50€','4761 2452 7651 2307'),
('21','50€','4303 4079 1312 8349'),
```

**Feedback**

```SQL
INSERT INTO Feedback (ID_Feedback,StelleUtente,CommentoUtente,StelleAutista,CommentoAutista,Data,ID_TrattaCompletata) VALUES 
('0','4','Veicolo molto pulito e comodo.','4','Utente rispettoso.','2023-12-19','2815'),
('1','3','Nulla di particolare','3','Nulla di particolare','2022-07-01','1046'),
('2','3','Nulla di particolare','3','Nulla di particolare','2022-05-13','4476'),
('3','3','Nulla di particolare','3','Nulla di particolare','2022-05-19','5136'),
('4','2','Non mi è piaciuto lo stile di guida','2','Utente ritardatario','2023-02-12','5995'),
('5','4','Veicolo molto pulito e comodo.','4','Utente rispettoso.','2023-01-18','3962'),
('6','4','Veicolo molto pulito e comodo.','4','Utente rispettoso.','2023-08-13','3702'),
('7','5','Autista veramente cordiale','5','Utente veramente genuino','2022-12-05','2406'),
('8','2','Non mi è piaciuto lo stile di guida','2','Utente ritardatario','2022-11-26','6915'),
('9','3','Nulla di particolare','3','Nulla di particolare','2023-02-05','6723'),
('10','1','Non lo prenderò mai più!','1','Utente scortese!','2022-05-26','3968'),
('11','1','Non lo prenderò mai più!','1','Utente scortese!','2023-04-04','4963'),
('12','4','Veicolo molto pulito e comodo.','4','Utente rispettoso.','2023-06-16','4291'),
('13','2','Non mi è piaciuto lo stile di guida','2','Utente ritardatario','2023-11-13','3065'),
('14','1','Non lo prenderò mai più!','1','Utente scortese!','2022-02-09','140'),
('15','2','Non mi è piaciuto lo stile di guida','2','Utente ritardatario','2023-05-04','211'),
('16','1','Non lo prenderò mai più!','1','Utente scortese!','2022-09-04','1982'),
('17','2','Non mi è piaciuto lo stile di guida','2','Utente ritardatario','2023-10-20','2024'),
('18','4','Veicolo molto pulito e comodo.','4','Utente rispettoso.','2022-12-11','2783'),
('19','3','Nulla di particolare','3','Nulla di particolare','2023-10-15','1814'),
('20','2','Non mi è piaciuto lo stile di guida','2','Utente ritardatario','2022-10-12','5646'),
('21','2','Non mi è piaciuto lo stile di guida','2','Utente ritardatario','2022-09-15','3931'),
('22','1','Non lo prenderò mai più!','1','Utente scortese!','2022-10-25','4678'),
('23','3','Nulla di particolare','3','Nulla di particolare','2022-08-24','198'),
('24','3','Nulla di particolare','3','Nulla di particolare','2022-12-04','6150'),
('25','2','Non mi è piaciuto lo stile di guida','2','Utente ritardatario','2022-08-27','3953'),
('26','1','Non lo prenderò mai più!','1','Utente scortese!','2022-08-10','6744'),
('27','3','Nulla di particolare','3','Nulla di particolare','2022-03-30','14'),
```

**Tratte Rifiutate**

```SQL
INSERT INTO TratteRifiutate (ID_TrattaR,Motivazione) VALUES ('6999','Troppo lontano'),
('7000','Problema generale'),
('7001','Problema generale'),
('7002','Indisponibilità al servizio'),
('7003','Indisponibilità al servizio'),
('7004','Problema generale'),
('7005','Problema generale'),
('7006','Indisponibilità al servizio'),
('7007','Problema generale'),
('7008','Troppo lontano'),
('7009','Indisponibilità al servizio'),
('7010','Indisponibilità al servizio'),
('7011','Troppo lontano'),
('7012','Problema generale'),
('7013','Troppo lontano'),
('7014','Problema generale'),
('7015','Troppo lontano'),
```

### Script di creazione automatica di query

Per rendere paragonabili i tempi di esecuzione delle query non ottimizzate con quelle ottimizzate, è stato necessario introdurre, nel database, un gran numero di record.
Per velocizzare questo processo, è stato scritto uno script in Python che scrive tutti gli inserimenti generati casualmente, in un semplice file di testo.

Il file è il seguente

```Python
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

def genRandomCardDate():
    start_date = datetime.date(2027, 1, 1)
    end_date = datetime.date(2034, 12, 30)
    num_days = (end_date - start_date).days
    rand_days = random.randint(1, num_days)
    random_date = start_date + datetime.timedelta(days=rand_days)

    return random_date

def genRandomLicenceDate():
    start_date = datetime.date(2025, 1, 1)
    end_date = datetime.date(2035, 12, 30)
    num_days = (end_date - start_date).days
    rand_days = random.randint(1, num_days)
    random_date = start_date + datetime.timedelta(days=rand_days)

    return random_date

def genRandomRequestDate():
    start_date = datetime.date(2022, 1, 1)
    end_date = datetime.date(2023, 12, 30)
    num_days = (end_date - start_date).days
    rand_days = random.randint(1, num_days)
    random_date = start_date + datetime.timedelta(days=rand_days)

    return random_date

def generateEmail(name, surname):
    
    domain = fake.domain_name()

    return f"{name}.{surname}@{domain}"

def generateTarga():
    SYMBOLS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    NUMBERS = "0123456789"
    start = "".join(random.choice(SYMBOLS) for i in range(2))
    mezzo = "".join(random.choice(NUMBERS) for i in range(3))
    fine = "".join(random.choice(SYMBOLS) for i in range(2))

    return start+mezzo+fine

def generatePsw():
    ALL = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    psw = "".join(random.choice(ALL) for i in range(9))
    return psw

def generateCardNumber():
    NUMBERS = "0123456789"
    number = "".join(random.choice(NUMBERS) for i in range(16))
    return number

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
    data = genRandomDate()
    tipo = random.choice(tipo_assicurazione)
    query = "('"+ str(random_id)+ "','"+ str(data)+ "','"+ str(tipo)+ "')"
    unique_Assicurazione.append(random_id)
    values_assicurazione.append(query)
f.write(
    "INSERT INTO Assicurazione (ID_Assicurazione,DataScadenza,Tipo) VALUES "+",\n".join(values_assicurazione)+";"
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
    "INSERT INTO Veicoli (Targa,Marca,Modello,PostiDisponibili,Assicurazione) VALUES "+",\n".join(values_veicolo)+";"
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
```

### Query

Di seguito verranno riportate e query

```SQL
select ID_Richiesta, PuntoDiRaccolta as Partenza, PuntoDiRilascio as Arrivo, Costo, c.NumeroCarta as Carta, u.Nome from `RichiestePrenotazioni` rp 
JOIN `TratteCompletate` tc on rp.`ID_Richiesta` = tc.`ID_TrattaC` 
JOIN `Carta` c on tc.`NumeroCarta` = c.`NumeroCarta` 
JOIN `Utenti` u on c.`ID_Utente` = u.`ID_Utente` 
WHERE u.Nome = 'Mario';
```


#### Ottimizzazione

Di seguito mettere le query ottimizzate tramite index