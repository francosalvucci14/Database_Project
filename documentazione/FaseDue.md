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

I **ruoli aziendali** sono i seguenti: 
- Addetti Marketing
- Autisti
- Manutentori

Gli **addetti al marketing** possono inserire, previa autorizzazzione da parte degli amministratori della società, delle **promo** che prevedono sconti sulle corse per gli utenti del sistema.

Gli **autisti** potranno scegliere se accettare o rifiutare la corsa, specificando in questo caso la motivazione del rifiuto.
Inoltre potranno lasciare un **feedback** all'utente riguardo il comportamento prima e durante la corsa.
Ogni **autista** ha la propria macchina privata, e può contattare i manutentori aziendali in caso di guasto del veicolo.
Ad ogni **autista** è assegnato un turno di lavoro di massimo 8 ore giornaliere.

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
Ogni **prenotazione** può essere accettata o rifiutata in base a determinati eventi dall'**autista**.
Ad ogni tratta completata è associato un feedback che può essere lasciato sia dall'**utente** che dall'**autista**.

Ogni **utente** ha diritto a ricevere **offerte** da poter usare al momento della prenotazione.
Può effettuare illimitate richieste di **prenotazione**, in base alle necessità personali (numero di passeggeri, persone con disabilità, punto di ritiro, punto di rilascio), con il vincolo di una corsa per volta.
A corsa completata l'**utente** può lasciare un **feedback** con un numero di stelle (da 1 a 5) e un commento.
Ogni **utente** deve aggiungere almeno una **carta** con cui effettuare il pagamento relativo alla tratta effettuata.
Ogni **utente** può aggiungere alla lista dei preferiti ua qualunque delle tratte effettuate da lui, scegliendo se aggiungere solo la tratta o anche l'autista.
Ogni **utente** può accedere alla cronologia delle prenotazioni effettuate.


## Glossario

| Entità                 | Descrizione                                                       | Sinonimi                  | Collegamenti                                                                      |
| ---------------------- | ----------------------------------------------------------------- | ------------------------- | --------------------------------------------------------------------------------- |
| Personale              | Membri totali della società                                       | Organigramma              | Addetti Marketing, Manutentori, Autisti                                           |
| Patente                | Descrive tutte le info riguardanti la patente degli autisti       | Licenza di Guida          | Autisti                                                                           |
| Offerte                | Serie di offerte che vengono proposte al singolo utente           | Promozioni                | Utenti, Addetti Marketing                                                         |
| Manutentori            | Addetti alla manutenzione delle auto degli autisti                | Meccanici, Operai         | Personale, Autisti                                                                |
| Autisti                | Personale che svolge il ruolo di autista delle auto nella società | Driver                    | Patente, Manutentori, Veicoli, Turni, Richiesta Prenotazione, Personale, Feedback |
| Veicoli                | Auto utilizzate per il servizio di taxi                           | Automobili                | Autisti, Assicurazione                                                            |
| Turni                  | Turni lavorativi che riguardano gli autisti                       | Orario Lavorativo         | Autisti                                                                           |
| Richiesta Prenotazione | Richieste di prenotazioni effettuate da parte dall'utente         | Prenotazioni              | Autisti, Utenti, Tratte Complete, Tratte Rifiutate                                |
| Utenti                 | Utenti utilizzatori del servizio taxi                             | Persone                   | Carta, Richiesta Prenotazione, Offerte, Feedback, Tratte completate               |
| Feedback               | Recensioni lasciate dall'utente e dagli autisti                   | Recensioni                | Tratte Completate, Utenti, Autisti                                                |
| Tratte Completate      | Corse effettuate portate a termine con successo                   | Corse                     | Richiesta Prenotazione, Feedback, Carta, Utenti                                   |
| Tratte Rifiutate       | Corse rifiutate da parte dell'autista per determinati motivi      | Corse Annullate           | Richiesta Prenotazione                                                            |
| Carta                  | Carta di credito personale dell'utente                            | Metodo di pagamento       | Utenti, Tratte completate                                                         |
| Assicurazione          | Dati dell'assicurazione associata al singolo veicolo              | RCA, Polizza assicurativa | Veicoli                                                                           |
| Addetti Marketing      | Personale addetto al reparto marketing della società              | Advertiser                | Offerte, Personale                                                                |
| Lista Preferiti        | Lista delle tratte impostate dall'utente come preferite           | Preferenze                | Utenti, Tratte completate                                                                                  |

# Schema E-R

## Schema E-R Fisico

Le entità padre si distinguono dalle entità figlio perchè sono rappresentate con il doppio cerchio

![[Schema-Fisico.jpg|center]]
