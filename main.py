from fastapi import FastAPI
from langdetect import detect
from textblob import TextBlob


app = FastAPI()
utenti = []

@app.get("/")
def homepage():
    return "Ciao, questa è l'homepage"

@app.get("/ciao")
def homepage():
    return "Sono nel path ciao"

@app.get("/ciao")
def homepage(nome: str, eta: int):

    return "ciao" + nome


################ ESERCIZIO ###########################


@app.get("/hello")
def homepage():
    return "Hello World!"

@app.get("/datianagrafici")
def homepage(nome: str, cognome: str):


    return "Ciao " + nome + " "+ cognome + "!"



@app.post("/aggiungiutente")
def homepage(username: str):

   
    utenti.append(username)
    print(utenti)

    return "Utente aggiunto con successo"


@app.get("/cercautente")
def homepage(cerca_username: str):

   
    if cerca_username in utenti:
        print("Utente Trovato!")
    else:
        print("Utente non trovato!")


    return cerca_username



@app.get("/totaleutenti")
def homepage():

    totaleUtenti = len(utenti)


    return totaleUtenti


@app.get("/eliminautente")
def homepage(cancellaUtente: str):

    if cancellaUtente in utenti:
        utenti.remove(cancellaUtente)
    else: print("L'utente non è presente nella lista!")

    return


@app.get("/rilevaLingua")
def homepage(testo: str):

    lingua = detect(testo)

    return print(f"La lingua rilevata è: {lingua}")



@app.get("/sentimento")
def homepage(frase: str):

    
    blob = TextBlob(frase)
    sentiment = blob.sentiment.polarity
    return print(sentiment)

