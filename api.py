from fastapi import FastAPI
# import main
import banco as b
from pydantic import BaseModel
import resto as r


# class Login(BaseModel):
#     user: str
#     senha: str


class funcionario(BaseModel):
    nome: str
    cpf: str
    cargo: str
    endereco: str
    telefone: str


class produto(BaseModel):
    nome: str
    categoria: str
    preco: int
    quantidade: int

class Item(BaseModel):
    id_item: int

ativo = None
    

app = FastAPI()


# removido
# @app.post("/login")
# def entrar(login: Login):
#     global ativo
#     resultado = b.login(login.user, login.senha)

#     if resultado is None:
#         return {"Login": False, "mensagem": "Usuário ou senha incorretos"}
#     else:
#         return {"Login": True, "mensagem": "Login bem sucedido!"}




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
    b.addprod(prod.nome, prod.categoria, prod.preco, prod.quantidade)
    return "Produto adicionado"

@app.get("/produtos")
def read():
    return b.seeprod()

@app.get("/")
def home():
    return "hello world"

# # dados = main.us()

# # users = []

# # json



    



@app.post("/funcionarios")
def create(colab: funcionario):
    nome = colab.nome
    cpf = colab.cpf 
    cargo = colab.cargo
    end = colab.endereco
    tel = colab.telefone

    nome = r.nome(nome)


    if nome == False:
        return "Nome inválido"
    if r.checkcpf(cpf) == False:
        return "CPF inválido."
    if len(tel) > 10:
        return "Telefone inválido."
    
    b.addfunc(nome, cpf, cargo, end, tel)
    return "Funcionário adicionado"




@app.get("/funcionarios")
def read():
    return b.seefunc()
    

@app.put("/funcionarios/{cpf}")
def update(cpf: str, dados: funcionario):
    b.chang(dados.nome, dados.cargo, dados.endereco, dados.telefone, cpf)
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