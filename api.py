from fastapi import FastAPI
# import main
import banco as b
from pydantic import BaseModel

class funcionario(BaseModel):
    nome: str
    cpf: str
    endereco: str
    telefone: str


app = FastAPI()


# dados = main.us()

# users = []

# json


@app.post("/funcionarios")
def create(colab: funcionario):
    b.addfunc(colab.nome, colab.cpf, colab.endereco, colab.telefone)
    return {"mensagem": "Funcionário adicionado"}




@app.get("/funcionarios")
def read():
    return b.seefunc()
    

@app.put("/funcionarios/{cpf}")
def update(cpf: str, dados: funcionario):

    resultado = b.chang(dados.nome, dados.endereco, dados.telefone, cpf)
    return resultado

@app.delete("/funcionarios/{cpf}")
def delete(cpf: str):
    resultado = b.remov(cpf)
    return resultado

    

# DELETE FROM table_name WHEERE condition; 


# @app.post("/")
# def add_user(dados):
#     users.append(dados)
#     return users