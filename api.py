from fastapi import FastAPI
# import main
import banco as b
from pydantic import BaseModel


class Login(BaseModel):
    user: str
    senha: str


class funcionario(BaseModel):
    nome: str
    cpf: str
    endereco: str
    telefone: str


class produto(BaseModel):
    nome: str
    categoria: str
    preco: int





app = FastAPI()

@app.post("/produtos")
def create(prod: produto):
    b.addfunc(prod.nome, prod.categoria, prod.preco)
    return "Produto adicionado"


@app.get("/")
def home():
    return "hello world"

# dados = main.us()

# users = []

# json

@app.post("/login")
def entrar(login: Login):
    resultado = b.login(login.user, login.senha)

    if resultado is None:
        return {"Login": False, "mensagem": "Usuário ou senha incorretos"}
    else:
        return {"Login": True, "mensagem": "Login bem sucedido!"}

    



@app.post("/funcionarios")
def create(colab: funcionario):
    b.addfunc(colab.nome, colab.cpf, colab.endereco, colab.telefone)
    return "Funcionário adicionado"




@app.get("/funcionarios")
def read():
    return b.seefunc()
    

@app.put("/funcionarios/{cpf}")
def update(cpf: str, dados: funcionario):

    resultado = b.chang(dados.nome, dados.endereco, dados.telefone, cpf)
    return {"mensagem": "Dados atualizado"}

@app.delete("/funcionarios/{cpf}")
def delete(cpf: str):
    resultado = b.remov(cpf)
    return {"mensagem": "Dados salvos"}

    

# DELETE FROM table_name WHEERE condition; 


# @app.post("/")
# def add_user(dados):
#     users.append(dados)
#     return users