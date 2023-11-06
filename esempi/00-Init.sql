CREATE TABLE Personale(
    Matricola int not null auto_increment,
    Nome varchar(255) not null,
    Cognome varchar(255) not null,
    Email varchar(255) not null,
    Password varchar(255) not null,
    Ruolo int not null,
    PRIMARY KEY(Matricola)
);
CREATE TABLE Turni(
    IDT int not null auto_increment,
    Orario_inizio date not null,
    Orario_fine date not null,
    Matricola_Autista int not null,
    PRIMARY KEY(IDT),
    FOREIGN KEY (Matricola_Autista) REFERENCES Personale(Matricola)
);
CREATE TABLE Veicoli(
    Targa varchar(255) not null,
    Marca varchar(255) not null,
    Modello varchar(255) not null,
    Capienza int not null,
    Matricola_Autista int not null,
    PRIMARY KEY(Targa),
    FOREIGN KEY (Matricola_Autista) REFERENCES Personale(Matricola)
);
CREATE TABLE Zone(
    IDZ int not null auto_increment,
    Nome varchar(255) not null,
    Targa varchar(255) not null,
    PRIMARY KEY(IDZ),
    FOREIGN KEY (Targa) REFERENCES Veicoli(Targa)
);

CREATE TABLE Tratta(
    ID_Tratta int not null auto_increment,
    Partenza varchar(255) not null,
    Arrivo varchar(255) not null,
    Costo int not null,
    Tempistica int not null,
    PRIMARY KEY(ID_Tratta)
);
CREATE TABLE Ricambi(
    Serial_Number int not null auto_increment,
    Modello varchar(255) not null,
    Marca_Compatibile varchar(255) not null,
    Costo int not null,
    Targa varchar(255) not null,
    PRIMARY KEY(Serial_Number),
    FOREIGN KEY (Targa) REFERENCES Veicoli(Targa)
);
CREATE TABLE Officina(
    Nome varchar(255) not null,
    Apertura varchar(255) not null,
    Chiusura varchar(255) not null,
    Zona int not null,
    PRIMARY KEY(Nome),
    FOREIGN KEY (Zona) REFERENCES Zone(IDZ)
);


CREATE TABLE Utenti(
    ID_Utente int not null auto_increment,
    Nome varchar(255) not null,
    Cognome varchar(255) not null,
    Email varchar(255) not null,
    Password varchar(255) not null,
    PRIMARY KEY(ID_Utente)
);

CREATE TABLE Feedback(
    ID_Feedback int not null auto_increment,
    Stelle int not null,
    Commento varchar(255) not null,
    Data date not null,
    ID_Utente int not null,
    PRIMARY KEY(ID_Feedback),
    FOREIGN KEY (ID_Utente) REFERENCES Utenti(ID_Utente)
);

CREATE TABLE Guidare(
    Matricola_Autista int not null,
    Targa varchar(255) not null,
    Data date not null,
    Ora date not null,
    FOREIGN KEY (Matricola_Autista) REFERENCES Utenti(ID_Utente),
    FOREIGN KEY (Targa) REFERENCES Veicoli(Targa)
);

CREATE TABLE Prenotare(
    ID_Prenotazione int not null auto_increment,
    IDU int not null,
    Matricola_Autista int not null,
    Targa varchar(255) not null,
    ID_Tratta int not null,
    PRIMARY KEY(ID_Prenotazione),
    FOREIGN KEY (Targa) REFERENCES Veicoli(Targa),
    FOREIGN KEY (Matricola_Autista) REFERENCES Personale(Matricola),
    FOREIGN KEY (IDU) REFERENCES Utenti(ID_Utente),
    FOREIGN KEY (ID_Tratta) REFERENCES Tratta(ID_Tratta)
);