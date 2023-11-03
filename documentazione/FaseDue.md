# Nome progetto: TaxiTua

## Componenti del gruppo
| Nome     | Cognome  | Matricola | Mail                                  |
| -------- | -------- | --------- | ------------------------------------- |
| Leonardo | Ascenzi  | 0310858   | leonardo.ascenzi@students.uniroma2.eu |
| Franco   | Salvucci | 0306604   | franco.salvucci@students.uniroma2.eu  |
| Nicolò   | Spadoni  | 0311175   | nicolo.spadoni@students.uniroma2.eu   |         |          |           |                                       |

## Motivazioni
Il database che stiamo realizzando è incentrato all'implementazione di un software dedicato all'organizzazione di tratte e viaggi tramite taxi.
L'utente potrà interagire con il sistema per prenotare una corsa, aggiungere una tratta all'elenco dei preferiti, fornire un feedback sia positivo che negativo alla qualità del servizio. 
Gli amministratori, accedendo ad un'area privata del sistema, potranno ricevere report degli utenti, ottimizzare il servizio (tempistiche, costi, ecc...) e impostare 
l'orario di inizio e fine corsa.

## Obiettivi
L'obiettivo principale di questo sistema è permettere agli utenti di organizzare gli spostamenti tramite Taxi a seconda della fascia oraria, del tipo di veicolo scelto e del costo della tratta scelta.
L'amministratore potrà individuare le tratte più gettonate e decidere di effettuare sconti e potenziare il servizio per la zona interessata.
Gli autisti potranno scegliere se accettare o rifiutare la corsa e, nel caso in cui ci fossero emergenze, potranno mettersi in contatto con l'utente tramite una chat dedicata con messaggi preimpostati

## Analisi dei requisiti
Esistono 3 tipologie di veicoli:
- Base: 3 posti disponibili
- Plus: 6 posti disponibili
- Premium: 9 posti disponibili

Il numero dei veicoli circolanti, in ogni zona di Roma, è determinato dall'amministratore di sistema, ma è comunque garantito un numero minimo di veicoli per ogni categoria:
- Base: 5
- Plus: 3
- Premium: 2

Un veicolo non può essere guidato da più autisti nello stesso orario

Ogni veicolo può percorrere una qualunque tratta, anche se fuori dalla sua zona di partenza, ma nel caso in cui tutti i veicoli di quella determinata categoria sono indisponibili in quella zona, l'utente può pagare un sovrapprezzo per richiedere un veicolo di una zona differente.

In ogni zona sono presenti dei nodi che rappresentano l'inizio o la fine di una corsa. Gli utenti possono quindi organizzare gli spostamenti scegliendo il punto di inizio e di fine. Ogni tratta avrà un costo calcolato in base alla distanza in kilometri tra i due nodi. 

Gli utenti hanno diversi ruoli:
- Admin: 1
- Autista: 2
- Utente base: 3

Ogni autista può guidare un silo veicolo, per tutta la durata del turno lavorativo

Gli admin possono:
- Modificare i prezzi delle tratte base
- Visionare le tratte con maggior numero di prenotazioni
- Leggere i feedback lasciati al servizio, filtrandoli tramite nome autista

Per gli utenti sono state pensate le seguenti operazioni:
- Prenotare $n$ corse, ma con il vincolo di una corsa per volta
- Lasciare un feedback all'autista
- Aggiungere alla lista dei preferiti $n$ autisti e $k$ corse
- Accedere alla cronologia delle prenotazioni effettuate dal singolo utente
- Verificare se è possibile usufruire dello spazio adibito al bagaglio a mano/valigia o trasporto animale
- Verificare se un altro utente ha prenotato la stessa corsa e dividere il prezzo di quest'ultima

## Glossario

| Entità   | Descrizione                                                                                         | Sinonimi            | Collegamenti                         |
| -------- | --------------------------------------------------------------------------------------------------- | ------------------- | ------------------------------------ |
| Utenti   | Utente che interagisce con il sistema, si dividono in Amministratori, Autisti e Utenti Base         | User                | Veicoli, Turni, Ricambi e Feedback   |
| Veicoli  | Veicolo adibito a Taxi per effettuare le corse                                                      | Mezzo di trasporto  | Ricambi, Zona, Prenotazione e Utenti |
| Turni    | Lista dei turni del singolo Autista                                                                 | Periodo di servizio | Utenti                               |
| Feedback | Recensione che gli Utenti lasciano all'Autista per giudicare la qualità del servizio                | Recensione          | Utenti                               |
| Ricambi  | Pezzo di ricambio compatibile con un dato veicolo                                                   | Pezzi di ricambio   | Utenti, Veicolo e Officina           |
| Officina | Luogo in cui è possibile effettuare manutenzione ai veicoli di servizio                             | Autoricambi         | Ricambio e Zona                      |
| Tratta   | Percorso standard contenente il punto di partenza e di arrivo che può essere prenotato dagli utenti | Corsa, Percorso     | Utenti e Veicoli                     |
| Zona     | Area adibita al servizio degli autisti                                                              | Settore             | Officina e Veicoli                   |
