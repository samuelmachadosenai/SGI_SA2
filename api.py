from fastapi import FastAPI

app = FastAPI()


# json

@app.get("/produtos")
def home():
    return "O amor é lindo."


