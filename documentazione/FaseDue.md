# Nome progetto: VRoomA

## Componenti del gruppo

| Nome     | Cognome  | Matricola | Mail                                  |
| -------- | -------- | --------- | ------------------------------------- |
| Leonardo | Ascenzi  | 0310858   | leonardo.ascenzi@students.uniroma2.eu |
| Franco   | Salvucci | 0306604   | franco.salvucci@students.uniroma2.eu  |
| Nicolò   | Spadoni  | 0311175   | nicolo.spadoni@students.uniroma2.eu   |         |          |           |                                       |

## Motivazioni

Il database che stiamo realizzando è incentrato all'implementazione di un software dedicato all'organizzazione di viaggi tramite taxi.

## Obiettivi

L'obiettivo principale di questo sistema è permettere agli utenti di organizzare gli spostamenti tramite Taxi a seconda della fascia oraria, del tipo di veicolo scelto e del costo della tratta scelta.

Da un punto di vista societario, gli obiettivi sono quelli di valutare la qualità del lavoro degli autisti tramite i feedback forniti dai clienti e migliorare dove possibile il servizio.



I DBA potranno effettuare modifiche al sistema.
Gli autisti potranno scegliere se accettare o rifiutare la corsa, specificando in questo caso la motivazione del rifiuto.

L'utente potrà interagire con il sistema per prenotare una corsa, aggiungere una tratta all'elenco dei preferiti, fornire un feedback sia positivo che negativo alla qualità del servizio.
Gli amministratori, accedendo ad un'area privata del sistema, potranno ricevere report degli utenti, ottimizzare il servizio (tempistiche, costi, ecc...) e in caso di guasti alle autovetture, contattare le officine del territorio per ordinare eventuali pezzi di ricambio.


## Analisi dei requisiti

I ruoli aziendali sono i seguenti: 
- Addetti Marketing
- Autisti
- Manutentori

Gli addetti al marketing possono inserire, previa autorizzazzione da parte degli amministratori della società, delle promo che prevedono sconti sulle corse per gli utenti del sistema

Gli autisti potranno scegliere se accettare o rifiutare la corsa, specificando in questo caso la motivazione del rifiuto.
Inoltre potranno lasciare un feedback all'utente riguardo il comportamento prima della corsa e durante la corsa.
Ogni autista ha la propria macchina privata, e può contattare i manutentori aziendali in caso di guasto del veicolo.

I manutentori possono ricevere richieste di assistenza da parte degli autisti e contattare le officine convenzionate per effettuare il lavoro di assistenza.
Le officine non fanno parte della società.

# Da completare

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

Ogni autista può guidare un singolo veicolo, per tutta la durata del turno lavorativo

Gli admin possono:
- Modificare i prezzi delle tratte base
- Visionare le tratte con maggior numero di prenotazioni
- Leggere i feedback lasciati al servizio, filtrandoli tramite nome autista
- In caso di necessità, contattare le officine del territorio per ordinare dei pezzi di ricambio per le autovetture

Per gli utenti sono state pensate le seguenti operazioni:
- Prenotare $n$ corse, ma con il vincolo di una corsa per volta
- Lasciare un feedback all'autista
- Aggiungere alla lista dei preferiti $n$ autisti e $k$ corse
- Accedere alla cronologia delle prenotazioni effettuate dal singolo utente
- Verificare se è possibile usufruire dello spazio adibito al bagaglio a mano/valigia o trasporto animale
- Verificare se un altro utente ha prenotato la stessa corsa e dividere il prezzo di quest'ultima

## Glossario

| Entità                 | Descrizione                                                       | Sinonimi            | Collegamenti                                                      |
| ---------------------- | ----------------------------------------------------------------- | ------------------- | ----------------------------------------------------------------- |
| DBA                    | DataBaseAdministrator                                             | Admin               | Personale, Addetti Marketing                                      |
| Personale              | Membri totali della società                                       | Organigramma        | DBA, Addetti Marketing, Manutentori, Autisti                      |
| Info Patente           | Descrive tutte le info riguardanti la patente degli autisti       | Licenza di Guida    | Autisti                                                           |
| Offerte                | Serie di offerte che vengono proposte al singolo utente           | Promozioni          | Utenti, Addetti Marketing                                         |
| Manutentori            | Addetti alla manutenzione delle auto degli autisti                | Meccanici, Operai   | Personale, Autisti                                                |
| Autisti                | Personale che svolge il ruolo di autista delle auto nella società | Driver              | Info Patente, Manutentori, Veicoli, Turni, Richiesta Prenotazione |
| Veicoli                | Auto utilizzate per il servizio di taxi                           | Automobili          | Autisti                                                           |
| Turni                  | Turni lavorativi che riguardano gli autisti                       | Orario Lavorativo   | Autisti                                                           |
| Richiesta Prenotazione | Richieste di prenotazioni effettuate da parte dall'utente         | Prenotazioni        | Autisti, Utenti, Tratte Complete, Tratte Rifiutate                |
| Utenti                 | Utenti utilizzatori del servizio taxi                             | Persone             | Carta, Richiesta Prenotazione, Offerte                            |
| Feedback               | Recensioni lasciate dall'utente e dagli autisti                   | Recensioni          | Tratte Completate                                                 |
| Tratte Completate      | Corse effettuate portate a termine con successo                   | Corse               | Richiesta Prenotazione, Feedback, Transazione                     |
| Tratte Rifiutate       | Corse rifiutate da parte dell'autista per determinati motivi      | Corse Annullate     | Richiesta Prenotazione                                            |
| Carta                  | Carta di credito personale dell'utente                            | Metodo di pagamento | Utenti, Transazione                                               |
| Transazione            | Transazione univoca del pagamento relativo alla singola corsa     | Pagamento           | Carta, Tratte Completate                                          |
| Addetti Marketing      | Personale addetto al reparto marketing della società              | Advertiser          | Offerte, Personale                                                |

# Schema E-R