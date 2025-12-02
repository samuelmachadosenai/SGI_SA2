from fastapi import FastAPI
import main



app = FastAPI()


dados = main.us()

users = []

# json

@app.get("/")
def home():
    return "Olá mundo"

@app.post("/")
def add_user(dados):
    users.append(dados)
    return users


