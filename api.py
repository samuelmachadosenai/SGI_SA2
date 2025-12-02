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

colab_list = []

app = FastAPI()


# dados = main.us()

# users = []

# json


@app.post("/funcionarios")
def create(colab: funcionario):
    try:
        b.addfunc(colab.nome, colab.cpf, colab.endereco, colab.telefone)
        colab_list.append(colab.model_dump())
        return {"mensagem": "Funcionário adicionado"}
    except Exception as e:
        return {'erro': str(e)}



@app.get("/funcionarios")
def read():
    colab_list = b.seefunc()
    return colab_list



# @app.post("/")
# def add_user(dados):
#     users.append(dados)
#     return users


