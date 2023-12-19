use ProgettoVroomA;

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
	NumeroPatente int not null,
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
	NumeroPatente int not null,
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
	OrarioRichiesta date not null,
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
	Stelle int not null,
	Commento varchar(255) not null,
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