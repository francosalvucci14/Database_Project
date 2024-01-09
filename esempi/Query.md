- Visualizza tutte i viaggi effettutati in un mese
	- SELECT  * FROM TratteCompletate WHERE MONTH(Data) = 'mese';
- Visualizza la media delle valutazioni di un dato conducente
	- SELECT AVG(StelleAutista) FROM Feedback ;
- Recupera i viaggi effettuati durante le ore di punta
	- SELECT * FROM RichiestaPrenotazioni WHERE HOUR(OrarioRichiesta) BETWEEN 7 AND 9 OR HOUR(OrarioRichiesta) BETWEEN 17 AND 19;
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

SELECT Targa, Modello, Marca, a2.DataScadenza AS DataScadenza FROM Veicoli v LEFT JOIN Assicurazione a2

ON v.Assicurazione = a2.ID_Assicurazione

WHERE YEAR (a2.DataScadenza) = "2024";

- Visualizza i turni di un dato autista

SELECT p.Nome, p.Cognome, t.OrarioInizio, t.OrarioFine FROM Autisti a JOIN Personale p

ON a.ID_Autista = p.ID

JOIN Turni t ON a.Turno = t.ID_Turno

WHERE p.Nome = "Raffaello" AND p.Cognome = "Costanzi";

- Visualizza tutti gli autisti hanno le stesso turno

SELECT p.Nome, p.Cognome, a.Turno, a.ID_Autista FROM Autisti a JOIN Personale p

ON a.ID_Autista = p.ID

JOIN Turni t ON a.Turno = t.ID_Turno

WHERE a.Turno = 2

- Visualizza la somma dei pagamenti effettuati dagli utenti in una data settimana

SELECT SUM(tc.Costo) AS Totale FROM TratteCompletate tc

JOIN RichiestePrenotazioni rp ON tc.ID_TrattaC = rp.ID_Richiesta

WHERE MONTH (rp.DataRichiesta) = "06"

AND DAY (rp.DataRichiesta) BETWEEN 1 AND 7

- Visualizza tutte le richieste di manutenzione relative ad uno specifico veicolo

SELECT cpg.Motivo, v.* FROM ContattaPerGuasto cpg

JOIN Autisti a ON cpg.ID_Autista = a.ID_Autista

JOIN Veicoli v ON a.Targa = v.Targa

WHERE v.Targa = "CO020CO";

- Visualizza tutte le tratte più gettonate

SELECT PuntoDiRaccolta, PuntoDiRilascio, COUNT(*) AS NumeroRichieste

FROM RichiestePrenotazioni rp

GROUP BY PuntoDiRaccolta, PuntoDiRilascio

ORDER BY NumeroRichieste DESC

LIMIT 10;

