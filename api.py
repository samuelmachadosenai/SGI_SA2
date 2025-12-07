from fastapi import FastAPI
# import main
import banco as b
from pydantic import BaseModel
import resto as r


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
    departamento: str
    preco: int

class Item(BaseModel):
    id_item: int


    


app = FastAPI()

@app.post("/login")
def entrar(login: Login):
    resultado = b.login(login.user, login.senha)

    if resultado is None:
        return {"Login": False, "mensagem": "Usuário ou senha incorretos"}
    else:
        return {"Login": True, "mensagem": "Login bem sucedido!"}



items = []

@app.post("/caixacompra")
def compra(item: Item):
    items.append(item.id_item)
    return items


lista = []

@app.get("/caixacompralista")
def listagem():
    global lista
    lista = []
   
    for i in items:
        result = b.search(i)
        if result == None:
            return "erro"
        
        nome = result[0][0]
        preco = result[0][1]

        d = {
        'nome': nome,
        'preco': preco}

        lista.append(d)  


     
        # r.append(result.__dict__)
    
    return lista

@app.post("/confirmarcompra")
def comprar():

    total = 0
    for i in lista:
        preco = int(i['preco'])
        total += preco

    
    return {'total': total, 'itens': lista}




@app.post("/produtos")
def create(prod: produto):
    b.addprod(prod.nome, prod.departamento, prod.preco)
    return "Produto adicionado"


@app.get("/")
def home():
    return "hello world"

# dados = main.us()

# users = []

# json



    



@app.post("/funcionarios")
def create(colab: funcionario):
    nome = colab.nome
    cpf = colab.cpf 
    end = colab.endereco
    tel = colab.telefone

    nome = r.nome(nome)

    if nome == False:
        return "Nome inválido"

    if r.checkcpf(cpf) == False:
        return "CPF inválido."
    
    b.addfunc(nome, cpf, end, tel)
    return "Funcionário adicionado"




@app.get("/funcionarios")
def read():
    return b.seefunc()
    

@app.put("/funcionarios/{cpf}")
def update(cpf: str, dados: funcionario):

    b.chang(dados.nome, dados.endereco, dados.telefone, cpf)
    return {"mensagem": "Dados atualizados"}

@app.delete("/funcionarios/{cpf}")
def delete(cpf: str):
    b.remov(cpf)
    return {"mensagem": "Dados salvos"}

    

# DELETE FROM table_name WHEERE condition; 


# @app.post("/")
# def add_user(dados):
#     users.append(dados)
#     return users