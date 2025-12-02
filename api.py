from fastapi import FastAPI
import main
import banco as b

colab = [
    {
        'nome': 'Açucena Pereira',
        'cpf': '123.456.789-09',
        'endereço': 'Rua da Alegria',
        'telefone': '(47) 99505-0565'
    }
]


app = FastAPI()


# dados = main.us()

users = []

# json

@app.get("/")
def home():
    return colab

@app.post("/funcionarios")
def ver_funcionario():
    nome = colab['nome']
    cpf = colab['cpf']
    end = colab['endereço']
    tel = colab['telefone']

    b.func(nome, cpf, end, tel)




    colab

# @app.post("/")
# def add_user(dados):
#     users.append(dados)
#     return users


