
# Indice degli argomenti

```table-of-contents
style: nestedList # TOC style (nestedList|inlineFirstLevel)
minLevel: 0 # Include headings from the specified level
maxLevel: 0 # Include headings up to the specified level
includeLinks: true # Make headings clickable
debugInConsole: false # Print debug info in Obsidian console
```

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

- Autisti
- Manutentori

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
- Partenza, ovvero la **via** da dove si vuole iniziare la corsa
- Arrivo, ovvero la **via** in cui termina la corsa

Ogni **prenotazione** può essere accettata o rifiutata in base a determinate esigenze dell'**utente** (Es: prenotazione effettuata per errore) e dell'**autista** (Es: indisponibilità al servizio).
Ad ogni tratta completata è associato un feedback che può essere lasciato sia dall'**utente** che dall'**autista**.

Ogni **utente** può effettuare illimitate richieste di **prenotazione**, in base alle necessità personali (numero di passeggeri, persone con disabilità, punto di ritiro, punto di rilascio), con il vincolo di una corsa per volta.
A corsa completata l'**utente** può lasciare un **feedback** con un numero di stelle (da 1 a 5) e un commento.
Ogni **utente** deve aggiungere una **carta** con cui effettuare il pagamento relativo alla tratta effettuata, in un secondo momento potrà aggiungere altri metodi di pagamento secondo le proprie esigenze.
Ogni **utente** può aggiungere alla lista dei preferiti ua qualunque delle tratte effettuate da lui, scegliendo se aggiungere solo la tratta o anche l'autista.
Ogni **utente** può accedere alla cronologia delle prenotazioni effettuate.
### Glossario delle entità

| Entità                 | Descrizione                                                       | Attributi                                                                    | Relazioni Coinvolte                                                     |
| ---------------------- | ----------------------------------------------------------------- | ---------------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| Patenti                | Descrive tutte le info riguardanti la patente degli autisti       | **Numero Patente**, DDS, Categoria                                           | Autisti                                                                 |
| Manutentori            | Addetti alla manutenzione delle auto degli autisti                | **ID_Manutentore**, Email, BNumeroTelefono, DDN, Congome, Nome, Qualifica                                                | Autisti                                                                 |
| Autisti                | Personale che svolge il ruolo di autista delle auto nella società | **ID_Autista**, Stipendio, Email, BNumeroTelefono, DDN, Congome, Nome                                                    | Patenti, Manutentori, Veicoli, TratteCompletate, TratteRifiutate,Turni |
| Veicoli                | Auto utilizzate per il servizio di taxi                           | **Targa**, Marca, Modello, NumeroPosti                                 | Autisti, Assicurazione                                                  |
| Turni                  | Turni lavorativi che riguardano gli autisti                       | **OraInzio**, **OraFine**                                     | Autisti                                                                 |
| Richiesta Prenotazione | Richieste di prenotazioni effettuate da parte dall'utente         | **Data**, **Ora**, **ID_Utente**, **Partenza**, **Arrivo**, Numero Passeggeri    | Utenti, Tratte Completate, Tratte Rifiutate, Fermate                               |
| Utenti                 | Utenti utilizzatori del servizio taxi                             | **ID_Utente**, Nome, Cognome, Email, Password                                | Carta, Richiesta Prenotazione, Feedback, Tratte completate              |
| Feedback               | Recensioni lasciate dall'utente e dagli autisti                   | **ID_Feedback**, StelleUtente, CommentoUtente,StelleAutista, CommentoAutista | Tratte Completate, Utenti, Autisti                                      |
| Tratte Completate      | Corse effettuate portate a termine con successo                   | Costo, MetodoDiPagamento                                                     | Richiesta Prenotazione, Feedback,Autisti                                |
| Tratte Rifiutate       | Corse rifiutate da parte dell'autista per determinati motivi      | Motivazione                                                                  | Richiesta Prenotazione, Autisti                                         |
| Carta                  | Carta di credito personale dell'utente                            | **Numero Carta**                                                             | Utenti                                                                  |
| Assicurazioni          | Dati dell'assicurazione associata al singolo veicolo              | **ID_Assicurazione**, Data di scadenza, Tipo                                 | Veicoli                                                                 |
| Fermate                | Elenco delle fermate disponibili                                  | **Latitudine**, **Longitudine**, NomeFermata                                                                             | Richiesta Prenotazione                                                                        |
### Glossario dei termini

| Entità                 | Descrizione                                                       | Sinonimi                  |
| ---------------------- | ----------------------------------------------------------------- | ------------------------- |
| Patente                | Descrive tutte le info riguardanti la patente degli autisti       | Licenza di Guida          |
| Manutentori            | Addetti alla manutenzione delle auto degli autisti                | Meccanici, Operai         |
| Autisti                | Personale che svolge il ruolo di autista delle auto nella società | Driver                    |
| Veicoli                | Auto utilizzate per il servizio di taxi                           | Automobili                |
| Turni                  | Turni lavorativi che riguardano gli autisti                       | Orario Lavorativo         |
| Richiesta Prenotazione | Richieste di prenotazioni effettuate da parte dall'utente         | Prenotazioni              |
| Utenti                 | Utenti utilizzatori del servizio taxi                             | Persone                   |
| Feedback               | Recensioni lasciate dall'utente e dagli autisti                   | Recensioni                |
| Tratte Completate      | Corse effettuate portate a termine con successo                   | Corse                     |
| Tratte Rifiutate       | Corse rifiutate da parte dell'autista per determinati motivi      | Corse Annullate           |
| Carta                  | Carta di credito personale dell'utente                            | Metodo di pagamento       |
| Assicurazioni          | Dati dell'assicurazione associata al singolo veicolo              | RCA, Polizza assicurativa |
| Fermate                | Elenco delle fermate selezionabili da un utente                   | Punti                          |
### Glossario delle relazioni

| Relazione                    | Descrizione                                                                                                                                     | Entità                                     |
| ---------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------ |
| VeicoloPossiedeAssicurazione | Relazione che dice che ogni veicolo ha una propria assicurazione                                                                                | Veicoli (1,1), Assicurazione (1,1)         |
| AutistaGuidaVeicolo          | Relazione che dice che ogni autista guida la propria autovettura                                                                                | Autisti (1,1), Veicoli (1,1)               |
| AutistaPossiedePatente       | Relazione che dice che ogni autista, per poter guidare, necessita di una patente                                                                | Autisti (1,1), Patente (1,1)               |
| ContattaPerGuasto            | Relazione che dice che ogni autista può (non necessariamente) contattare un manutentore per un guasto al veicolo                                | Autisti (0,N), Manutentori (0,N)           |
| AutistaAccettaCorsa          | Relazione che dice che ogni autista accetta la richiesta di prenotazione                                                                        | Autisti (1,N), TratteCompletate (1,1)      |
| AutistaRifiutaCorsa          | Relazione che dice che l'autista rifiuta la corsa, in base a determinate circostanze                                                            | Autisti (1,N), TratteRifiutate (1,1)       |
| UtentePossiedeCarta          | Relazione che dice che ogni utente deve possedere almeno una carta con cui effettuare i pagamenti                                               | Utenti (1,N), Carta (1,1)                  |
| EffettuaPrenotazione         | Relazione che dice che ogni utente effettua una o più prenotazioni                                                                              | Utenti (1,N), Richiesta Prenotazioni (1,1) |
| TrattaAvereFeedback          | Relazione che dice che ogni tratta completata può avere (non necessariamente) un solo feedback, che viene lasciato dagli utenti e dagli autisti | Tratte Completate (0,1), Feedback (1,1)    |
| TabellaOrarioLavorativo      | Ogni autista ha un proprio turno lavorativo, ad ogni turno lavorativo vengono assegnati uno o più autisti                                       | Autisti (1,N), Turni (1,N)                 |
| SceglierePartenza            | Punto di partenza scelto per il ritiro da parte dell'autista                                                                                    | Fermate(1,N), RichiestaPrenotazioni(1,1)   |
| ScegliArrivo                 | Punto di fine scelto per il rilascio da parte dell'autista                                                                                      | Fermate(1,N), RichiestaPrenotazioni(1,1)   |
| Accettare                    | L'autista accetta la tratta                                                                                                                     | Autisti(0,N), TratteCompletate(1,1)        |
| Rifiutare                             | L'autista rifiuta la tratta                                                                                                                                                | Autisti(0,N), TratteRifiutate(1,1)                                           |
## Schemi

### Schema Scheletro

Le entità principali del sistema sono le seguenti:

- *Utenti*
- *RichiestaPrenotazioni*
- *Autisti*

La relazione che intercorre tra queste entità ci permette di affermare che l'*Utente* può effettuare una *Prenotazione* che verrà poi assegnata ad un singolo *Autista*.

![[Scheletro.png |center|600]]

#### Raffinazione

In questo caso stiamo raffinando l'entità *Utenti*.

- Ad ogni *Utente* è associata una o più *Carte* con cui poi l'*Utente* effettuerà i vari pagamenti.

I dati della *Carta* non sono salvati nel database per questioni di privacy, bensì, verranno prelevati tramite interrogazioni al database della banca (che non fa parte del nostro sistema)

![[RaffinazioneUtent.png|center|600]]

In questo caso stiamo raffinando l'entità *Autisti*.

- La prima relazione che si ha descrive il comportamento tra *Autisti* e *Turni*, un*Autista* ha uno o più *Turni* lavorativi, con il vincolo che non può avere due *Turni* uguali. Ad un *Turno* sono assegnati uno o più *Autisti*

- La seconda relazione che si ha descrive il comportamento tra *Autisti* e *Patenti*, un *Autista* possiede una ed una sola *Patente*. Una *Patente* è posseduta da uno ed un solo *Autista*

- La terza relazione che si ha descrive il comportamento tra *Autisti* e *Veicoli*, un *Autista* possiede uno più *Veicoli* con cui effettua le sue corse. Il *Veicolo* è privato e quindi è associato ad un singolo *Autista*.

- La quarta relazione che si ha descrive il comportamento tra gli *Autisti* e i *Manutentori*, un *Autista* può contattare uno o più *Manutentori*. Un *Manutentore* può essere contattato da uno o più *Autisti*

- L'ultima relazione descrive il comportamento tra *Veicoli* e *Assicurazioni*, ovvero, ad ogni *Veicolo* è associata una sola *Assicurazione*. Viceversa per le *Assicurazioni*.

![[RaffinazioneAutisti.png |center|600]]

In questo caso stiamo raffinando l'entità *RichiestaPrenotazione*.

- La prima relazione che si ha permette alla *Prenotazione* di decidere uno ed un solo punto di partenza tra le *Fermate*. Le *Fermate* hanno più di un punto di partenza.

- La seconda relazione che si ha permette alla *Prenotazione* di decidere uno ed un solo punto di arrivo tra le *Fermate*. Le *Fermate* hanno più di un punto di arrivo.

Successivamente si evidenzia il fatto che la *RichiestaPrenotazione* ha 2 entità figlie (*TratteCompletate*, *TratteRifiutate*) che verranno generalizzate più avanti.

- Infine troviamo l'ultima relazione che descrive il comportamento tra le *Tratte completate* e *Feedback*. Una *Tratta Completata* può avere uno ed un solo *Feedback*. Un *Feedback* appartiene ad una sola *Tratta Completata*.

![[RaffinazionePrenotazioni 1.png|center|600]]

### Schema Concettuale

![[SchemaConcettuale.png|center|600]]

#### Normalizzazione

Di seguito si discutono le forme normali dello schema concettuale:

- **1NF**: tutti gli schemi di relazione nello schema logico sopra riportato sono in **1NF**, poiché tutti gli attributi sono semplici, ovvero contengono soltanto valori atomici indivisibili.
- **2NF**: tutti gli schemi di relazione dello schema logico sono anche già in **2NF**, poiché sono già in **1NF** e nessun attributo presenta alcuna dipendenza parziale. Tutti gli attributi dipendono funzionalmente solo dalla chiave primaria della stessa tabella.
- **3NF**: tutti gli schemi di relazione sono anche in **3NF** perché già in **2NF**, ed inoltre, tutti gli attributi delle tabelle dipendono funzionalmente e direttamente dalla chiave primaria, senza transitività.
#### Generalizzazione

Una generalizzazione rappresenta un legame logico tra un’entità genitore e una o più entità figlie, in questo caso l'entità genitore è "Richiesta Prenotazione", e le entità figlie sono:

1) **Richiesta prenotazione**
	1) Tratte completate
	2) Tratte rifiutate

Abbiamo tre metodi per rappresentare una generalizzazione a livello fisico:

- Accorpamento del padre nelle entità figlie
- Accorpamento delle entità figlie nel padre
- Sostituzione della generalizzazione con relazioni

Tra questi metodi abbiamo scelto il terzo in quanto da noi considerato il più adeguato. Infatti, il primo metodo avrebbe portato ad una ridondanza di relazioni.

Il secondo metodo necessita dell’aggiunta di un attributo nell' entità "Richiesta Prenotazioni", ovvero il tipo di prenotazione (Es. Completata = 1 e Rifiutata = 2), in più si sarebbe dovuto scegliere se perdere informazioni (attributi) dei figli o inserire le informazioni nel padre, quindi aggiungere attributi dei figli al padre. La seconda scelta avrebbe portato ad una quantità non indifferente di valori NULL.

Nelle entità, le chiavi secondarie sono indentificate con il pallino grigio, mentre quelle primarie sono identificate con il pallino nero.
#### Schema Finale

![[SchemaFinale.jpg|center|600]]

### Schema Logico

![[SchemaLogico.jpg|center|600]]

Le chiave primarie sono identificate in **grassetto**, mentre le chiavi secondarie (o esterne) sono scritte in stile _Italic_

- Autisti (**Matricola**,Nome,Cognome,Email,DDN,_NumeroPatente_,Stipendio)
- Manutentori (**ID_Manutentore**,Nome,Cognome,Email,DDN,NumeroTelefono,Qualifica)
- ContattaPerGuasto (**_ID_Manutentore_, _ID_Autista_**,Motivo,Data)
- Turni (**OrarioInizio, OrarioFine**)
- TabellaOrarioLavorativo (**_Matricola_,_OrarioInizio_,_OrarioFine_**,Data)
- Veicoli (**Targa**, Marca, Modello, NumPosti,_Matricola_)
- Assicurazione (**Numero**, DataDiScadenza, Tipo,Stato,_Targa_)
- Utenti (**ID_Utente**, Nome, Cognome, Email, DDN, Password)
- Carta (**NumeroCarta**,DDS,CVV, _ID_Utente_)
- Richiesta Prenotazione (**_ID_Utente,Partenza,Arrivo,DataRichiesta,OrarioRichiesta_**, NumeroPasseggeri)
- Tratte Completate (**_ID_Utente,Partenza,Arrivo,DataRichiesta,OrarioRichiesta_**, Costo,MetodoDiPagamento,DataPagamento,OraPagamento,_Matricola_)
- Tratte Rifiutate (**_ID_Utente,Partenza,Arrivo,DataRichiesta,OrarioRichiesta_**, Motivazione,_Matricola_)
- Feedback (**ID_Feedback**, StelleUtente, CommentoUtente,StelleAutista, CommentoAutista,**_ID_Utente,Partenza,Arrivo,DataRichiesta,OrarioRichiesta_**)
### Schema Fisico

Lo schema fisico è il seguente

![[SchemaFisico.jpg|center|700]]

## Implementazione Database - MySQL
### Creazione delle tabelle

```SQL
use VroomA;

CREATE TABLE Patente (
	NumeroPatente varchar(50) not null,
	DDS date not null,
	Categoria varchar(50),
	PRIMARY KEY (NumeroPatente)
);
CREATE TABLE Manutentori (
	ID_Manutentore int not null ,
	Nome varchar(25) not null,
	Cognome varchar(25) not null,
	Email varchar(50) not null,
	DDN date not null,
	NumeroTelefono varchar(25) not null,
	Qualifica varchar(50) not null,
	PRIMARY KEY (ID_Manutentore)
);

CREATE TABLE Autisti (
	Matricola int not null ,
	Nome varchar(25) not null,
	Cognome varchar(25) not null,
	Email varchar(50) not null,
	DDN date not null,
	NumeroTelefono varchar(25) not null,
	NumeroPatente varchar(50) not null,
	Stipendio int not null,
	PRIMARY KEY (Matricola),
	FOREIGN KEY (NumeroPatente) REFERENCES Patente(NumeroPatente)
);

CREATE TABLE Veicoli (
	Targa varchar(50) not null,
	Marca varchar(50) not null,
	Modello varchar(50) not null,
	NumPosti int not null,
	Matricola int not null,
	PRIMARY KEY (Targa),
	FOREIGN KEY (Matricola) REFERENCES Autisti(Matricola)
);

CREATE TABLE Assicurazioni (
	Numero int not null,
	DDS date not null,
	Tipo varchar(50) not null,
	Stato varchar(25) not null,
	Targa varchar(50) not null,
	PRIMARY KEY (Numero),
	FOREIGN KEY (Targa) REFERENCES Veicoli(Targa)
);

CREATE TABLE Turni (
	OrarioInizio int not null,
	OrarioFine int not null,
	PRIMARY KEY (OrarioInizio,OrarioFine)
);


CREATE TABLE Utenti (
	ID_Utente int not null ,
	Nome varchar(50) not null,
	Cognome varchar(50) not null,
	Email varchar(255) not null,
	Password varchar(255) not null,
	DDN date not null,
	PRIMARY KEY (ID_Utente)
);

CREATE TABLE Fermate (
	NomeFermata varchar(50) not null,
	Latitudine varchar(25) not null,
	Longitudine varchar(25) not null,
	PRIMARY KEY (NomeFermata)
);

CREATE TABLE RichiestePrenotazioni (
	ID_Utente int not null,
	Partenza varchar(50) not null,
	Arrivo varchar(50) not null,
	DataRichiesta date not null,
	OrarioRichiesta varchar(25) not null,
	NumeroPasseggeri int not null,
	PRIMARY KEY (ID_Utente,Partenza,Arrivo,DataRichiesta,OrarioRichiesta),
	FOREIGN KEY (ID_Utente) REFERENCES Utenti(ID_Utente),
	FOREIGN KEY (Partenza) REFERENCES Fermate(NomeFermata),
	FOREIGN KEY (Arrivo) REFERENCES Fermate(NomeFermata)
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
	ID_Utente int not null,
	Partenza varchar(50) not null,
	Arrivo varchar(50) not null,
	DataRichiesta date not null,
	OrarioRichiesta varchar(25) not null,
	Costo int not null,
	MetodoDiPagamento varchar(50) not null,
	DataPagamento date not null,
	OraPagamento varchar(10) not null,
	Autista int not null,
	PRIMARY KEY (ID_Utente,Partenza,Arrivo,DataRichiesta,OrarioRichiesta),
	FOREIGN KEY (ID_Utente,Partenza,Arrivo,DataRichiesta,OrarioRichiesta) 
	REFERENCES RichiestePrenotazioni(ID_Utente,Partenza,Arrivo,DataRichiesta,OrarioRichiesta),
	FOREIGN KEY	(Autista) REFERENCES Autisti(Matricola)
);

CREATE TABLE TratteRifiutate (
	ID_Utente int not null,
	Partenza varchar(50) not null,
	Arrivo varchar(50) not null,
	DataRichiesta date not null,
	OrarioRichiesta varchar(25) not null,
	Motivazione varchar(255) not null,
	Autista int not null,
	PRIMARY KEY (ID_Utente,Partenza,Arrivo,DataRichiesta,OrarioRichiesta),
	FOREIGN KEY (ID_Utente,Partenza,Arrivo,DataRichiesta,OrarioRichiesta) 
	REFERENCES RichiestePrenotazioni(ID_Utente,Partenza,Arrivo,DataRichiesta,OrarioRichiesta),
	FOREIGN KEY	(Autista) REFERENCES Autisti(Matricola)
);

CREATE TABLE Feedback (
	ID_Feedback int not null ,
	StelleUtente int not null,
	CommentoUtente varchar(255) not null,
	StelleAutista int not null,
	CommentoAutista varchar(255) not null,
	ID_Utente int not null,
	Partenza varchar(50) not null,
	Arrivo varchar(50) not null,
	DataRichiesta date not null,
	OrarioRichiesta varchar(25) not null,
	PRIMARY KEY (ID_Feedback),
	FOREIGN KEY (ID_Utente,Partenza,Arrivo,DataRichiesta,OrarioRichiesta) 
	REFERENCES TratteCompletate(ID_Utente,Partenza,Arrivo,DataRichiesta,OrarioRichiesta)
);

CREATE TABLE ContattaPerGuasto (
	ID_Manutentore int not null,
	Matricola int not null,
	Motivo varchar(255) not null,
	Data date not null,
	FOREIGN KEY (ID_Manutentore) REFERENCES Manutentori (ID_Manutentore),
	FOREIGN KEY (Matricola) REFERENCES Autisti (Matricola)
);

CREATE TABLE TabellaOrarioLavorativo(
	Matricola int not null,
	OraInizio int not null,
	OraFine int not null,
	Data date not null,
	PRIMARY KEY(Matricola,OraInizio, OraFine,Data),
	FOREIGN KEY	(Matricola) REFERENCES Autisti(Matricola),
	FOREIGN KEY	(OraInizio,OraFine) REFERENCES Turni(OrarioInizio,OrarioFine)
);
```

### Triggers

I trigger fanno parte del DDL (Data Definition Language), essi seguono il principio ECA, ovvero Event-Condition-Action. Solitamente, un trigger si può attivare prima o dopo un inserimento e hanno 2 livelli di granularità:
1. attivarsi per ogni tupla
2. attivarsi per ogni istruzione DML

Nello specifico in MySQL i trigger operano a livello di riga e si ammette un solo trigger per tabella. Osserviamo inoltre che questi vengono usati per mantenere constraint di ogni tipo, in primis il vincolo di integrità referenziale. Quelli di seguito sono una serie di trigger di esempio necessari per mantenere una serie di vincoli nel nostro database

**Maschera CVV**

```SQL
DELIMITER //

CREATE TRIGGER `MaskCVV` BEFORE INSERT ON `Carta` FOR EACH ROW BEGIN

    DECLARE done INT DEFAULT 0;
    DECLARE original_value VARCHAR(255);
    DECLARE str_length INT;
    DECLARE masked_value VARCHAR(255);
    DECLARE cur CURSOR FOR SELECT CVV FROM Carta;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = 1;

    OPEN cur;
    read_loop: LOOP
        FETCH cur INTO original_value;
        IF done THEN
            LEAVE read_loop;
        END IF;
        
        SET str_length = CHAR_LENGTH(original_value);
        SET masked_value = REPEAT('*', str_length);
        
        UPDATE Carta SET CVV = masked_value WHERE CVV = original_value;
    END LOOP;
    CLOSE cur;
END//

DELIMITER ;
```

**Maschera Password Utente**

```SQL
DELIMITER //

CREATE TRIGGER `MaskPSW` BEFORE INSERT ON `Utenti` FOR EACH ROW BEGIN

    DECLARE done INT DEFAULT 0;
    DECLARE original_value VARCHAR(255);
    DECLARE str_length INT;
    DECLARE masked_value VARCHAR(255);
    DECLARE cur CURSOR FOR SELECT Password FROM Utenti;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = 1;

    OPEN cur;
    read_loop: LOOP
        FETCH cur INTO original_value;
        IF done THEN
            LEAVE read_loop;
        END IF;
        
        SET str_length = CHAR_LENGTH(original_value);
        SET masked_value = REPEAT('*', str_length);
        
        UPDATE Utenti SET Password = masked_value WHERE Password = original_value;
    END LOOP;
    CLOSE cur;
END//

DELIMITER ;
```

**Controlla Partenza e Arrivo**

```SQL
use VroomA;

DELIMITER //

CREATE TRIGGER `CheckPartenzaArrivo` BEFORE INSERT ON `RichiestePrenotazioni` FOR EACH ROW BEGIN

-- Controlla se la partenza e l'arrivo sono uguali
	IF EXISTS (
		SELECT 1
		FROM RichiestePrenotazioni
		WHERE NEW.Partenza = NEW.Arrivo
	) THEN
	
	-- Se lo sono, interrompi l'inserimento
		SIGNAL SQLSTATE '45000'
		SET MESSAGE_TEXT = '[ERRORE],LE FERMATE SCELTE NON POSSONO ESSERE UGUALI';
	END IF;

END //
DELIMITER 
```
### Inserimenti

Di seguito vengono riportati alcuni estratti di query per l'inserimento, presi dallo script di creazione automatica delle query

**Patente**

```SQL
INSERT INTO Patenti (NumeroPatente,DDS,Categoria) VALUES ('EHWG3H1B7','2035-05-27','B'),
('Y7YHGWEHQ','2025-12-29','B'),
('UF1SENNTF','2031-02-26','B96'),
('9YT7A9PVI','2029-09-03','BE'),
('RW8IHEVV6','2025-07-27','BE'),
('V237AZUJ2','2035-11-26','BE'),
('9OMH8G2NQ','2034-12-01','B96'),
('8CPZXDWY0','2032-09-30','BE'),
('TKT1JRIBR','2033-02-09','B'),
('BERW3WFWM','2032-06-26','B96'),
('6WZTUDP40','2029-04-08','B96'),
('MQRVDSV6F','2026-10-13','BE'),
('BX02A0VU1','2035-01-31','B'),
('P62UTI6T3','2026-12-09','B'),
('7TEM5ASMM','2035-06-19','B96'),
('QL2D47JVC','2030-04-13','B96'),
('6QMZC1SO8','2025-04-17','B'),
('1VX58URD4','2028-05-22','B'),
('9OIJPBKP5','2031-03-10','B'),
('N30EJXUVS','2028-02-13','BE'),
('C1W3VO2RV','2030-02-24','BE'),
('JZLS8HW6Y','2025-04-13','B96'),
('W8RKEZHZU','2028-04-15','B'),
('L9WMDN05J','2032-12-13','B96'),
```

**Turni**

```SQL
INSERT INTO Turni (OrarioInizio,OrarioFine) VALUES ('10','22'),
('14','21'),
('10','17'),
('9','17'),
('11','20');
```

**Assicurazioni**

```SQL
INSERT INTO Assicurazioni (Numero,DDS,Tipo,Stato,Targa) VALUES ('0','2024-12-11','Polizza cristalli','Valida','EJ653GD'),
('1','2023-01-14','Incendio','Scaduta','EI831GC'),
('2','2023-10-11','Furto','Scaduta','AJ543GE'),
('3','2024-04-01','Polizza cristalli','Valida','BK471BF'),
('4','2024-12-13','Incendio','Valida','EK281EF'),
('5','2024-07-24','Polizza cristalli','Valida','DN364DA'),
('6','2024-10-13','Polizza cristalli','Valida','GM256ED'),
('7','2024-02-23','Incendio','Valida','EP555AF'),
('8','2023-09-08','Base','Scaduta','AQ238AA'),
('9','2024-09-22','Polizza cristalli','Valida','GO564BA'),
('10','2023-07-14','Incendio','Scaduta','DL749AB'),
('11','2024-08-14','Base','Valida','GJ735FG'),
('12','2024-11-22','Incendio','Valida','BO916AE'),
('13','2023-06-05','Polizza cristalli','Scaduta','BR844FC'),
('14','2023-02-03','Polizza cristalli','Scaduta','BP196AE'),
('15','2024-10-22','Base','Valida','BN418FG'),
('16','2023-02-27','Base','Scaduta','DN508CA'),
('17','2023-12-26','Polizza cristalli','Scaduta','FN951DC'),
('18','2024-01-15','Base','Scaduta','DQ859EB'),
('19','2023-11-09','Furto','Scaduta','BR827DD'),
('20','2023-10-02','Kasko','Scaduta','AP980BD'),
('21','2024-06-06','Polizza cristalli','Valida','GL833EB'),
('22','2023-03-29','Furto','Scaduta','CI759DE'),
('23','2023-01-06','Furto','Scaduta','FI524BD'),
('24','2023-02-07','Base','Scaduta','FP347EG'),
('25','2023-09-23','Furto','Scaduta','FP636AD'),
```

**Veicoli**

```SQL
INSERT INTO Veicoli (Targa,Marca,Modello,NumPosti,Matricola) VALUES ('EJ653GD','Alfa Romeo','Giulia','6','907043'),
('EI831GC','Renault','Clio','6','097191'),
('AJ543GE','Renault','Clio','10','892418'),
('BK471BF','Audi','A1','8','367546'),
('EK281EF','Fiat','Panda','9','291867'),
('DN364DA','Audi','RS7','10','660815'),
('GM256ED','Fiat','Tipo','7','996037'),
('EP555AF','Fiat','Panda','12','824266'),
('AQ238AA','Alfa Romeo','Giulia','4','425418'),
('GO564BA','Renault','Captur','11','907043'),
('DL749AB','Alfa Romeo','Giulia','7','705683'),
('GJ735FG','Audi','Q8','7','337035'),
('BO916AE','Range Rover','Hybrid','8','350166'),
('BR844FC','Alfa Romeo','Giulietta','12','184585'),
('BP196AE','Fiat','Punto','8','238930'),
('BN418FG','Fiat','Punto','7','456561'),
('DN508CA','Fiat','Panda','3','988512'),
('FN951DC','Range Rover','Hybrid','6','362750'),
('DQ859EB','BMW','X1','7','765838'),
('BR827DD','Range Rover','Defender','7','166452'),
('AP980BD','BMW','X1','12','387263'),
```

**Autisti**

```SQL
INSERT INTO Autisti (Matricola,Nome,Cognome,Email,DDN,NumeroTelefono,NumeroPatente,Stipendio) VALUES ('862339','Mario','Palazzo','Mario.Palazzo@trentini-pulci.net','1997-10-15','0835517007','EHWG3H1B7','900'),
('359600','Silvia','Lombroso','Silvia.Lombroso@soderini.it','2000-05-17','37364037445','Y7YHGWEHQ','900'),
('766220','Fulvio','Viola','Fulvio.Viola@scaduto.it','1994-01-14','376039271','UF1SENNTF','900'),
('164922','Marco','Chiaramonte','Marco.Chiaramonte@acerbi.net','1977-03-31','+39 09114486182','9YT7A9PVI','900'),
('228009','Orlando','Stefanelli','Orlando.Stefanelli@gori.it','1994-08-02','077582906','RW8IHEVV6','1200'),
('180221','Massimiliano','Mazzocchi','Massimiliano.Mazzocchi@sanudo.it','1982-02-15','0185928182','V237AZUJ2','900'),
('892418','Eraldo','Curiel','Eraldo.Curiel@conte.com','1989-11-06','+39 3629501183','9OMH8G2NQ','800'),
('438144','Lando','Satta','Lando.Satta@montalti.it','2001-12-15','+39 0835247442','8CPZXDWY0','800'),
('557580','Lazzaro','Castelli','Lazzaro.Castelli@fischetti.net','1997-11-09','+39 351745817','TKT1JRIBR','900'),
('726111','Ronaldo','Zabarella','Ronaldo.Zabarella@fantini.com','1999-03-11','+39 0331778576','BERW3WFWM','900'),
```

**Manutentori**

```SQL
INSERT INTO Manutentori (ID_Manutentore,Nome,Cognome,Email,DDN,NumeroTelefono,Qualifica) VALUES ('0','Ezio','Abbagnale','Ezio.Abbagnale@zichichi.eu','1975-03-16','377228848','Meccanico'),
('1','Aldo','Pirandello','Aldo.Pirandello@luna-scaduto.com','1985-04-25','35144225856','Elettrauto'),
('2','Ansaldo','Caracciolo','Ansaldo.Caracciolo@tognazzi.org','1987-08-08','324692291','Meccanico'),
('3','Silvio','Curiel','Silvio.Curiel@caruso.org','1983-12-27','+39 01082492773','Meccanico'),
('4','Donato','Bersani','Donato.Bersani@grossi-boaga.eu','1997-08-02','320651106','Elettrauto'),
('5','Massimo','Serlupi','Massimo.Serlupi@mazzacurati-porcellato.org','1992-09-19','0344384866','Elettrauto'),
('6','Natalia','Opizzi','Natalia.Opizzi@missoni.com','1991-11-01','3500584409','Meccanico'),
('7','Annalisa','Bonolis','Annalisa.Bonolis@modigliani.com','1987-09-17','+39 3778345997','Carrozziere'),
('8','Micheletto','Modigliani','Micheletto.Modigliani@soffici.org','1986-05-24','0933585905','Meccanico'),
('9','Irma','Guglielmi','Irma.Guglielmi@giulietti.com','1981-02-12','+39 0166621144','Carrozziere'),
('10','Rocco','Cortese','Rocco.Cortese@gianetti-modiano.com','1997-09-11','0906462388','Gommista'),
```

**ContattaPerGuasto**

```SQL
INSERT INTO ContattaPerGuasto (ID_Manutentore,Matricola,Motivo,Data) VALUES ('169','919110','Problema con il FAP','2024-04-17'),
('87','887799','Radiatore bucato','2024-06-06'),
('81','267120','Errore centralina','2024-03-10'),
('190','902982','Gomma Bucata','2023-05-29'),
('84','778618','Errore centralina','2024-05-14'),
('79','477856','Problema con il FAP','2023-09-10'),
('40','769888','Guarnizione della testata bruciata','2023-12-25'),
('34','605185','Radiatore bucato','2024-04-15'),
```

**Utenti**

```SQL
INSERT INTO Utenti (ID_Utente,Nome,Cognome,Email,Password,DDN) VALUES ('0','Benvenuto','Crespi','Benvenuto.Crespi@antonello.net','tglhLl809','1998-04-19'),
('1','Pierluigi','Comencini','Pierluigi.Comencini@dulbecco-bergoglio.org','KZcROjzwj','1998-08-24'),
('2','Alessandro','Piccinni','Alessandro.Piccinni@medici.net','eSPCmZKEM','1976-11-09'),
('3','Cassandra','Gagliardi','Cassandra.Gagliardi@montecchi.com','9C4KGy0W5','1977-11-17'),
('4','Tiziana','Ferretti','Tiziana.Ferretti@schiavone.com','u12oqaoer','1981-01-20'),
('5','Annalisa','Calvo','Annalisa.Calvo@ottino.it','y77wFFk1q','1990-03-10'),
('6','Giacomo','Impastato','Giacomo.Impastato@sordi.com','VzzJPry9S','1985-05-13'),
('7','Dolores','Broggini','Dolores.Broggini@monteverdi.it','yOeh4BYEs','1977-12-20'),
('8','Achille','Vanvitelli','Achille.Vanvitelli@scarpetta-roncalli.it','EUGQocKVv','1996-02-16'),
('9','Ciro','Valmarana','Ciro.Valmarana@verdi-mimun.it','5xLHVnvKK','1979-11-09'),
('10','Marisa','Miniati','Marisa.Miniati@marazzi.it','FT3geaukL','1994-12-29'),
('11','Rodolfo','Cuzzocrea','Rodolfo.Cuzzocrea@gravina.com','1gFceVPV7','1995-05-06'),
('12','Rosa','Totino','Rosa.Totino@jacuzzi-sraffa.com','xPTggCyAL','1994-09-06'),
('13','Giuliano','Varano','Giuliano.Varano@cortese-guinizzelli.it','OP7qwo90A','1996-01-08'),
```

**Carta**

```SQL
INSERT INTO Carta (NumeroCarta,DataScadenza,CVV,ID_Utente) VALUES 
('5408 5435 8155 5165','2031-04-21','723','559'),
('5403 9253 8984 9652','2032-11-17','463','7319'),
('4538 0898 9479 9627','2032-03-26','947','92'),
('4137 1568 0601 0206','2027-03-11','305','6653'),
('4132 5464 2554 0178','2034-12-03','682','2540'),
('4659 8931 2359 3963','2027-02-15','550','5095'),
('4110 0127 3522 2047','2031-09-09','526','1217'),
('5477 3054 3417 3215','2034-08-07','624','5836'),
('5165 7046 9800 8081','2033-11-22','509','85'),
('4523 4831 1850 5881','2031-02-20','406','2213'),
('5358 5488 6836 2290','2031-07-04','581','1833'),
('5018 7484 7748 9774','2031-04-22','684','4241'),
('4437 3291 9168 3552','2033-02-27','461','4172'),
```

**Fermate**

```SQL
INSERT INTO Fermate (NomeFermata,Latitudine,Longitudine) VALUES ('Anagnina','41.8425652','12.5860085'),
('Termini','41.9016577','12.5007858'),
('Giardinetti','41.8641331','12.6105711'),
('Lucio Sestio','41.8596969','12.5572829'),
('Porta Furba','41.863995','12.5443672'),
('Tor Bella Monaca','41.868496','12.6412461'),
('Campo de Fiori','41.8955774','12.472158637200002'),
('Trastevere','41.8911586','12.466845904466918'),
('Tufello','42.5621714','1.3071746'),
('Pigneto','41.8884916','12.5281664'),
('Palmiro Togliatti','41.9033311','12.5741939'),
('Salaria','42.912642649999995','13.885354808053245'),
('Verano','46.6053657','11.2262711'),
('Prima Porta','42.0019746','12.4859701'),
('Colosseo','41.8902614','12.493087103595503'),
('Prenestina','41.8953602','12.6149407');
```

**Richieste Prenotazioni**

```SQL
INSERT INTO RichiestePrenotazioni (ID_Utente,Partenza,Arrivo,DataRichiesta,OrarioRichiesta,NumeroPasseggeri) VALUES ('4695','Salaria','Palmiro Togliatti','2023-05-20','20','1'),
('9386','Porta Furba','Campo de Fiori','2021-10-26','16','11'),
('9786','Lucio Sestio','Pigneto','2020-04-05','9','8'),
('4997','Giardinetti','Pigneto','2022-09-17','9','2'),
('5734','Termini','Colosseo','2021-09-12','11','4'),
('7414','Tufello','Prenestina','2021-03-13','10','6'),
('465','Porta Furba','Anagnina','2024-02-13','9','11'),
('4557','Prima Porta','Trastevere','2023-11-28','20','7'),
('7961','Pigneto','Colosseo','2021-06-07','9','6'),
('1865','Pigneto','Prenestina','2022-03-04','14','10'),
('9852','Lucio Sestio','Tufello','2022-09-09','10','8'),
('6460','Verano','Tor Bella Monaca','2020-10-12','14','11'),
('929','Pigneto','Lucio Sestio','2021-01-09','22','4'),
('2007','Campo de Fiori','Pigneto','2023-07-21','20','1'),
('4055','Palmiro Togliatti','Salaria','2022-05-13','15','6'),
('6351','Termini','Lucio Sestio','2021-04-24','22','4'),
('9795','Lucio Sestio','Verano','2023-03-30','11','6'),
```

**Tratte Completate**

```SQL
INSERT INTO TratteCompletate (ID_Utente,Partenza,Arrivo,DataRichiesta,OrarioRichiesta,Costo,MetodoDiPagamento,DataPagamento,OraPagamento,Autista) VALUES ('4695','Salaria','Palmiro Togliatti','2023-05-20','20','25','Postepay','2023-05-20','23','315732'),
('9386','Porta Furba','Campo de Fiori','2021-10-26','16','115','Carta di credito','2021-10-26','23','636668'),
('9786','Lucio Sestio','Pigneto','2020-04-05','9','115','Contanti','2020-04-05','23','752609'),
('4997','Giardinetti','Pigneto','2022-09-17','9','65','Carta di debito','2022-09-17','9','836794'),
('5734','Termini','Colosseo','2021-09-12','11','35','Carta di credito','2021-09-12','15','399715'),
('7414','Tufello','Prenestina','2021-03-13','10','50','CashUp','2021-03-13','22','002725'),
('465','Porta Furba','Anagnina','2024-02-13','9','115','Satispay','2024-02-13','23','332908'),
('4557','Prima Porta','Trastevere','2023-11-28','20','50','Contanti','2023-11-28','21','105954'),
('7961','Pigneto','Colosseo','2021-06-07','9','115','Carta di debito','2021-06-07','23','363195'),
('1865','Pigneto','Prenestina','2022-03-04','14','25','Postepay','2022-03-04','15','801129'),
('9852','Lucio Sestio','Tufello','2022-09-09','10','35','Satispay','2022-09-09','14','908342'),
('6460','Verano','Tor Bella Monaca','2020-10-12','14','115','Carta di credito','2020-10-12','9','777773'),
('929','Pigneto','Lucio Sestio','2021-01-09','22','65','Carta di credito','2021-01-09','23','895521'),
```

**Feedback**

```SQL
INSERT INTO Feedback (ID_Feedback,StelleUtente,CommentoUtente,StelleAutista,CommentoAutista,ID_Utente,Partenza,Arrivo,DataRichiesta,OrarioRichiesta) VALUES ('0','4','Veicolo molto pulito e comodo.','4','Utente gentile','7177','Colosseo','Lucio Sestio','2020-03-01','15'),
('1','2','Non mi è piaciuto lo stile di guida','3','Nulla di particolare','7177','Colosseo','Lucio Sestio','2020-03-01','15'),
('2','1','Non lo prenderò mai più!','5','Utente veramente genuino','7177','Colosseo','Lucio Sestio','2020-03-01','15'),
('3','2','Non mi è piaciuto lo stile di guida','4','Utente gentile','7177','Colosseo','Lucio Sestio','2020-03-01','15'),
('4','5','Autista veramente cordiale','1','Utente scortese!','7177','Colosseo','Lucio Sestio','2020-03-01','15'),
('5','3','Nulla di particolare','3','Utente ok','7177','Colosseo','Lucio Sestio','2020-03-01','15'),
('6','5','Ottima esperienza, lo dirò a tutti','3','Nulla di particolare','7177','Colosseo','Lucio Sestio','2020-03-01','15'),
('7','5','Autista veramente cordiale','2','Non rispetta l autista','7177','Colosseo','Lucio Sestio','2020-03-01','15'),
('8','5','Autista veramente cordiale','4','Utente gentile','7177','Colosseo','Lucio Sestio','2020-03-01','15'),
('9','5','Ottima esperienza, lo dirò a tutti','2','Non rispetta l autista','7177','Colosseo','Lucio Sestio','2020-03-01','15'),
('10','4','Veicolo molto pulito e comodo.','4','Utente rispettoso.','7177','Colosseo','Lucio Sestio','2020-03-01','15'),
```

**Tratte Rifiutate**

```SQL
INSERT INTO TratteRifiutate (ID_Utente,Partenza,Arrivo,DataRichiesta,OrarioRichiesta,Motivazione,Autista) VALUES ('1046','Pigneto','Verano','2022-02-27','11','Utente con recensioni troppo negative','286836'),
('5138','Colosseo','Tor Bella Monaca','2023-01-08','14','Utente con recensioni troppo negative','220447'),
('1082','Prenestina','Colosseo','2020-04-22','15','Problema generale','305507'),
('6458','Palmiro Togliatti','Lucio Sestio','2022-09-20','16','Problema generale','722714'),
('3773','Giardinetti','Pigneto','2023-03-07','22','Indisponibilità al servizio','405336'),
('135','Tor Bella Monaca','Lucio Sestio','2022-08-22','15','Troppo lontano','987641'),
('4922','Anagnina','Salaria','2020-06-24','15','Problema generale','097874'),
('5684','Tor Bella Monaca','Palmiro Togliatti','2022-01-07','10','Indisponibilità al servizio','704570'),
('8725','Campo de Fiori','Salaria','2020-08-10','21','Utente con recensioni troppo negative','987641'),
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
from geopy.geocoders import Nominatim

def getLatAndLong(posto):
    # calling the Nominatim tool and create Nominatim class
    loc = Nominatim(user_agent="Geopy Library")

    # entering the location name
    getLoc = loc.geocode(posto)

    return getLoc.latitude, getLoc.longitude

def prendi_due_elementi(array):
    # Scegli due indici casuali
    indice1, indice2 = random.sample(range(len(array)), 2)
    
    # Se gli elementi sono uguali, scegli un nuovo indice2
    while array[indice1] == array[indice2]:
        indice2 = random.randint(0, len(array) - 1)
    
    return array[indice1], array[indice2]


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
    SYMBOLS = "ABCDEFG"
    SYMBOLS_END = "HIJKLMNOPQR"
    NUMBERS = "0123456789"
    start = "".join(random.choice(SYMBOLS) for i in range(1))
    start_2 = "".join(random.choice(SYMBOLS_END) for i in range(1))
    mezzo = "".join(random.choice(NUMBERS) for i in range(3))
    fine = "".join(random.choice(SYMBOLS) for i in range(2))

    return start+start_2+mezzo+fine

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
print("Inizio Creazione 2.txt")

f = open("2.txt","w+")

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
    inizio = "".join(random.choice(ora_inizio))
    fine = "".join(random.choice(ora_fine))
    unique_Turno.append((inizio,fine))
    query = "('"+ inizio+ "','"+ fine+ "')"
    
    values_turni.append(query)
f.write(
    "INSERT INTO Turni (OrarioInizio,OrarioFine) VALUES "+",\n".join(values_turni)+";"
)
f.write("\n")
print("--------------- Fine Inserimento Turni\n")
print("--------------- Inizio Inserimento Autisti\n")

unique_Autisti = []
values_autisti = []
stipendio = ["1200","1100","900","800"]

for i in range(3000):
    matricola = "".join(random.choice(NUMBERS) for i in range(6))
    if matricola in unique_Autisti:
        matricola = "".join(random.choice(NUMBERS) for i in range(6))
    random_patente = unique_Patente[i]
    #random_Turno = random.choice(unique_Turno[1:])
    #random_targa = random.choice(unique_Veicolo)
    nome = fake.first_name()
    cognome = fake.last_name()
    email = generateEmail(nome,cognome)
    ddn = genRandomDate()
    num_telefono = fake.phone_number()
    query = "('"+ matricola+ "','"+ str(nome)+ "','"+ str(cognome)+ "','"+ str(email)+ "','"+ str(ddn)+ "','"+ num_telefono+ "','"+ random_patente+ "','"+random.choice(stipendio)+"')"
    unique_Autisti.append(matricola)
    values_autisti.append(query)
f.write(
    "INSERT INTO Autisti (Matricola,Nome,Cognome,Email,DDN,NumeroTelefono,NumeroPatente,Stipendio) VALUES "+",\n".join(values_autisti)+";"
)
f.write("\n")
print("--------------- Fine Inserimento Autisti\n")
f.write("\n")
print("--------------- Inizio Inserimento Veicoli\n")
unique_Veicolo = []
values_veicolo = []
dict_veicoli={
    "Fiat":["Punto","Panda"],
    "BMW":["Q3","Q8","X1","Gran Coupè"],
    "Audi":["RS7"],
    "Range Rover":["Hybrid","Defender","Sport"]
}

for i in range(3000):
    random_targa = generateTarga()
    #random_assicurazione = unique_Assicurazione[i]
    marca_random = random.choice(list(dict_veicoli.keys()))
    modello_random = str(random.choice(dict_veicoli[marca_random]))
    autista = unique_Autisti[i]
    query = "('"+ str(random_targa)+ "','"+ str(marca_random)+ "','"+ str(modello_random)+ "','"+str(random.randint(3,12))+"','"+autista+"')"
    unique_Veicolo.append(random_targa)
    values_veicolo.append(query)

f.write(
    "INSERT INTO Veicoli (Targa,Marca,Modello,NumPosti,Matricola) VALUES "+",\n".join(values_veicolo)+";"
)
f.write("\n")
print("--------------- Fine Inserimento Veicoli\n")
print("--------------- Inizio Inserimento Assicurazione\n")

unique_Assicurazione = []
values_assicurazione = []
tipo_assicurazione=["Kasko","Furto","Incendio","Base","Polizza cristalli"]

for i in range(3000):
    random_id = str(i)
    targa = unique_Veicolo[i]
    data = genRandomInsuranceDate()
    tipo = random.choice(tipo_assicurazione)
    if str(data) < "2024-02-16":
        stato = "Scaduta"
    else:
        stato = "Valida"
    query = "('"+ str(random_id)+ "','"+ str(data)+ "','"+ str(tipo)+ "','"+ str(stato)+"','"+str(targa)+"')"
    unique_Assicurazione.append(random_id)
    values_assicurazione.append(query)
f.write(
    "INSERT INTO Assicurazioni (Numero,DDS,Tipo,Stato,Targa) VALUES "+",\n".join(values_assicurazione)+";"
)
f.write("\n")
print("--------------- Fine Inserimento Assicurazione\n")
f.write("\n")
f.write("\n")
f.write("\n")
print("--------------- Inizio Inserimento TabellaOrarioLavorativo\n")

values_tabella = []
unique_TabellaOrario = []
for i in range(2000):
    matricola = random.choice(unique_Autisti)
    turno = random.choice(unique_Turno)
    turno_inizio = turno[0]
    turno_fine = turno[1]
    data = genRandomInsuranceDate()
    query = "('"+ matricola+ "','"+ turno_inizio+ "','"+turno_fine+"','"+str(data)+"')"
    unique_TabellaOrario.append((matricola,turno_inizio,turno_fine,data))
    values_tabella.append(query)
f.write(
    "INSERT INTO TabellaOrarioLavorativo (Matricola,OraInizio,OraFine,Data) VALUES "+",\n".join(values_tabella)+";"
)
f.write("\n")
print("--------------- Fine Inserimento TabellaOrarioLavorativo\n")
f.write("\n")
print("--------------- Inizio Inserimento Manutentori\n")

unique_Manutentori = []
values_manutentori = []
qualifica = ["Gommista","Elettrauto","Meccanico","Carrozziere"]
for i in range(200):
    random_id = str(i)
    nome = fake.first_name()
    cognome = fake.last_name()
    email = generateEmail(nome,cognome)
    ddn = genRandomDate()
    query = "('"+ random_id+ "','"+ random.choice(qualifica)+ "')"
    telefono = fake.phone_number()
    query = "('"+ random_id+ "','"+ str(nome)+ "','"+ str(cognome)+ "','"+ str(email)+ "','"+ str(ddn)+ "','"+ str(telefono)+ "','"+random.choice(qualifica)+"')"
    unique_Manutentori.append(random_id)
    values_manutentori.append(query)
f.write(
    "INSERT INTO Manutentori (ID_Manutentore,Nome,Cognome,Email,DDN,NumeroTelefono,Qualifica) VALUES "+",\n".join(values_manutentori)+";"
)
f.write("\n")
print("--------------- Fine Inserimento Manutentori\n")
f.write("\n")
print("--------------- Inizio Inserimento ContattaPerGuasto\n")

unique_Contatto = []
values_contatto = []
motivi = ["Gomma Bucata","Spia dell motore accesa","Radiatore bucato","Batteria scarica","Problema con il FAP","Errore centralina","Specchietto rotto","Guarnizione della testata bruciata","Rottura degli ammortizzatori","Semiasse distrutto","Differenziale rotto","La macchina non parte","Cambio pasticche dei freni"]

for i in range(1500):
    random_manutentore = random.choice(unique_Manutentori)
    random_autista = random.choice(unique_Autisti[0:200])
    data = genRandomInsuranceDate()
    query = "('"+ random_manutentore+ "','"+ random_autista+ "','"+random.choice(motivi)+"','"+str(data)+"')"
    unique_Contatto.append((random_manutentore,random_autista))
    values_contatto.append(query)
f.write(
    "INSERT INTO ContattaPerGuasto (ID_Manutentore,Matricola,Motivo,Data) VALUES "+",\n".join(values_contatto)+";"
)
f.write("\n")
print("--------------- Fine Inserimento ContattaPerGuasto\n")

print("2.txt Done")
f.close()

print("Inizio Creazione 3.txt")
f = open("3.txt","w+")

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
    data = genRandomDate()
    query = "('"+ random_id+ "','"+ name+ "','"+ surname+ "','"+email+"','"+psw+"','"+str(data)+"')"
    unique_Utenti.append(random_id)
    values_utenti.append(query)
f.write(
    "INSERT INTO Utenti (ID_Utente,Nome,Cognome,Email,Password,DDN) VALUES "+",\n".join(values_utenti)+";"
)
f.write("\n")
print("--------------- Fine Inserimento Utenti\n")
f.write("\n")
print("--------------- Inizio Inserimento Carte\n")

unique_Carta = []
values_carta = []

utente_carta = []
for i in range(20000):
    
    numero_Carta = str(random.randint(4,5))+"".join(str(random.randint(0,9)) for i in range(3))+" "+"".join(str(random.randint(0,9)) for i in range(4))+" "+"".join(str(random.randint(0,9)) for i in range(4))+" "+"".join(str(random.randint(0,9)) for i in range(4))
    data_scadenza = genRandomCardDate()
    cvv = "".join(str(random.randint(0,9)) for i in range(3))
    utente = random.choice(unique_Utenti)
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
f.write("\n")
print("--------------- Inizio Inserimento Fermate\n")

unique_Fermata = []
values_fermata = []
fermate = ["Anagnina","Termini","Giardinetti","Lucio Sestio","Porta Furba","Tor Bella Monaca","Campo de Fiori","Trastevere","Tufello","Pigneto","Palmiro Togliatti","Salaria","Verano","Prima Porta","Colosseo","Prenestina"]

for i in range(16):
    
    fermata_choice = fermate[i]
    latitudine,longitudine = getLatAndLong(fermata_choice)
    query = "('"+ fermata_choice+ "','"+ str(latitudine)+ "','"+ str(longitudine)+ "')"
    unique_Fermata.append(fermata_choice)
    values_fermata.append(query)

f.write(
    "INSERT INTO Fermate (NomeFermata,Latitudine,Longitudine) VALUES "+",\n".join(values_fermata)+";"
)
f.write("\n")
print("--------------- Fine Inserimento Fermate\n")
f.write("\n")
print("--------------- Inizio Inserimento RichiestaPrenotazioni\n")

unique_RichPren = []
values_ricpren = []
date = []
ora = ['9','10','11','14','15','16','20','21','22']
id_carta_utente = []
for i in range(20000):
    #random_id = str(i)
    passeggeri = str(random.randint(1,12))
    
    utente = random.choice(unique_Utenti)
    #autista = random.choice(unique_Autisti)
    data = genRandomRequestDate()
    orario = random.choice(ora)
    partenza,arrivo = prendi_due_elementi(unique_Fermata)
    
    query = "('"+str(utente)+"','"+ str(partenza)+ "','"+ str(arrivo)+ "','"+str(data)+"','"+str(orario)+"','"+str(passeggeri)+"')"
    unique_RichPren.append((utente,partenza,arrivo,data,orario))
    values_ricpren.append(query)
    date.append(data)
f.write(
    "INSERT INTO RichiestePrenotazioni (ID_Utente,Partenza,Arrivo,DataRichiesta,OrarioRichiesta,NumeroPasseggeri) VALUES "+",\n".join(values_ricpren)+";"
)
f.write("\n")
print("--------------- Fine Inserimento RichiestaPrenotazioni\n")
f.write("\n")
print("--------------- Inizio Inserimento TratteCompletate\n")

unique_TrattaC = []
values_trattac = []
costo = ["25","65","115","35","50"]
pagamento = ["Carta di credito","Paypal","Contanti","Satispay","Carta di debito","CashUp","Postepay"]
for i in range(15000):
    pk = unique_RichPren[i]
    costi = random.choice(costo)
    orario_pagamento = random.choice(ora)
    if orario_pagamento < pk[4]:
        orario_pagamento = "23"
    metodo = random.choice(pagamento)
    autista = random.choice(unique_Autisti)
    query = "('"+ str(pk[0])+ "','"+ str(pk[1])+ "','"+ str(pk[2])+ "','"+ str(pk[3])+ "','"+ str(pk[4])+ "','"+ str(costi)+ "','"+ str(metodo)+ "','"+ str(pk[3])+ "','"+ str(orario_pagamento)+ "','"+str(autista)+"')"
    
    unique_TrattaC.append((utente,partenza,arrivo,data,orario))
    values_trattac.append(query)
    
f.write(
    "INSERT INTO TratteCompletate (ID_Utente,Partenza,Arrivo,DataRichiesta,OrarioRichiesta,Costo,MetodoDiPagamento,DataPagamento,OraPagamento,Autista) VALUES "+",\n".join(values_trattac)+";"
)
f.write("\n")
print("--------------- Fine Inserimento TratteCompletate\n")
f.write("\n")
print("--------------- Inizio Inserimento Feedback\n")

unique_Feed = []
values_feed = []
feedback_utente = {
                    1: ["Non lo prenderò mai più!","Esperienza orribile","Guidava in stato di ebrezza"],
                    2: ["Non mi è piaciuto lo stile di guida","La prossima volta preferirei un\' altro autista","Non guidava in modo sicuro"],
                    3: ["Nulla di particolare","Tutto nella norma"],
                    4: ["Veicolo molto pulito e comodo.","Esperienza normale"],
                    5: ["Autista veramente cordiale","Ottima esperienza, lo dirò a tutti"],
                   }

feedback_autisti = {
                    1: ["Utente scortese!","L\' utente offende","L\' utente insisteva nel cambiare strada"],
                    2: ["Utente ritardatario","Non rispetta l\'autista","Stava fumando in macchina"],
                    3: ["Nulla di particolare","Utente ok"],
                    4: ["Utente rispettoso.","Utente gentile"],
                    5: ["Utente veramente genuino","Molto bravo e cortese"],
                   }

for i in range(15000):
    random_id = str(i)
    
    stelle_random_ut = random.choice(list(feedback_utente.keys()))
    
    commento_ut = str(random.choice(feedback_utente[stelle_random_ut]))

    #stelle_random_aut = checkStelleUtenti(stelle_random_ut)
    stelle_random_aut = random.choice(list(feedback_autisti.keys()))
    
    commento_aut = str(random.choice(feedback_autisti[stelle_random_aut]))
    fk_trattac = random.choice(unique_TrattaC)
    query = "('"+ random_id+ "','"+ str(stelle_random_ut)+ "','"+ str(commento_ut)+ "','"+str(stelle_random_aut)+"','"+str(commento_aut)+"','"+str(fk_trattac[0])+"','"+str(fk_trattac[1])+"','"+str(fk_trattac[2])+"','"+str(fk_trattac[3])+"','"+str(fk_trattac[4])+"')"

    unique_Feed.append(random_id)
    values_feed.append(query)
    unique_TrattaC.remove(fk_trattac)

f.write(
    "INSERT INTO Feedback (ID_Feedback,StelleUtente,CommentoUtente,StelleAutista,CommentoAutista,ID_Utente,Partenza,Arrivo,DataRichiesta,OrarioRichiesta) VALUES "+",\n".join(values_feed)+";"
)
f.write("\n")
print("--------------- Fine Inserimento Feedback\n")
f.write("\n")
print("--------------- Inizio Inserimento TratteRifiutate\n")

unique_TrattaR = []
values_trattar = []
motivi = ["Problema generale","Indisponibilità al servizio","Troppo lontano","Fuori dal mio orario lavorativo","Utente con recensioni troppo negative"]
for i in range(5000):
    fk_prenotazione = unique_RichPren[15000+i]
    motivo = random.choice(motivi)
    autista = random.choice(unique_Autisti)
    query = "('"+ str(fk_prenotazione[0])+ "','"+ str(fk_prenotazione[1])+ "','"+ str(fk_prenotazione[2])+ "','"+ str(fk_prenotazione[3])+ "','"+ str(fk_prenotazione[4])+ "','"+ str(motivo)+ "','"+str(autista)+"')"
    unique_TrattaR.append(fk_prenotazione)
    values_trattar.append(query)
f.write(
    "INSERT INTO TratteRifiutate (ID_Utente,Partenza,Arrivo,DataRichiesta,OrarioRichiesta,Motivazione,Autista) VALUES "+",\n".join(values_trattar)+";"
)
f.write("\n")
print("--------------- Fine Inserimento TratteRifiutate\n")
print("4.txt Done")
f.close()
```

### Query

- Visualizza tutte le tratte completate, con annesso costo e carta usata per il pagamento, fatte da un determinato utente

```SQL
SELECT tc.*
from TratteCompletate tc
JOIN Utenti u on tc.ID_Utente = u.ID_Utente
WHERE u.Nome = 'Benvenuto' AND u.Cognome = 'Crespi';
```


![[query1.png|center|700]]


- Visualizza tutti i veicoli la cui assicurazione scadrà entro febbraio 2024

```SQL
SELECT v.Targa, Modello, Marca, a.DDS AS DataScadenza, a.Stato 
FROM Veicoli v
JOIN Assicurazioni a ON v.Targa = a.Targa
WHERE YEAR(a.DDS) = "2024" AND MONTH(a.DDS) = "02" AND Stato = "Valida";
```

![[query2.png|center|500]]


- Visualizza gli autisti che hanno lavorato in una data specifica

```SQL
SELECT a.Nome, a.Cognome, tol.OraInizio, tol.OraFine 
FROM Autisti a
JOIN TabellaOrarioLavorativo tol ON a.Matricola = tol.Matricola
WHERE tol.`Data` = "2020-01-02";
```

![[appunti bsd/Progetto db/Risultati Query/query3.png|center|350]]

- Visualizza tutti gli autisti che hanno avuto lo stesso turno in una data specifica

```SQL
SELECT a.Nome, a.Cognome, tol.OraInizio, tol.OraFine 
FROM Autisti a
JOIN TabellaOrarioLavorativo tol ON a.Matricola = tol.Matricola
WHERE tol.`Data` = "2020-01-02" AND tol.OraInizio = "9" AND tol.OraFine = "17"
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

- Visualizza il numero di feeback con almeno 3 stelle lasciati da ogni utente

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

- Visualizza le tratte completate con un certo tipo di veicolo

```SQL
SELECT TC.*,v.Marca,a.ID_Autista
FROM TratteCompletate TC
JOIN RichiestePrenotazioni rp ON TC.ID_TrattaC = rp.ID_Richiesta
JOIN Autisti a ON rp.ID_Autista = a.ID_Autista
JOIN Veicoli v ON a.Targa = v.Targa
WHERE v.Marca = 'Seat';
```

![[query19.png|center|400]]

- Trova tutti gli autisti che non hanno mai effettuato una richiesta di manutenzione

```SQL
SELECT A.*
FROM Autisti A
WHERE A.ID_Autista NOT IN 
(
	SELECT cpg.ID_Autista FROM ContattaPerGuasto cpg
);
```

![[query20.png|center|300]]

- Visualizza il totale dei pagamenti relativi ad un determinato giorno

```SQL
SELECT SUM(tc.Costo) AS TotalePagamenti FROM TratteCompletate tc
JOIN RichiestePrenotazioni rp ON tc.ID_TrattaC = rp.ID_Richiesta
WHERE rp.DataRichiesta = "2023-06-05"
```

![[query21.png|center|200]]

- Visualizza gli autisti con lo stipendio più alto

```SQL
SELECT *
FROM Autisti
WHERE Stipendio =
(
	SELECT MAX(Stipendio)
	FROM Autisti
);
```

![[query22.png|center|300]]

- Trova gli autisti che hanno completato il minor numero di corse in un determinato giorno

```SQL
SELECT a.ID_Autista,p.Nome,p.Cognome, COUNT(*) AS NumeroCorseEffettuate
FROM TratteCompletate tc 
JOIN RichiestePrenotazioni rp ON tc.ID_TrattaC = rp.ID_Richiesta
JOIN Autisti a ON rp.ID_Autista = a.ID_Autista
JOIN Personale p ON a.ID_Autista = p.ID
WHERE rp.DataRichiesta = "2023-06-05"
GROUP BY a.ID_Autista, p.Nome, p.Cognome
ORDER BY NumeroCorseEffettuate
```

![[query23.png|center|450]]

- Visualizza tutti i dati di un determinato utente, comprese le carte a lui associate

```SQL
SELECT u.*, c.NumeroCarta, c.DataScadenza, c.CVV
FROM Utenti u JOIN Carta c ON c.ID_Utente = u.ID_Utente
WHERE Nome = "Geronimo" AND Cognome = "Lucarelli"
```

![[query24.png|center]]

-  Visualizza tutti gli utenti che hanno almeno 2 carte associate

```SQL
SELECT u.ID_Utente, u.Nome, u.Cognome, COUNT(*) AS NumeroCarteAssociate
FROM Utenti u JOIN Carta c ON c.ID_Utente = u.ID_Utente
GROUP BY u.ID_Utente, u.Nome, u.Cognome
HAVING NumeroCarteAssociate > 2
ORDER BY NumeroCarteAssociate DESC
```

![[query25.png|center|450]]

#### Ottimizzazione

Di seguito abbiamo selezionato degli attributi su cui creare indici secondari per velocizzare l’esecuzione delle query.
Ovviamente, non abbiamo creato troppi indici per una questione di costi di memoria.
Gli indici occupano memoria e quindi abbiamo trovato un compromesso, creando indici solo per gli attributi più richiesti.

**Creazione di indici in MySQL**

```SQL
CREATE INDEX idx_name 
ON Personale(Nome);
```

```SQL
CREATE INDEX idx_stip 
ON Autisti(Stipendio);
```

```SQL
CREATE INDEX idx_ut_star
ON Feedback(StelleUtente);
```

```SQL
CREATE INDEX idx_ut_name
ON Utenti(Nome);
```

Utilizzando questi indici secondari, abbiamo la versione ottimizzata di alcune delle query descritte in precedenza, che vengono eseguite sui dati casuali generati dal programma Python. Riportiamo inoltre, la frazione di miglioramento temporale delle ottimizzazioni.

<u>Formula di miglioramento : 100 * (originale-nuovo) / originale</u>

**Visualizza gli autisti con lo stipendio più alto**

```SQL
SELECT *
FROM Autisti
WHERE Stipendio =
(
	SELECT MAX(Stipendio)
	FROM Autisti
);
```

Prima della creazione dell'index sul campo "Stipendio",  il tempo di esecuzione della query è il seguente
![[tempoEsecQuery1.png|center]]

Dopo aver creato l'index, il tempo di esecuzione è il seguente:

![[tempoEsecQueryConIndex1.png|center]]

La formula di miglioramento risulta essere la seguente
$$100*\frac{(0.063-0.060)}{0.063}\sim 4.7\:\%$$
Quindi, volendo arrotondare, abbiamo un miglioramento di circa il 5%

**Visualizza il numero di feeback con almeno 3 stelle lasciati da ogni utente**

```SQL
SELECT u.Nome,u.Cognome, COUNT(*) AS NumeroFeedback3Stelle
FROM Feedback f JOIN TratteCompletate tc ON f.ID_TrattaCompletata = tc.ID_TrattaC
JOIN RichiestePrenotazioni rp ON tc.ID_TrattaC = rp.ID_Richiesta
JOIN Utenti u ON rp.ID_Utente = u.ID_Utente
WHERE f.StelleUtente >= 3
GROUP BY u.Nome,u.Cognome
ORDER BY NumeroFeedback3Stelle DESC
```

Prima di aver creato l'index sul campo "StelleUtente", il tempo di esecuzione della query è il seguente

![[tempoEsecQuery2.png|center]]

Dopo aver creato l'index, il tempo di esecuzione risulta essere:

![[tempoEsecQueryConIndex2.png|center]]

La formula di miglioramento risulta essere la seguente
$$100*\frac{(0.632-0.342)}{0.632}\sim 45.9\:\%$$

**Visualizza gli utenti che hanno effettuato almeno 10 richieste**

```SQL
SELECT u.ID_Utente, u.Nome, u.Cognome, COUNT(*) AS NumeroRichieste
FROM RichiestePrenotazioni rp JOIN Utenti u ON rp.ID_Utente = u.ID_Utente
GROUP BY u.ID_Utente, u.Nome, u.Cognome
HAVING NumeroRichieste >= 10
ORDER BY NumeroRichieste DESC;
```

Prima di aver creato l'index sul campo "Nome", il tempo di esecuzione della query è il seguente

![[tempoEsecQuery3.png|center]]

Dopo aver creato l'index, il tempo di esecuzione risulta essere:

![[tempoEsecQueryConIndex3.png|center]]

La formula di miglioramento risulta essere la seguente
$$100*\frac{(0.161-0.115)}{0.161}\sim28.6\:\%$$
**Trova gli autisti che hanno completato il minor numero di corse in un determinato giorno**

```SQL
SELECT a.ID_Autista,p.Nome,p.Cognome, COUNT(*) AS NumeroCorseEffettuate
FROM TratteCompletate tc 
JOIN RichiestePrenotazioni rp ON tc.ID_TrattaC = rp.ID_Richiesta
JOIN Autisti a ON rp.ID_Autista = a.ID_Autista
JOIN Personale p ON a.ID_Autista = p.ID
WHERE rp.DataRichiesta = "2023-06-05"
GROUP BY a.ID_Autista, p.Nome, p.Cognome
ORDER BY NumeroCorseEffettuate
```

Prima di aver creato l'index sul campo "Nome", dell'entità Personale, il tempo di esecuzione della query è il seguente

![[tempoEsecQuery4.png|center]]

Dopo aver creato l'index, il tempo di esecuzione risulta essere:

![[tempoEsecQUeryConIndex4.png|center]]

La formula di miglioramento risulta essere la seguente
$$100*\frac{0.035-0.015}{0.035}\sim 57.15\:\%$$

#### Algebra Relazionale

L’algebra relazionale è un linguaggio query _procedurale_ in notazione algebrica. In una query, si applicano sequenzialmente le operazioni alle relazioni. Ogni operazione (unaria o binaria) riceve in input una relazione e ne produce un’altra in output.

Le operazioni _**primitive**_ sono:
- Selezione ($\sigma$)
- Proiezione ($\pi$)
- Unione ($\bigcup$)
- Differenza Insiemistica ($-$)
- Prodotto Cartesiano ($X$)
- Ridenominazione ($\rho$)

Esistono altre operazioni da esse derivabili, tra cui l’intersezione insiemistica ($\bigcap$).
Di seguito troviamo alcune query sul nostro database scritte in Algebra Relazionale:


_**Visualizza tutte le tratte completate che non hanno un feedback**_

```SQL
SELECT tc.* FROM TratteCompletate tc
WHERE tc.ID_TrattaC NOT IN 
(
	SELECT ID_TrattaCompletata FROM Feedback f
);
```

In algebra relazionale la query diventa
$$\pi_{tc.*}(\text{TratteCompletate}\bowtie(\pi_\text{ID\_TrattaC}(\text{TratteCompletate})-\pi_\text{ID\_TrattaCompletata}(\text{Feedback})))$$
_**Visualizza tutti i dati di un determinato utente, comprese le carte a lui associate**_

```SQL
SELECT u.*, c.NumeroCarta, c.DataScadenza, c.CVV
FROM Utenti u JOIN Carta c ON c.ID_Utente = u.ID_Utente
WHERE Nome = "Geronimo" AND Cognome = "Lucarelli"
```

In algebra relazionale la query diventa:
$$\begin{align}&\text{Utenti}\bowtie_{\text{ID\_Utente=ID\_Utente}}\text{Carta}=A\\&\sigma_{\text{Nome='Geronimo',Cognome='Lucarelli'}}(A)\end{align}$$

Dove:

- $\pi$ rappresenta l'operazione di proiezione.
- $\sigma$ rappresenta l'operazione di selezione.
- $\bowtie$ rappresenta l'operazione di join.

L'operazione di join ($\bowtie$) viene eseguita sulla condizione ID_Utente=ID_Utente, e successivamente vengono selezionate le righe in cui Nome="Geronimo" e Cognome="Lucarelli", dopodiché viene applicata la proiezione sui campi specificati.

Per questioni di semplicità, abbiamo denominato con A tutta la parte del join

***Visualizza tutti i veicoli la cui assicurazione scadrà entro febbraio 2024***

```SQL
SELECT Targa, Modello, Marca, a.DataScadenza FROM Veicoli v 
JOIN Assicurazioni a
ON v.ID_Assicurazione = a.ID_Assicurazione
WHERE YEAR(a.DataScadenza) = "2024" AND MONTH(a.DataScadenza) = "02";
```

In algebra relazionale la query diventa:
$$\begin{align}&\text{Veicoli}\bowtie_{\text{ID\_Assicurazione=ID\_Assicurazione}}\text{Assicurazioni}= A\\&\pi_{\text{Targa,Modello,Marca,DataScadenza}}(\sigma_{\text{DataScadenza}<\text{'2024-02-01'}}(A))\end{align}$$

***Visualizza tutti gli autisti che hanno una certa categoria di patente***

```SQL
SELECT p.Nome, p.Cognome, pt.Categoria
FROM Personale p JOIN Autisti a ON p.ID = a.ID_Autista
JOIN Patente pt ON a.NumeroPatente = pt.NumeroPatente
WHERE pt.Categoria = "B96"
```

In algebra relazionale diventa:

$$\begin{align}
&\text{Personale}\bowtie_\text{ID=ID\_Autista}(\text{Autisti}\bowtie_\text{NumeroPatente=NumeroPatente}\text{Patente}) = A\\
&\pi_\text{Nome,Cognome,Categoria}(\sigma_\text{Categoria='B96'}(A))
\end{align}$$

***Trova tutti gli autisti che non hanno mai effettuato una richiesta di manutenzione***

```SQL
SELECT A.*
FROM Autisti A
WHERE A.ID_Autista NOT IN 
(
	SELECT cpg.ID_Autista FROM ContattaPerGuasto cpg
);
```

In algebra relazionale la query diventa

$$\pi_{A.*}(\text{Autisti}\bowtie(\pi_\text{ID\_Autista}(\text{Autisti})-\pi_\text{ID\_Autista}(\text{ContattaPerGuasto})))$$
***Visualizza le tratte completate con un certo tipo di veicolo***

```SQL
SELECT TC.*,v.Marca,a.ID_Autista
FROM TratteCompletate TC
JOIN RichiestePrenotazioni rp ON TC.ID_TrattaC = rp.ID_Richiesta
JOIN Autisti a ON rp.ID_Autista = a.ID_Autista
JOIN Veicoli v ON a.Targa = v.Targa
WHERE v.Marca = 'Seat';
```

In algebra relazionale diventa

$$\begin{align}&\text{TratteCompletate}\bowtie_{\text{ID\_TrattaC=ID\_Richiesta}}\text{RichiestePrenotazioni}\bowtie_{\text{ID\_Autista=ID\_Autista}}\text{Autisti}=A\\&\pi_{\text{TC.*,v.Marca,a.ID\_Autista}}(\sigma_{\text{Marca='Seat'}}(A\bowtie_{\text{Targa=Targa}}\text{Veicoli}))\end{align}$$
Per comodità abbiamo raggruppato tutti i join nella variabile A, per poi effettuare l'ultimo join partendo da A
#### Calcolo Relazionale

Il calcolo relazionale è un linguaggio query non procedurale ma _dichiarativo_. Invece dell’algebra, utilizza il calcolo dei predicati matematici del primo ordine in notazione logica. L’output di una query è una relazione che contiene solo tuple che soddisfano le formule logiche espresse. Il potere espressivo del calcolo relazionale è dunque equivalente a quello
dell’algebra relazionale.

Versioni:
1. Calcolo relazionale sui domini
2. _Calcolo relazionale sulle tuple con dichiarazione di range_

Di seguito sono alcune query espresse tramite il _calcolo relazionale sulle tuple con dichiarazione di range_:

**_Visualizza tutte le tratte completate che non hanno un feedback_**

$$\begin{align}&\text{p} = \text{tc.ID\_TrattaCompletata}\in{\text{tc}}\:\land\:\text{tc.ID\_TrattaCompletata}\not\in\text{f}\\&\{\text{tc.*}\:|\:\text{tc(TratteCompletate),f(Feedback)}\:|\:\text{p} \}\end{align}$$

_**Visualizza tutti i dati di un determinato utente, comprese le carte a lui associate**_

$$\begin{align}&\text{p}=\{(\text{u.Nome='Geronimo'}\land\text{u.Cognome='Lucarelli')}\land(\text{c.ID\_Utente=u.ID\_Utente})\}\\&\{\text{u.*,c.(NumeroCarta,DataScadenza,CVV)}|\text{u(Utenti),c(Carta)}|\:\text{p}\}\end{align}$$

***Visualizza tutti i veicoli la cui assicurazione scadrà entro febbraio 2024***

$$\begin{align*}
&\text{p} = \{\text{(a.DataScadenza} <\text{'2024-01-02')}\land(\text{v.ID\_Assicurazione=a.ID\_Assicurazione})\}\\
&\{\text{v.(Targa,Modello,Marca),a.(DataScadenza) | v(Veicoli),a(Assicurazione) | p} \}
\end{align*}$$

***Visualizza tutti gli autisti che hanno una certa categoria di patente***

$$\begin{align*}
&\text{p} = \{\text{(pt.Categoria='B96'}\land(\text{p.ID=a.ID\_Autista})\land\text{a.NumeroPat = p.NumeroPat}\}\\
&\{\text{p.(Nome,Cognome),pt.(Categoria) | p(Personale), pt(Patenti), a(Autisiti) | p} \}
\end{align*}$$

***Trova tutti gli autisti che non hanno mai effettuato una richiesta di manutenzione***

$$\begin{align}&\text{p} = \{\text{a.ID\_Autista}\in{\text{a}}\:\land\:\text{a.ID\_Autista}\not\in\text{cpg}\}\\&\{\text{a.*}\:|\:\text{a(Autista), cpg(ContattaPerGuasto)}\:|\:\text{p} \}\end{align}$$

***Visualizza le tratte completate con un certo tipo di veicolo***

$$\begin{align*}
&\text{p} = \{(\text{tc.ID\_TrattaC=rp.ID\_Richiesta})\land(\text{a.Id\_Aut = rp.Id\_Aut})\land(\text{a.Targa = v.Targa})\\&\land\text{v.Marca = 'Seat'}\}\\
&\{\text{tc.*, v(Marca), a.(Id\_Aut) | tc.(TratCompl), v(Veicoli), a(Autisti), rp(RichPren) | p} \}
\end{align*}$$
### Sicurezza

Ovviamente in un database aziendale devono essere presenti diverse tipologie di utenti con diversi diritti, nella nostra modellizzazione della realtà, infatti, abbiamo definito 2 classi di utenti:
- un amministratore che ha tutti i diritti
- gli autisti,gli addetti marketing e i manutentori che possono aggiungere righe e fare query

Inoltre, si è definito un terzo utente che ha accesso solamente a delle view in modalità lettura, questo perché non gli si vuole dare accesso alle tabelle originali per questioni di sicurezza. Ovviamente la creazione di questo ultimo utente ha il solo fine dimostrativo e non sarebbe effettivamente inserito in un progetto reale.

Le view sono tabelle che non memorizzano dati, esse condividono lo stesso spazio delle tabelle originali. Spesso vengono assegnate ad altri utenti con specifici campi oscurati anche se il loro utilizzo inappropriato può portare all’inconsistenza del database.
#### Views

 ***Visualizza tutti gli utenti che hanno almeno 2 carte associate***

```SQL
CREATE VIEW CartePerUtente AS 
(
	SELECT u.ID_Utente, u.Nome, u.Cognome, COUNT(*) AS NumeroCarteAssociate
	FROM Utenti u JOIN Carta c ON c.ID_Utente = u.ID_Utente
	GROUP BY u.ID_Utente, u.Nome, u.Cognome
	HAVING NumeroCarteAssociate > 2
	ORDER BY NumeroCarteAssociate DESC
)
```

![[view1.png|center]]

![[risView1.png|center|450]]


***Visualizza il numero di feeback con almeno 3 stelle lasciati da ogni utente***

```SQL
CREATE VIEW NumeroFeedbackTreStelle AS 
(
	SELECT u.Nome,u.Cognome, COUNT(*) AS NumeroFeedback3Stelle
	FROM Feedback f JOIN TratteCompletate tc ON f.ID_TrattaCompletata = tc.ID_TrattaC
	JOIN RichiestePrenotazioni rp ON tc.ID_TrattaC = rp.ID_Richiesta
	JOIN Utenti u ON rp.ID_Utente = u.ID_Utente
	WHERE f.StelleUtente >= 3
	GROUP BY u.Nome,u.Cognome
	ORDER BY NumeroFeedback3Stelle DESC
)
```

![[view2.png|center]]

![[risView2.png|center|450]]

#### Creazione Utenti

Poiché il progetto rappresenta una realtà aziendale di una società, abbiamo creato 3 classi di utenti in ordine decrescente di grado di privilegi. Un amministratore è colui che gestisce il database e quindi ha tutti i diritti. Il personale ha il diritto di inserire nuove tuple e di effettuare query ai fini lavorativi.
Infine, abbiamo creato anche un generico utente autorizzato solo ad interrogare le view esistenti.

1. **Amministratore**: ha tutti i diritti
```SQL
CREATE USER 'administrator'@'localhost' IDENTIFIED BY 'adminpassword';
REVOKE ALL PRIVILEGES, GRANT OPTION FROM 'administrator'@'localhost';
GRANT ALL ON VroomA.* TO 'administrator'@'localhost';
```
2. **Personale**:  Può fare query e inserire tuple
```SQL
CREATE USER 'personale'@'localhost' IDENTIFIED BY 'perspassword';
REVOKE ALL PRIVILEGES, GRANT OPTION FROM 'personale'@'localhost';
GRANT SELECT ON VroomA.* TO 'personale'@'localhost';
GRANT INSERT ON VroomA.* TO 'personale'@'localhost';
```
3. Creazione di un utente che ha il solo diritto di eseguire le view sopra scritte
```SQL
CREATE USER 'lfn'@'localhost' IDENTIFIED BY 'lfnpassword';
REVOKE ALL PRIVILEGES, GRANT OPTION FROM 'lfn'@'localhost';
GRANT SELECT ON CartePerUtente TO 'lfn'@'localhost';
GRANT SELECT ON NumeroFeedbackTreStelle TO 'lfn'@'localhost';
```

#### Crittografia dei dati