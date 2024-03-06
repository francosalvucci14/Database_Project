- Visualizza tutte i viaggi effettutati in un mese
	- `SELECT  * FROM TratteCompletate WHERE MONTH(Data) = 'mese';`
- Visualizza la media delle valutazioni di un dato conducente
	- `SELECT AVG(StelleAutista) FROM Feedback ;`
- Recupera i viaggi effettuati durante le ore di punta
	- `SELECT * FROM RichiestaPrenotazioni WHERE HOUR(OrarioRichiesta) BETWEEN 7 AND 9 OR HOUR(OrarioRichiesta) BETWEEN 17 AND 19;`
- Visualizza i viaggi con feedback positivi
	- SELECT * FROM TratteCompletate WHERE Feedback LIKE '....';
Visualizza tutte le assicurazioni scadute

Visualizza tutti gli autisti che hanno una certa categoria di patente

Visualizza tutte le richieste di manutenzione effettuate per un veicolo

Visualizza i turni di un dato autista 

Visualizza tutti gli utenti che hanno un abbonamento annuale

Visualizza le auto con un numero di posti superiori a un certo numero

Visualizza i/il passeggeri/o che hanno/ha effettuato il maggior numero di viaggi

Calcola il guadagno sulle corse in una data settimana

# Query Usate

- Visualizza tutti i veicoli la cui assicurazione scadrà entro il 2024
```SQL
SELECT Targa, Modello, Marca, a2.DataScadenza AS DataScadenza FROM Veicoli v LEFT JOIN Assicurazione a2
ON v.Assicurazione = a2.ID_Assicurazione
WHERE YEAR (a2.DataScadenza) = "2024";
```
- Visualizza i turni di un dato autista
``` sql
SELECT p.Nome, p.Cognome, t.OrarioInizio, t.OrarioFine FROM Autisti a JOIN Personale p
ON a.ID_Autista = p.ID
JOIN Turni t ON a.Turno = t.ID_Turno
WHERE p.Nome = "Raffaello" AND p.Cognome = "Costanzi";
```
- Visualizza tutti gli autisti hanno le stesso turno
```SQL
SELECT p.Nome, p.Cognome, a.Turno, a.ID_Autista FROM Autisti a JOIN Personale p
ON a.ID_Autista = p.ID
JOIN Turni t ON a.Turno = t.ID_Turno
WHERE a.Turno = 2
```
- Visualizza la somma dei pagamenti effettuati dagli utenti in una data settimana
```SQL
SELECT SUM(tc.Costo) AS Totale FROM TratteCompletate tc
JOIN RichiestePrenotazioni rp ON tc.ID_TrattaC = rp.ID_Richiesta
WHERE MONTH (rp.DataRichiesta) = "06"
AND DAY (rp.DataRichiesta) BETWEEN 1 AND 7
```
- Visualizza tutte le richieste di manutenzione relative ad uno specifico veicolo
```SQL
SELECT cpg.Motivo, v.* FROM ContattaPerGuasto cpg
JOIN Autisti a ON cpg.ID_Autista = a.ID_Autista
JOIN Veicoli v ON a.Targa = v.Targa
WHERE v.Targa = "CO020CO";
```
- Visualizza tutte le tratte più gettonate
```SQL
SELECT PuntoDiRaccolta, PuntoDiRilascio, COUNT(*) AS NumeroRichieste
FROM RichiestePrenotazioni rp
GROUP BY PuntoDiRaccolta, PuntoDiRilascio
ORDER BY NumeroRichieste DESC
LIMIT 10;
```
- Visualizza gli utenti che hanno effettuato almeno 10 richieste
```SQL
SELECT u.ID_Utente, u.Nome, u.Cognome, COUNT(*) AS NumeroRichieste
FROM RichiestePrenotazioni rp JOIN Utenti u ON rp.ID_Utente = u.ID_Utente
GROUP By u.ID_Utente, u.Nome, u.Cognome
HAVING NumeroRichieste >= 10
ORDER BY NumeroRichieste DESC;
```
-  Di un dato range di utenti (ID compreso tra 2000 e 6000 e l'iniziale del nome "F"), visualizza le offerte associate e la sua descrizione
```SQL
SELECT u.ID_Utente, u.Nome, u.Cognome, o.ID_Offerta, o.InfoOfferta
FROM Utenti u JOIN Offerte o ON u.ID_Offerta = o.ID_Offerta
WHERE u.ID_Utente
IN(SELECT ID_Utente FROM Utenti u2 WHERE ID_Utente BETWEEN 2000 AND 6000 AND Nome LIKE "F%")
```
- Visualizza il motivo del rifiuto della richiesta di prenotazione più riccorrente
```SQL
SELECT tr.Motivazione, COUNT(*) AS NumeroOccorrenze
FROM TratteRifiutate tr GROUP BY tr.Motivazione
ORDER BY NumeroOccorrenze DESC
LIMIT 1;
```
-  Di tutti gli autisti che hanno un ID compreso tra 50 e 400, mostra il turno assegnato e i dati del veicolo che utilizzano
```SQL
SELECT a.ID_Autista, p.Nome, p.Cognome, t.*, v.*
FROM Autisti a JOIN Personale p ON a.ID_Autista = p.ID
JOIN Veicoli v ON a.Targa = v.Targa
JOIN Turni t ON a.Turno = t.ID_Turno
WHERE ID_Autista BETWEEN 50 AND 400;
```
- Visualizza tutte le tratte completate che non hanno un feedback
```SQL
SELECT tc.* FROM TratteCompletate tc 
WHERE tc.ID_TrattaC NOT IN 
(
	SELECT ID_TrattaCompletata FROM Feedback f
);
```
- Visualizza tutte le richieste di prenotazioni effettuate da un singolo utente
```SQL
SELECT rp.* FROM RichiestePrenotazioni rp JOIN Utenti u
ON rp.ID_Utente = u.ID_Utente 
WHERE u.Nome = 'Carla' AND u.Congome = 'Raimondi'
```
- Visualizza la media delle stelle ottenute da un singolo autista
```SQL
SELECT p.Nome, p.Cognome, AVG(f.StelleUtente) AS MediaStelle FROM Feedback f JOIN TratteCompletate tc
ON f.ID_TrattaCompletata = tc.ID_TrattaC
JOIN RichiestePrenotazioni rp ON tc.ID_TrattaC = rp.ID_Richiesta
JOIN Autisti a ON rp.ID_Autista = a.ID_Autista
JOIN Personale p ON a.ID_Autista = p.ID
WHERE rp.ID_Autista = "500"
GROUP BY p.Nome, p.Cognome
ORDER BY MediaStelle DESC
```
- Visualizza la spesa totale di un singolo utente
```SQL
SELECT u.Nome, u.Cognome, SUM(tc.Costo) AS SpesaTotale
FROM TratteCompletate tc JOIN RichiestePrenotazioni rp
ON tc.ID_TrattaC = rp.ID_Richiesta
JOIN Utenti u ON rp.ID_Utente = u.ID_Utente
WHERE u.ID_Utente = "1"
GROUP BY u.Nome, u.Cognome
ORDER BY SpesaTotale
```
- Visualizza il numero totale delle assicurazioni kasko
```SQL
SELECT COUNT(a.Tipo) AS TotaleKasko
FROM Assicurazioni a
WHERE a.Tipo = "Kasko"
```
- Visualizza tutti gli autisti che hanno una certa categoria di patente
```SQL
SELECT p.Nome, p.Cognome, pt.Categoria
FROM Personale p JOIN Autisti a ON p.ID = a.ID_Autista
JOIN Patente pt ON pt.NumeroPatente = a.NumeroPatente
WHERE pt.Categoria = "B96"
```
- Visualizza il numero di utenti che hanno lasciato almeno 3 stelle di valutazione nei feedback
```SQL

```

# Nuove Query 

Visualizza tutte le tratte completate, il costo e il metodo di pagamento di un determinato utente
```
SELECT tc.Partenza, tc.Arrivo, tc.Costo, tc.MetodoDiPagamento FROM TratteCompletate tc
JOIN Utenti u ON tc.ID_Utente = u.ID_Utente 
WHERE u.Nome = 'Nino' AND u.Cognome = 'Pausini'
```
Visualizza i veicoli la cui assicurazione scadrà nel mese di febbraio e i dati del proprietario
```
SELECT v.Targa, Modello, Marca, a.DDS  AS DataScadenza, au.Nome, au.Cognome FROM Veicoli v 
JOIN Assicurazioni a ON v.Targa  = a.Targa  
JOIN Autisti au ON au.Matricola = v.Matricola 
WHERE YEAR(a.DDS) = "2024" AND MONTH(a.DDS) = "02";
```
Visualizza tutti i turni lavorati da un dato autista 
```
SELECT tol.Data, tol.OraInizio, tol.OraFine FROM Autisti a JOIN TabellaOrarioLavorativo tol 
ON a.Matricola  = tol.Matricola 
WHERE a.Nome = "Silvia" AND a.Cognome = "Saffi"
ORDER BY tol.Data;
```

