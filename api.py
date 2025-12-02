from fastapi import FastAPI
# import main
import banco as b
from pydantic import BaseModel

class funcionario(BaseModel):
    nome: str
    cpf: str
    endereco: str
    telefone: str

colab = [
    {
        'nome': 'Açucena Pereira',
        'cpf': '123.456.789-09',
        'endereco': 'Rua da Alegria',
        'telefone': '(47) 99505-0565'
    }
]


app = FastAPI()


# dados = main.us()

# users = []

# json

@app.get("/funcionarios")
def listar_funcionarios():
    return colab

@app.post("/funcionarios")
def ver_funcionario(colab: funcionario):
    b.func(colab.nome, colab.cpf, colab.endereco, colab.telefone)
    return {"mensagem": "Funcionário adicionado"}



# @app.post("/")
# def add_user(dados):
#     users.append(dados)
#     return users


