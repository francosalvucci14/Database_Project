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