
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
| Richiesta Prenotazione | Richieste di prenotazioni effettuate da parte dall'utente | **ID**, Punto di raccolta, Punto di rilascio, Data richiesta, Orario richiesta, Numero Passeggeri | Autisti, Utenti, Tratte Complete, Tratte Rifiutate |
| Utenti | Utenti utilizzatori del servizio taxi | **ID**, Nome, Cognome, Email, Password | Carta, Richiesta Prenotazione, Offerte, Feedback, Tratte completate |
| Feedback | Recensioni lasciate dall'utente e dagli autisti | **ID**, StelleUtente, CommentoUtente,StelleAutista, CommentoAutista | Tratte Completate, Utenti, Autisti |
| Tratte Completate | Corse effettuate portate a termine con successo | **ID**, Costo | Richiesta Prenotazione, Feedback, Carta, Utenti |
| Tratte Rifiutate | Corse rifiutate da parte dell'autista per determinati motivi | **ID**, Motivazione | Richiesta Prenotazione |
| Carta | Carta di credito personale dell'utente | **Numero Carta**, Data di Scadenza, CVV | Utenti, Tratte completate |
| Assicurazioni | Dati dell'assicurazione associata al singolo veicolo | **ID**, Data di scadenza, Tipo | Veicoli |
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
| Assicurazioni | Dati dell'assicurazione associata al singolo veicolo | RCA, Polizza assicurativa |
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
- Autisti (**ID_Autista**, Stipendio, _NumeroPatente_, _Targa_, _ID_Turno_)
- Manutentori (**ID_Manutentore**, Qualifica)
- Addetti Marketing (**ID_Addetto**, Ruolo)
- ContattaPerGuasto (_ID_Manutentore_, _ID_Autista_)
- Patente (**NumeroPatente**, DDS, Categoria)
- Turni (**ID_Turno**, OrarioInizio, OrarioFine)
- Veicoli (**Targa**, Marca, Modello, PostiDisponibili, _ID_Assicurazione_)
- Assicurazioni (**ID_Assicurazione**, DataDiScadenza, Tipo)
- Offerte (**ID_Offerta**, PromoCode, InfoOfferta, _ID_Addetto_)
- Utenti (**ID_Utente**, Nome, Cognome, Email, Abbonamento, PSW, _ID_Offerta_)
- Carta (**NumeroCarta**, DataScadenza, CVV, _ID_Utente_)
- Richiesta Prenotazione (**ID_Richiesta**, OrarioRichiesta, NumeroPasseggeri, PuntoRaccolta, PuntoRilascio, _ID_Utente_, _ID_Autista_)
- Tratte Complete (**ID_Tratta**, Costo, _NumeroCarta_)
- Tratte Rifiutate (**ID_Tratta**, Motivazione)
- Feedback (**ID_Feedback**, StelleUtente, CommentoUtente,StelleAutista, CommentoAutista, _ID_TrattaCompletata_)
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

CREATE TABLE Assicurazioni (
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

**Controlla Carta**

```SQL
CREATE TRIGGER `ControllaInserimentiCarta` BEFORE INSERT ON `Carta` FOR EACH ROW BEGIN

-- Controlla se l'autista è stato già assegnato al turno richiesto
	IF EXISTS (
		SELECT 1
		FROM Carta c
		WHERE NumeroCarta = NEW.NumeroCarta AND ID_Utente = NEW.ID_Utente
	) THEN

	-- Se si, interrompi l'inserimento
		SIGNAL SQLSTATE '45000'
		SET MESSAGE_TEXT = '[ERRORE],LA CARTA CHE SI VUOLE AGGIUNGERE È GIÀ PRESENTE NEL DATABASE';

	END IF;

END
```
### Inserimenti

Di seguito vengono riportati alcuni estratti di query per l'inserimento, presi dallo script di creazione automatica delle query

**Personale**

```SQL
INSERT INTO Personale (ID,Nome,Cognome,DDN,NumeroDiTelefono,Email) VALUES('0','Alessandra','Turci','1998-01-10','3367627622','Alessandra.Turci@gradenigo.com'),
('1','Maria','Andreotti','1976-02-25','+39 340517754','Maria.Andreotti@sgalambro.org'),
('2','Elena','Toscanini','1999-04-22','034354072','Elena.Toscanini@casarin.com'),
('3','Lorenzo','Toscani','1986-07-18','0185195557','Lorenzo.Toscani@vittadello-franscini.com'),
('4','Paride','Ferragni','1982-06-09','37608479136','Paride.Ferragni@tarantino-giannuzzi.net'),
('5','Sante','Biagi','1987-10-22','+39 035138406','Sante.Biagi@boccaccio.it'),
('6','Renata','Gonzaga','1982-05-22','0308099892','Renata.Gonzaga@gagliardi.eu'),
('7','Gaetano','Lombroso','1987-01-08','04318152253','Gaetano.Lombroso@ostinelli-ammaniti.it'),
('8','Claudio','Bacosi','1981-08-05','03555787953','Claudio.Bacosi@broschi-pignatti.it'),
('9','Arnulfo','Borromini','1975-04-28','092590091','Arnulfo.Borromini@gaito-branciforte.com'),
('10','Rosalia','Giulietti','1976-10-12','0357716989','Rosalia.Giulietti@renzi.it'),
('11','Durante','Ughi','1998-07-01','3783935849','Durante.Ughi@busoni.eu'),
('12','Annamaria','Travia','1997-12-29','+39 0571009017','Annamaria.Travia@bresciani.it'),
('13','Guarino','Salvini','1995-05-03','+39 37138530579','Guarino.Salvini@santoro.it'),
('14','Eugenia','Prati','1995-05-26','+39 0375042347','Eugenia.Prati@buscetta-ferraris.it'),
('15','Virgilio','Doglioni','1990-01-22','+39 3971845809','Virgilio.Doglioni@montecchi.com'),
('16','Goffredo','Botta','1999-08-22','3711811676','Goffredo.Botta@napolitano.com'),
('17','Raffaellino','Strangio','1983-04-01','+39 0163724485','Raffaellino.Strangio@zamorani.com'),
('18','Mariana','Viviani','1994-06-11','+39 37153448788','Mariana.Viviani@guariento-aulenti.net'),
('19','Valerio','Caffarelli','1999-10-15','+39 058506278','Valerio.Caffarelli@lussu.it'),
('20','Gianfranco','Oscuro','1980-09-26','+39 0141131737','Gianfranco.Oscuro@turchetta.it')
```

**Addetti Marketing**

```SQL
INSERT INTO AddettiMarketing (ID_Addetto,Ruolo) VALUES
('5900','Responsabile'),
('5901','Responsabile'),
('5902','Analista'),
('5903','Responsabile'),
('5904','Coordinatore'),
('5905','Coordinatore'),
('5906','Responsabile'),
('5907','Analista'),
('5908','Coordinatore'),
('5909','Responsabile'),
('5910','Responsabile'),
('5911','Responsabile'),
('5912','Coordinatore'),
('5913','Coordinatore'),
('5914','Responsabile'),
('5915','Responsabile'),
('5916','Analista'),
('5917','Coordinatore'),
('5918','Analista'),
('5919','Analista'),
```

**Patente**

```SQL
INSERT INTO Patente (NumeroPatente,DDS,Categoria) VALUES 
('1VZAPG5HF','2030-07-10','BE'),
('1GIO6ZZN8','2026-04-06','B96'),
('SIHTMVO46','2026-03-08','B96'),
('7XDZBD28P','2029-09-05','BE'),
('MI1VXVJE2','2031-04-09','B96'),
('LNDKURWCJ','2026-04-13','B96'),
('ARTNO6OB4','2030-11-28','BE'),
('F4AHC35K1','2025-09-23','B96'),
('T45K1B5CD','2026-06-19','B'),
('GBC716IUZ','2027-07-31','B96'),
('0RIBPMS0S','2027-09-25','B'),
('7XF1NCD4P','2035-04-08','B'),
('5UDTLYT7S','2034-11-13','B96'),
('6CZMPX888','2034-01-02','BE'),
```

**Turni**

```SQL
IINSERT INTO Turni (ID_Turno,OrarioInizio,OrarioFine) VALUES 
('0','9','17'),
('1','11','22'),
('2','10','21'),
('3','9','22'),
('4','14','17');
```

**Assicurazioni**

```SQL
INSERT INTO Assicurazioni (ID_Assicurazione,DataScadenza,Tipo) VALUES 
('0','2024-07-21','Incendio'),
('1','2023-07-27','Incendio'),
('2','2023-11-03','Kasko'),
('3','2024-12-06','Incendio'),
('4','2023-11-22','Furto'),
('5','2024-01-27','Furto'),
('6','2023-11-17','Furto'),
('7','2023-09-27','Base'),
('8','2023-09-23','Incendio'),
('9','2024-03-30','Kasko'),
('10','2023-06-25','Base'),
('11','2023-01-26','Kasko'),
('12','2023-10-31','Base'),
('13','2023-02-19','Furto'),
('14','2023-09-28','Base'),
('15','2023-01-10','Base'),
('16','2024-03-16','Incendio'),
('17','2023-11-20','Base'),
('18','2023-06-17','Base'),
('19','2024-02-25','Base'),
('20','2023-11-10','Kasko'),
```

**Veicoli**

```SQL
INSERT INTO Veicoli (Targa,Marca,Modello,PostiDisponibili,ID_Assicurazione) VALUES 
('SC670UV','Audi','RS7','2','0'),
('AY173TM','BMW','Panda','11','1'),
('ZD988ED','Audi','Q8','2','2'),
('PS408RD','Fiat','Panda','5','3'),
('VS694BO','Audi','Panda','2','4'),
('BB582OY','Audi','Punto','3','5'),
('CM575GU','Fiat','Punto','10','6'),
('YR313NC','Fiat','Q8','3','7'),
('AF288JI','BMW','Q8','4','8'),
('CF779IO','Fiat','RS7','6','9'),
('QX126ME','Range Rover','Q8','12','10'),
('WK748BW','BMW','Q8','3','11'),
('BL407OS','Range Rover','RS7','5','12'),
('OR153EO','BMW','Punto','1','13'),
('YX590FW','Range Rover','RS7','8','14'),
('PW990ED','Audi','RS7','3','15'),
('UH792HC','BMW','Q8','8','16'),
('XV292AR','Seat','Q8','2','17'),
('LX404VB','Audi','Panda','1','18'),
('NG689AU','Seat','Panda','12','19'),
```

**Autisti**

```SQL
INSERT INTO Autisti (ID_Autista,NumeroPatente,Turno,Targa,Stipendio) VALUES ('0','1VZAPG5HF','3','QF365OB','1200'),
('1','1GIO6ZZN8','2','ZW508CB','800'),
('2','SIHTMVO46','1','VS694BO','1200'),
('3','7XDZBD28P','2','AD555MK','1200'),
('4','MI1VXVJE2','3','US482YF','800'),
('5','LNDKURWCJ','1','XJ474EH','1100'),
('6','ARTNO6OB4','2','XF186JW','1100'),
('7','F4AHC35K1','1','RX184KI','900'),
('8','T45K1B5CD','1','FE998XV','1100'),
('9','GBC716IUZ','2','FL184DP','1100'),
('10','0RIBPMS0S','2','NR192MK','1100'),
('11','7XF1NCD4P','2','VT628VM','900'),
('12','5UDTLYT7S','3','HZ030UQ','1100'),
('13','6CZMPX888','1','YJ817VA','800'),
('14','FLU0C3Y7N','4','EC656OS','900'),
('15','0VJ5IZUF4','1','VS897AB','900'),
('16','FCVLNXPZA','3','GY188RG','800'),
('17','OWVH2ITCE','2','TU882AL','800'),
('18','0J8RQR58D','1','HS782WY','900'),
('19','0F83LL0NU','3','ZZ498WK','800'),
('20','YSE3RS33J','3','VG466BR','1100'),
```

**Manutentori**

```SQL
INSERT INTO Manutentori (ID_Manutentore,Qualifica) VALUES ('3000','Carrozziere'),
('3001','Gommista'),
('3002','Gommista'),
('3003','Carrozziere'),
('3004','Elettrauto'),
('3005','Gommista'),
('3006','Meccanico'),
('3007','Elettrauto'),
('3008','Gommista'),
('3009','Carrozziere'),
('3010','Meccanico'),
('3011','Carrozziere'),
('3012','Meccanico'),
('3013','Meccanico'),
('3014','Carrozziere'),
('3015','Carrozziere'),
('3016','Carrozziere'),
('3017','Meccanico'),
('3018','Carrozziere'),
('3019','Carrozziere'),
```

**ContattaPerGuasto**

```SQL
INSERT INTO ContattaPerGuasto (ID_Manutentore,ID_Autista,Motivo) VALUES ('3303','162','Specchietto rotto'),
('3437','63','Radiatore bucato'),
('4525','10','Errore centralina'),
('4824','194','Radiatore bucato'),
('3366','105','Semiasse distrutto'),
('5492','66','Spia dell motore accesa'),
('5810','148','La macchina non parte'),
('3252','29','Errore centralina'),
('4064','131','Radiatore bucato'),
('4431','34','Semiasse distrutto'),
('4797','105','La macchina non parte'),
('5322','50','Spia dell motore accesa'),
('3278','90','Semiasse distrutto'),
('3679','14','Spia dell motore accesa'),
('4430','147','Semiasse distrutto'),
('3519','25','Rottura degli ammortizzatori'),
('3201','179','Differenziale rotto'),
('4127','91','Errore centralina'),
('3907','145','Specchietto rotto'),
('3652','12','Problema con il FAP'),
('5179','114','Gomma Bucata'),
('3404','2','Semiasse distrutto'),
```

**Offerte**

```SQL
INSERT INTO Offerte (ID_Offerta,PromoCode,InfoOfferta,ID_Addetto) VALUES ('0','273824','Credito 5€','5907'),
('1','364933','Sconto 15%','5969'),
('2','136714','Credito 10€','5942'),
('3','655866','Credito 5€','5970'),
('4','931497','Credito 10€','5966'),
('5','624579','Credito 5€','5998'),
('6','295792','Sconto 20%','5900'),
('7','488267','Credito 10€','5952'),
('8','752354','Credito 10€','5941'),
('9','436112','Credito 10€','5961'),
('10','635915','Sconto 15%','5994'),
('11','292342','Sconto 10%','5909'),
('12','139624','Sconto 20%','5961'),
('13','666711','Credito 5€','5920'),
('14','716143','Sconto 20%','5983');
```

**Utenti**

```SQL
INSERT INTO Utenti (ID_Utente,Nome,Cognome,Email,Password,ID_Offerta) VALUES ('0','Geronimo','Lucarelli','Geronimo.Lucarelli@ligorio.it','UllKLu1aR','12'),
('1','Eva','Montesano','Eva.Montesano@morandi.it','s7w7DABQr','10'),
('2','Umberto','Pizzo','Umberto.Pizzo@fioravanti.net','TUyC3gN2f','2'),
('3','Licia','Interminelli','Licia.Interminelli@manunta-tasso.com','1wbysw17I','10'),
('4','Atenulf','Alfonsi','Atenulf.Alfonsi@liguori.it','M2Wuw90jZ','12'),
('5','Carla','Cadorna','Carla.Cadorna@goldstein-troisi.it','LLpEc0ipa','5'),
('6','Marissa','Cavalcanti','Marissa.Cavalcanti@faugno.it','pxKgaxGJ4','1'),
('7','Manuel','Mogherini','Manuel.Mogherini@chindamo.net','MvvB8NhDy','10'),
('8','Stella','Tencalla','Stella.Tencalla@toscanini-palladio.it','tnNk04ipx','8'),
('9','Venancio','Sgarbi','Venancio.Sgarbi@dellucci.net','bOQ7Qk4Zw','8'),
('10','Donna','Tassoni','Donna.Tassoni@luciani.it','L7r4biloi','9'),
('11','Piero','Marinetti','Piero.Marinetti@travaglio-ferrucci.it','Mq2D9oi3h','4'),
('12','Mario','Colletti','Mario.Colletti@lattuada.com','of1QG2O4m','6'),
('13','Silvia','Giulietti','Silvia.Giulietti@asprucci-tozzi.com','m1Fg0hvy5','5'),
('14','Pomponio','Scarpa','Pomponio.Scarpa@castellitto.com','Esio46MMH','13'),
('15','Leopoldo','Guariento','Leopoldo.Guariento@armellini.com','SIA2coy92','3'),
('16','Viridiana','Beffa','Viridiana.Beffa@travaglia.com','LvmqCIG2Y','1'),
('17','Fausto','Gualtieri','Fausto.Gualtieri@cristoforetti.org','ndvVU7RdX','6'),
('18','Sabatino','Comisso','Sabatino.Comisso@virgilio.org','GcJhrfI47','3'),
('19','Adelasia','Pavanello','Adelasia.Pavanello@santoro.com','JJUn7EmBU','3'),
('20','Germana','Doglioni','Germana.Doglioni@foletti.it','wJsuPsgQv','3'),
```

**Carta**

```SQL
INSERT INTO Carta (NumeroCarta,DataScadenza,CVV,ID_Utente) VALUES 
('5516 6245 1261 0132','2030-10-18','479','0'),
('4757 0060 3749 3269','2031-01-15','850','1'),
('4147 7481 0581 8262','2033-02-16','871','2'),
('4241 7064 9449 0308','2027-05-14','909','3'),
('4130 0669 8284 2854','2030-01-19','573','4'),
('4767 3839 2746 2434','2029-04-20','340','5'),
('4381 7526 0880 0555','2033-01-19','228','6'),
('5648 4762 3809 8495','2032-09-17','883','7'),
('5399 5927 8149 2142','2029-07-13','475','8'),
('4191 1402 6218 6567','2032-02-16','420','9'),
('4909 5358 3453 7202','2030-05-20','248','10'),
('5684 5971 5717 0779','2029-10-27','574','11'),
('4334 5438 9255 3174','2029-08-21','017','12'),
('5349 9153 1786 1035','2029-05-17','280','13'),
('4399 5092 3169 1653','2032-04-08','884','14'),
('4238 1558 8766 1848','2032-05-03','735','15'),
('4092 3571 3675 4525','2031-11-17','452','16'),
('5892 6823 9691 1048','2027-02-18','391','17'),
('4528 2796 0798 3218','2034-08-21','453','18'),
('5280 7228 9635 4347','2028-04-23','090','19'),
('4292 6680 9680 7438','2029-06-05','773','20'),
('5949 3770 6304 7987','2030-10-27','700','21'),
('4597 3672 2445 1647','2031-05-29','484','22'),
('5126 4874 4373 9777','2028-05-03','603','23'),
```

**Richieste Prenotazioni**

```SQL
INSERT INTO RichiestePrenotazioni (ID_Richiesta,PuntoDiRaccolta,PuntoDiRilascio,DataRichiesta,OrarioRichiesta,NumeroPasseggeri,ID_Utente,ID_Autista) VALUES 
('0','Tor Vergata','San Lorenzo','2023-12-16','22','4','2953','2206'),
('1','Centocelle','San Lorenzo','2023-01-08','20','4','2019','783'),
('2','Tor Vergata','San Lorenzo','2023-12-01','11','4','2114','1682'),
('3','Termini','Garbatella','2022-07-01','22','6','2725','1767'),
('4','Centocelle','Finocchio','2023-10-10','22','9','1668','2550'),
('5','Centocelle','Finocchio','2023-06-04','20','3','3890','448'),
('6','Eur','San Basilio','2023-12-10','14','6','1799','1478'),
('7','Colosseo','Garbatella','2022-03-24','10','4','1186','1816'),
('8','Tor Vergata','Finocchio','2022-09-23','21','8','4653','585'),
('9','Eur','San Basilio','2022-03-10','9','6','3440','694'),
('10','Colosseo','Finocchio','2022-04-25','21','7','583','1208'),
('11','Termini','San Basilio','2023-11-23','14','8','4143','2366'),
('12','Colosseo','San Basilio','2022-08-12','20','8','2857','554'),
('13','Centocelle','Primavalle','2023-06-13','14','8','2052','1420'),
('14','Colosseo','Garbatella','2022-11-09','11','4','3713','1738'),
('15','Eur','Ostia','2023-08-05','11','6','961','1822'),
('16','Tor Vergata','San Lorenzo','2023-03-16','15','6','1959','801'),
('17','Eur','Garbatella','2023-10-14','21','12','631','1677'),
('18','Tor Vergata','San Lorenzo','2023-06-10','10','12','1331','1928'),
('19','Colosseo','Ostia','2022-08-30','16','8','853','1029'),
('20','Centocelle','Garbatella','2023-08-26','21','9','909','1922'),
('21','Colosseo','Primavalle','2023-05-06','9','4','3118','2427'),
('22','Anagnina','Garbatella','2022-09-30','11','11','2969','1521'),
('23','Eur','Finocchio','2022-10-29','16','7','109','782'),
('24','Colosseo','Primavalle','2022-06-30','9','11','4021','677'),
('25','Termini','Finocchio','2023-10-24','16','6','3443','2174'),
('26','Tor Vergata','Garbatella','2023-09-05','15','2','2704','584'),
('27','Anagnina','San Lorenzo','2022-09-09','14','12','912','2570'),
('28','Anagnina','Primavalle','2022-01-17','16','12','3096','1222'),
('29','Anagnina','Ostia','2022-11-17','22','3','4189','2245'),
('30','Tor Vergata','San Basilio','2023-08-26','16','4','95','1239'),
```

**Tratte Completate**

```SQL
INSERT INTO TratteCompletate(ID_TrattaC,Costo,NumeroCarta) VALUES ('0','50','4089 5151 5662 4069'),
('1','25','5047 0846 1593 2618'),
('2','50','4061 4269 4847 7335'),
('3','115','5318 1436 0940 0684'),
('4','50','5975 4893 1583 8147'),
('5','65','5684 5078 3830 4961'),
('6','25','5366 8615 7812 6293'),
('7','50','4722 5730 3302 9435'),
('8','35','4543 4190 3841 6987'),
('9','35','5480 6038 6779 5241'),
('10','115','5855 4204 7208 8110'),
('11','25','4341 8786 4075 8180'),
('12','50','4576 1500 6391 0947'),
('13','25','5037 0899 6806 9872'),
('14','25','4045 9340 1401 7460'),
('15','50','5708 7914 3067 7696'),
('16','50','4282 0309 1668 9769'),
('17','25','4868 5174 4338 4566'),
('18','50','4955 5482 5347 8387'),
('19','65','4733 5758 5742 4031'),
('20','65','4116 6449 8486 0800'),
('21','25','4826 7536 1058 0146'),
('22','115','5941 4951 3635 7089'),
```

**Feedback**

```SQL
INSERT INTO Feedback(ID_Feedback,StelleUtente,CommentoUtente,StelleAutista,CommentoAutista,ID_TrattaCompletata) VALUES 
('0','1','Non lo prenderò mai più!','1','L utente offende','7125'),
('1','3','Tutto nella norma','3','Utente ok','10044'),
('2','2','La prossima volta preferirei un altro autista','2','Non rispetta l autista','13925'),
('3','3','Nulla di particolare','3','Utente ok','1942'),
('4','1','Esperienza orribile','1','Utente scortese!','1666'),
('5','1','Non lo prenderò mai più!','1','L utente offende','1417'),
('6','4','Veicolo molto pulito e comodo.','4','Utente gentile','1418'),
('7','1','Non lo prenderò mai più!','1','L utente offende','4084'),
('8','4','Esperienza normale','4','Utente gentile','852'),
('9','1','Non lo prenderò mai più!','1','Utente scortese!','12330'),
('10','5','Autista veramente cordiale','5','Molto bravo e cortese','12209'),
('11','5','Ottima esperienza, lo dirò a tutti','5','Molto bravo e cortese','10205'),
('12','2','La prossima volta preferirei un'altro autista','2','Non rispetta l'autista','10421'),
('13','4','Esperienza normale','4','Utente gentile','2178'),
('14','5','Autista veramente cordiale','5','Molto bravo e cortese','2990'),
('15','3','Tutto nella norma','3','Nulla di particolare','766'),
('16','1','Esperienza orribile','1','Utente scortese!','684'),
('17','1','Non lo prenderò mai più!','1','Utente scortese!','7668'),
('18','2','La prossima volta preferirei un altro autista','2','Utente ritardatario','11378'),
('19','5','Ottima esperienza, lo dirò a tutti','5','Utente veramente genuino','13213'),
('20','4','Esperienza normale','4','Utente rispettoso.','10766'),
('21','2','Non mi è piaciuto lo stile di guida','2','Non rispetta l autista','11735'),
('22','3','Tutto nella norma','3','Nulla di particolare','5012'),
('23','1','Non lo prenderò mai più!','1','L utente offende','3562'),
('24','3','Nulla di particolare','3','Nulla di particolare','11570'),
('25','3','Tutto nella norma','3','Utente ok','8507'),
('26','5','Autista veramente cordiale','5','Molto bravo e cortese','9198'),
('27','1','Esperienza orribile','1','Utente scortese!','12949'),
('28','4','Esperienza normale','4','Utente rispettoso.','7575'),
('29','1','Esperienza orribile','1','Utente scortese!','9106'),
```

**Tratte Rifiutate**

```SQL
INSERT INTO TratteRifiutate (ID_TrattaR,Motivazione) VALUES ('15000','Indisponibilità al servizio'),
('15001','Indisponibilità al servizio'),
('15002','Troppo lontano'),
('15003','Troppo lontano'),
('15004','Troppo lontano'),
('15005','Indisponibilità al servizio'),
('15006','Indisponibilità al servizio'),
('15007','Problema generale'),
('15008','Problema generale'),
('15009','Problema generale'),
('15010','Troppo lontano'),
('15011','Indisponibilità al servizio'),
('15012','Troppo lontano'),
('15013','Problema generale'),
('15014','Indisponibilità al servizio'),
('15015','Problema generale'),
('15016','Indisponibilità al servizio'),
('15017','Problema generale'),
('15018','Troppo lontano'),
('15019','Troppo lontano'),
('15020','Problema generale'),
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
unique_Personale = []

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

unique_AddMark = []

ruoli = ["Responsabile", "Analista", "Coordinatore"]
values_marketing = []
for i in range(100):
   
    random_ruolo = random.choice(ruoli)
    random_id = unique_Personale[5900+i]
    
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
unique_Patente = []
values_patenti = []
for i in range(3000):
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

unique_Turno = []
ora_inizio = ['9','10','11','14']
ora_fine = ['17','20','21','22']
values_turni = []
for i in range(5):
    
    #random_turno = "".join(random.choice(NUMBERS) for i in range(1))
    random_turno = str(i)
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

unique_Assicurazione = []
values_assicurazione = []
tipo_assicurazione=["Kasko","Furto","Incendio","Base"]
for i in range(3000):
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
unique_Veicolo = []
values_veicolo = []
l_marca = ["Fiat","BMW","Audi","Range Rover","Seat"]
l_modello = ["Punto","Panda","Q8","RS7"]
for i in range(3000):
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

unique_Autisti = []
values_autisti = []
stipendio = ["1200","1100","900","800"]
for i in range(3000):
    random_id = unique_Personale[i]
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

unique_Manutentori = []
values_manutentori = []
qualifica = ["Gommista","Elettrauto","Meccanico","Carrozziere"]
for i in range(2900):
    random_id = unique_Personale[3000+i]
    
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

unique_Contatto = []
values_contatto = []
motivi = ["Gomma Bucata","Spia dell motore accesa","Radiatore bucato","Batteria scarica","Problema con il FAP","Errore centralina","Specchietto rotto","Guarnizione della testata bruciata","Rottura degli ammortizzatori","Semiasse distrutto","Differenziale rotto","La macchina non parte","Cambio pasticche dei freni"]

for i in range(500):
    random_manutentore = random.choice(unique_Manutentori)
    random_autista = random.choice(unique_Autisti[0:200])

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

print("--------------- Inizio Inserimento Offerte\n")
unique_Offerta = []
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
    "INSERT INTO Offerte (ID_Offerta,PromoCode,InfoOfferta,ID_Addetto) VALUES "+",\n".join(values_offerta)+";"
)
f.write("\n")
print("--------------- Fine Inserimento Offerte\n")
f.write("\n")
print("--------------- Inizio Inserimento Utenti\n")

unique_Utenti = []
values_utenti = []

for i in range(10000):
    random_id = str(i)
    surname = fake.last_name()
    name = fake.first_name()
    email = str(generateEmail(name, surname))
    psw = generatePsw()
    id_off = random.choice(unique_Offerta)
    query = "('"+ random_id+ "','"+ name+ "','"+ surname+ "','"+email+"','"+psw+"','"+id_off+"')"
    unique_Utenti.append(random_id)
    values_utenti.append(query)
f.write(
    "INSERT INTO Utenti (ID_Utente,Nome,Cognome,Email,Password,ID_Offerta) VALUES "+",\n".join(values_utenti)+";"
)
f.write("\n")
print("--------------- Fine Inserimento Utenti\n")
f.write("\n")
print("--------------- Inizio Inserimento Carte\n")

unique_Carta = []
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
    "INSERT INTO Carta (NumeroCarta,DataScadenza,CVV,ID_Utente) VALUES "+",\n".join(values_carta)+";"
)
print("--------------- Fine Inserimento Carte\n")


print("3.txt Done")
f.close()
print("Inizio creazione 4.txt")
f = open("4.txt","w+")

print("--------------- Inizio Inserimento RichiestaPrenotazioni\n")

unique_RichPren = []
values_ricpren = []
raccolta = ["Anagnina","Termini","Centocelle","Eur","Tor Vergata","Colosseo"]
rilascio = ["Finocchio","Garbatella","Ostia","San Lorenzo","Primavalle","San Basilio"]
date = []
ora = ['9','10','11','14','15','16','20','21','22']
id_carta_utente = []
for i in range(20000):
    random_id = str(i)
    passeggeri = str(random.randint(1,12))
    
    tupla = random.choice(utente_carta[0:5000])
    #print(utente)
    utente = tupla[0]
    id_carta_utente.append(utente)
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

unique_TrattaC = []
values_trattac = []
costo = ["25","65","115","35","50"]
for i in range(15000):
    random_id = unique_RichPren[i]
    costi = random.choice(costo)
    id = int(id_carta_utente[i])
    
    numcarta = utente_carta[id][1]
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

unique_Feed = []
values_feed = []
feedback_utente = {
                    1: ["Non lo prenderò mai più!","Esperienza orribile"],
                    2: ["Non mi è piaciuto lo stile di guida","La prossima volta preferirei un\'altro autista"],
                    3: ["Nulla di particolare","Tutto nella norma"],
                    4: ["Veicolo molto pulito e comodo.","Esperienza normale"],
                    5: ["Autista veramente cordiale","Ottima esperienza, lo dirò a tutti"],
                   }

feedback_autisti = {
                    1: ["Utente scortese!","L\'utente offende"],
                    2: ["Utente ritardatario","Non rispetta l\'autista"],
                    3: ["Nulla di particolare","Utente ok"],
                    4: ["Utente rispettoso.","Utente gentile"],
                    5: ["Utente veramente genuino","Molto bravo e cortese"],
                   }

for i in range(15000):
    random_id = str(i)
    
    stelle_random_ut = random.choice(list(feedback_utente.keys()))
    
    commento_ut = str(random.choice(feedback_utente[stelle_random_ut]))

    stelle_random_aut = checkStelleUtenti(stelle_random_ut)
    
    commento_aut = str(random.choice(feedback_autisti[stelle_random_aut]))
    random_trattac = random.choice(unique_TrattaC)
    query = "('"+ random_id+ "','"+ str(stelle_random_ut)+ "','"+ str(commento_ut)+ "','"+str(stelle_random_aut)+"','"+str(commento_aut)+"','"+str(random_trattac)+"')"

    unique_Feed.append(random_id)
    values_feed.append(query)
    unique_TrattaC.remove(random_trattac)

f.write(
    "INSERT INTO Feedback (ID_Feedback,StelleUtente,CommentoUtente,StelleAutista,CommentoAutista,ID_TrattaCompletata) VALUES "+",\n".join(values_feed)+";"
)
f.write("\n")
print("--------------- Fine Inserimento Feedback\n")
f.write("\n")
print("--------------- Inizio Inserimento TratteRifiutate\n")

unique_TrattaR = []
values_trattar = []
motivi = ["Problema generale","Indisponibilità al servizio","Troppo lontano"]
for i in range(5000):
    random_id = unique_RichPren[15000+i]
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

- Visualizza tutte le tratte completate, con annesso costo e carta usata per il pagamento, fatte da un determinato utente

```SQL
SELECT ID_Richiesta, PuntoDiRaccolta as Partenza, PuntoDiRilascio as Arrivo, Costo, c.NumeroCarta as Carta from `RichiestePrenotazioni` rp 
JOIN `TratteCompletate` tc on rp.`ID_Richiesta` = tc.`ID_TrattaC` 
JOIN `Carta` c on tc.`NumeroCarta` = c.`NumeroCarta` 
JOIN `Utenti` u on c.`ID_Utente` = u.`ID_Utente` 
WHERE u.Nome = 'Carla' AND u.Cognome = 'Raimondi';
```


![[appunti bsd/Progetto db/Risultati Query/query1.png|center|500]]


- Visualizza tutti i veicoli la cui assicurazione scadrà entro febbraio 2024

```SQL
SELECT Targa, Modello, Marca, a.DataScadenza AS DataScadenza FROM Veicoli v 
JOIN Assicurazioni a
ON v.ID_Assicurazione = a.ID_Assicurazione
WHERE YEAR(a.DataScadenza) = "2024" AND MONTH(a.DataScadenza) = "02";
```

![[appunti bsd/Progetto db/Risultati Query/query2.png|center|300]]

- Visualizza il/i turno/i di un dato autista

```SQL
SELECT p.Nome, p.Cognome, t.OrarioInizio, t.OrarioFine FROM Autisti a JOIN Personale p
ON a.ID_Autista = p.ID
JOIN Turni t ON a.Turno = t.ID_Turno
WHERE p.Nome = "Patrizio" AND p.Cognome = "Mattarella";
```

![[appunti bsd/Progetto db/Risultati Query/query3.png|center|350]]

- Visualizza tutti gli autisti che hanno lo stesso turno

```SQL
SELECT p.Nome, p.Cognome, a.Turno, a.ID_Autista FROM Autisti a JOIN Personale p
ON a.ID_Autista = p.ID
JOIN Turni t ON a.Turno = t.ID_Turno
WHERE a.Turno = 2;
```

![[query4.png|center|350]]

- Visualizza la somma dei pagamenti effettuati dagli utenti in una data settimana

```SQL
SELECT SUM(tc.Costo) AS Totale FROM TratteCompletate tc
JOIN RichiestePrenotazioni rp ON tc.ID_TrattaC = rp.ID_Richiesta
WHERE MONTH (rp.DataRichiesta) = "06" AND DAY (rp.DataRichiesta) BETWEEN 1 AND 7
```

![[query5.png|center|300]]

- Visualizza tutte le richieste di manutenzione relative ad uno specifico veicolo

```SQL
SELECT cpg.Motivo, v.* FROM ContattaPerGuasto cpg
JOIN Autisti a ON cpg.ID_Autista = a.ID_Autista
JOIN Veicoli v ON a.Targa = v.Targa
WHERE v.Targa = "QD795XT";
```

![[query6.png|center]]

- Visualizza le 10 tratte più gettonate

```SQL
SELECT PuntoDiRaccolta, PuntoDiRilascio, COUNT(*) AS NumeroRichieste
FROM RichiestePrenotazioni rp
GROUP BY PuntoDiRaccolta, PuntoDiRilascio
ORDER BY NumeroRichieste DESC
LIMIT 10;
```

![[query7.png|center|500]]

- Visualizza gli utenti che hanno effettuato almeno 10 richieste

```SQL

SELECT u.ID_Utente, u.Nome, u.Cognome, COUNT(*) AS NumeroRichieste
FROM RichiestePrenotazioni rp JOIN Utenti u ON rp.ID_Utente = u.ID_Utente
GROUP BY u.ID_Utente, u.Nome, u.Cognome
HAVING NumeroRichieste >= 10
ORDER BY NumeroRichieste DESC;
```

![[query8.png|center|450]]

- Di un dato range di utenti (ID compreso tra 2000 e 6000 e l'iniziale del nome "F"), visualizza le offerte associate agli utenti, con le relative descrizioni

```SQL
SELECT u.ID_Utente, u.Nome, u.Cognome, o.ID_Offerta, o.InfoOfferta
FROM Utenti u JOIN Offerte o ON u.ID_Offerta = o.ID_Offerta
WHERE u.ID_Utente
IN
(
	SELECT ID_Utente 
	FROM Utenti u2 
	WHERE ID_Utente BETWEEN 2000 AND 6000 AND Nome LIKE "F%"
)
```

![[query9.png|center|500]]

- Visualizza il motivo di rifiuto delle richieste di prenotazione che occorre più spesso

```SQL
SELECT tr.Motivazione, COUNT(*) AS NumeroOccorrenze
FROM TratteRifiutate tr GROUP BY tr.Motivazione
ORDER BY NumeroOccorrenze DESC
LIMIT 1;
```

![[query10.png|center|400]]

- Di tutti gli autisti che hanno un ID compreso tra 50 e 400, mostra il turno assegnato e i dati del veicolo che utilizzano

```SQL
SELECT a.ID_Autista, p.Nome, p.Cognome, t.*, v.*
FROM Autisti a JOIN Personale p ON a.ID_Autista = p.ID
JOIN Veicoli v ON a.Targa = v.Targa
JOIN Turni t ON a.Turno = t.ID_Turno
WHERE ID_Autista BETWEEN 50 AND 400;
```

![[query11.png|center]]

- Visualizza tutte le tratte completate che non hanno un feedback

```SQL
SELECT tc.* FROM TratteCompletate tc
WHERE tc.ID_TrattaC NOT IN 
(
	SELECT ID_TrattaCompletata FROM Feedback f
);
```

![[query12.png|center|350]]

- Visualizza tutte le richieste di prenotazione effettuate da un determinato utente

```SQL
SELECT rp.* FROM RichiestePrenotazioni rp 
JOIN Utenti u ON rp.ID_Utente = u.ID_Utente
WHERE u.Nome = 'Carla' AND u.Cognome = 'Raimondi'
```

![[query13.png|center]]

- Visualizza la media delle stelle ottenute da un singolo autista

```SQL
SELECT p.Nome, p.Cognome, AVG(f.StelleUtente) AS MediaStelle
FROM Feedback f
JOIN TratteCompletate tc ON f.ID_TrattaCompletata = tc.ID_TrattaC
JOIN RichiestePrenotazioni rp ON rp.ID_Richiesta = tc.ID_TrattaC
JOIN Autisti a ON rp.ID_Autista = a.ID_Autista
JOIN Personale p ON a.ID_Autista = p.ID
WHERE rp.ID_Autista = '500'
GROUP BY p.Nome, p.Cognome
ORDER BY MediaStelle DESC
```

![[query14.png|center|300]]

- Visualizza il numero totale delle assicurazioni Kasko

```SQL
SELECT COUNT(a.Tipo) AS TotaleKasko
FROM Assicurazioni a
WHERE a.Tipo = 'Kasko';
```

![[query15.png|center|200]]

- Visualizza tutti gli autisti che hanno una certa categoria di patente

```SQL
SELECT p.Nome, p.Cognome, pt.Categoria
FROM Personale p JOIN Autisti a ON p.ID = a.ID_Autista
JOIN Patente pt ON a.NumeroPatente = pt.NumeroPatente
WHERE pt.Categoria = "B96"
```

![[query16.png|center|350]]

- Visualizza il numero di feeback con alemno 3 stelle lasciati da ogni utente

```SQL
SELECT u.Nome,u.Cognome, COUNT(*) AS NumeroFeedback3Stelle
FROM Feedback f JOIN TratteCompletate tc ON f.ID_TrattaCompletata = tc.ID_TrattaC
JOIN RichiestePrenotazioni rp ON tc.ID_TrattaC = rp.ID_Richiesta
JOIN Utenti u ON rp.ID_Utente = u.ID_Utente
WHERE f.StelleUtente >= 3
GROUP BY u.Nome,u.Cognome
ORDER BY NumeroFeedback3Stelle DESC
```

![[query17.png|center|400]]

- Visualizza l'ultima richiesta di prenotazione di un certo utente, aggiungendo (**solo in output**) un campo che dice se la Richiesta fa parte di una tratta completata o no

```SQL
SELECT rp.*, 
IF(rp.ID_Richiesta IN (SELECT ID_TrattaC FROM TratteCompletate tc),'SI','NO' ) AS Completata 
FROM RichiestePrenotazioni rp 
JOIN Utenti u ON rp.ID_Utente = u.ID_Utente
WHERE rp.ID_Utente = '3430' AND rp.DataRichiesta 
IN 
(
	SELECT MAX(DataRichiesta) 
	FROM RichiestePrenotazioni 
	WHERE ID_Utente = '3430'
)
```

![[query18.png|center]]

#### Ottimizzazione

Di seguito mettere le query ottimizzate tramite index