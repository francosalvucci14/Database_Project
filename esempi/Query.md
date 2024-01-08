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


