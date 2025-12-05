import mysql.connector

# con = mysql.connector.connect(
#     host="localhost",
#     user="root",        
#     password="geleiadoce",
#     database="mercadinho"
# )

ps = "geleiadoce"

def login(a, s):
    con = mysql.connector.connect(
    host="localhost",
    user="root",
    password=ps,
    database="mercadinho"
    )
    cursor = con.cursor()
    comando = "SELECT nome, senha FROM users WHERE nome=%s AND senha=%s"
    cursor.execute(comando, (a, s))
    resultado = cursor.fetchone()
    cursor.close()
    con.close()


    return resultado

def search(id):
    con = mysql.connector.connect(
    host="localhost",
    user="root",
    password=ps,
    database="mercadinho"
    )
    cursor = con.cursor()
    comando = "SELECT Nome, Preco FROM produto WHERE idProduto=%s"
    cursor.execute(comando, (id, ))
    resultado = cursor.fetchall()
    cursor.close()
    con.close()

    return resultado


# if con.is_connected():
#     print("Conectado!")

# cursor = con.cursor()


def addprod(n, c, p):
    con = mysql.connector.connect(
    host="localhost",
    user="root",
    password=ps,
    database="mercadinho"
    )
    cursor = con.cursor()
    comando = "INSERT INTO produto (Nome, Categoria, Preco) VALUES (%s, %s, %s)"
    cursor.execute(comando, (n, c, p))
    con.commit()
    cursor.close()
    con.close()
    return "Salvo"

def addfunc(n, c, e, t):
    con = mysql.connector.connect(
    host="localhost",
    user="root",
    password=ps,
    database="mercadinho"
    )
    cursor = con.cursor()
    comando = "INSERT INTO funcionario (Nome, CPF, Endereco, Telefone) VALUES (%s, %s, %s, %s)"
    cursor.execute(comando, (n, c, e, t))
    con.commit()
    cursor.close()
    con.close()
    return "Salvo"

def seefunc():
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password=ps,
        database="mercadinho"
    )
    cursor = con.cursor(dictionary=True)
    cursor.execute("SELECT Nome, CPF, Endereco, Telefone FROM funcionario")
    resultados = cursor.fetchall()
    cursor.close()
    con.close()
    return resultados

def chang(n, e, t, c):
        con = mysql.connector.connect(
        host="localhost",
        user="root",
        password=ps,
        database="mercadinho"
        )
        cursor = con.cursor()
        comando = """
        UPDATE funcionario
        SET Nome=%s, Endereco=%s, Telefone=%s
        WHERE CPF=%s
        """
        cursor.execute(comando, (n, e, t, c))
        con.commit()
        cursor.close()
        con.close()

        return "Mudanças salvas"

def remov(cpf):
    con = mysql.connector.connect(
    host="localhost",
    user="root",
    password=ps,
    database="mercadinho"
    )
    cursor = con.cursor()
    comando = """DELETE FROM funcionario WHERE CPF=%s"""
    cursor.execute(comando, (cpf,))
    con.commit()
    cursor.close()
    con.close()

    return "Mudanças salvas"