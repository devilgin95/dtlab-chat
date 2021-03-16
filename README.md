# DTLAB-CHAT
[WEEK 3] Applicazione per le lezioni degli studenti del Cisco DTLAB 2021 sui capitoli 5-6 del corso DEVASC.

## Descrizione
Utilizzando il web framework Flask, i file realizzano un semplice servizio REST con storage in memoria
di una web chat. Sono realizzate le seguenti funzionalità:
- signup e signin con email e password degli utenti;
- gli utenti possono inviare messaggi agli altri utenti identificati per email;

## ESERCIZIO 1.0
Creare una route '/login' che consenta agli utenti di effettuare il login con la fuzione Login del modulo user;

## ESERCIZIO 2.0
Creare un modulo 'message.py' con una funzione 'SaveMessage' che memorizza un messaggio.
In particolare, un messaggio deve contenere:
- mittente: id dell'utente che ha inviato il messaggio;
- destinatario: id dell'utente a cui è destinato il messaggio;
- contenuto: testo del messaggio;
Ragioniamo su altre informazioni che possono servire. Ad esempio:
- se volessi in futuro dare la possibilità di eliminare un messaggio inviato?
- se volessi mostrare i messaggi di una conversazione con quale ordine li mostrerei?

## ESERCIZIO 2.1
Creare una route che consenta agli utenti di visualizzare i messaggi ricevuti con un'apposita funzione nel modulo message;

## Esercizio 2.2
Aggiungere 2 route:
- DELETE /user/<id_utente>: l'utente invia email e password per cancellare il suo account:  
- GET /user/<id_utente>: l'utente invia email e password prende le informazioni memorizzate del suo account;

Esempio
- GET /user/123 -> informazioni utente con ID 123;
- DELETE /user/123 -> cancella utente con ID 123;

Per inviare una richiesta con autenticazione, bisogna utilizzare un "authorization header". Come abbiamo visto, gli header aggiungono ulteriori informazioni sul come trattare la richiesta; sottoforma di coppie chiave valore. Ad esempio:

**Content-Type: application/json**: indica di interpretare il contentuto del corpo della richiesta come json.

Utilizzando un Authorization header possiamo inviare informazioni per identificare l'utente nel sistema. Come visto in teoria ci sono diversi tipi di autorizzazione. Prova ad utilizzare la basic auth: inviamo username e password separati da ":" in base64;

Lato server, bisogna validare la richiesta verificando prima che le credenziali siano corrette e poi eseguire l'operazione. Se la convalida non va a buon fine, è buona norma ritornare "401 - Unauthorized". 

Domanda: come facciamo a passare alla callback l'id dell'utente che viene inviato dal client?

## Esercizio 3.1
Implementare un webhook per notificare un client che si sottoscrive per la ricezione di messaggi.
