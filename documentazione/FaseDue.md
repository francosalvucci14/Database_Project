
# Indice degli argomenti

- Nome progetto
- Fase concettuale
- Schemi

# Intro al progetto

## Nome progetto

La nostra socità si chiama **VRoomA**
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
| Autisti | Personale che svolge il ruolo di autista delle auto nella società | **ID** | Patente, Manutentori, Veicoli, Turni, Richiesta Prenotazione, Personale, Feedback |
| Veicoli | Auto utilizzate per il servizio di taxi | **Targa**, Marca, Modello, Posti disponibili | Autisti, Assicurazione |
| Turni | Turni lavorativi che riguardano gli autisti | **ID**, Orario inizio, Orario fine | Autisti |
| Richiesta Prenotazione | Richieste di prenotazioni effettuate da parte dall'utente | **ID**, Punto di raccolta, Punto di rilascio, Orario richiesta, Numero Passeggeri | Autisti, Utenti, Tratte Complete, Tratte Rifiutate |
| Utenti | Utenti utilizzatori del servizio taxi | **ID**, Nome, Cognome, Email, Password, Abbonamento | Carta, Richiesta Prenotazione, Offerte, Feedback, Tratte completate |
| Feedback | Recensioni lasciate dall'utente e dagli autisti | **ID**, Stelle, Commento, Data | Tratte Completate, Utenti, Autisti |
| Tratte Completate | Corse effettuate portate a termine con successo | **ID**, Costo | Richiesta Prenotazione, Feedback, Carta, Utenti |
| Tratte Rifiutate | Corse rifiutate da parte dell'autista per determinati motivi | **ID**, Motivazione | Richiesta Prenotazione |
| Carta | Carta di credito personale dell'utente | **Numero Carta**, Data di Scadenza, CVV | Utenti, Tratte completate |
| Assicurazione | Dati dell'assicurazione associata al singolo veicolo | **ID**, Data di scandenza, Tipo | Veicoli |
| Addetti Marketing | Personale addetto al reparto marketing della società | **ID** | Offerte, Personale |

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
| Lista Preferiti | Lista delle tratte impostate dall'utente come preferite | Preferenze |  |

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
| UtenteHaOfferta              | Relazione che dice che ogni utente può avere (non necessariamente) una o più offerte attive                                                     | Utenti (1,N), Offerte (0,1)                 |
| UtentePossiedeCarta          | Relazione che dice che ogni utente deve possedere almeno una carta con cui effettuare i pagamenti                                               | Utenti (1,N), Carta (1,1)                   |
| EffettuaPrenotazione         | Relazione che dice che ogni utente effettua una o più prenotazioni                                                                              | Utenti (1,N), Richiesta Prenotazioni (1,1)  |
| UtenteLasciaFeedback         | Relazione che dice che ogni utente può lasciare uno o più feedback relativi alle corse da lui effettuate                                        | Utenti (1,N), Feedback (1,1)                |
| CartaPagaTratta              | Relazione che dice che ogni utente, tramite la propria carta, deve pagare le tratte da lui effettuate                                           | Carta (1,N), Tratte Completate (1,1)        |
| ListaPreferiti               | Relazione che dice che ogni utente può impostare la propria lista dei preferiti per quanto riguarda le tratte completate e gli autisti          | Utenti (1,N), Tratte Completate (1,N)       |
| TrattaAvereFeedback             | Relazione che dice che ogni tratta completata può avere (non necessariamente) un solo feedback, che viene lasciato dagli utenti e dagli autisti | Tratte Completate (0,1), Feedback (1,1)     |

## Schemi

### Schemi di relazione

Le chiave primarie sono identificate in **grassetto**, mentre le chiavi secondarie (o esterne) sono identificate tramite la _sottolineatura_

Forse da aggiungere
### Schema Logico Normalizzato

Mettere schema ER logico derivato dallo schema Fisico normalizzato

### Diagramma Entity-Relationship (Schema Fisico)

Le entità padre si distinguono dalle entità figlio perchè sono rappresentate con il doppio cerchio.

Lo schema risulta già normalizzato in 3NF, e di conseguenza già in 2NF e 1NF.

![[Schema-Fisico-Restyle.jpg|center]]


