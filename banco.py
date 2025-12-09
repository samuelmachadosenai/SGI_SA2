import mysql.connector

# con = mysql.connector.connect(
#     host="localhost",
#     user="root",        
#     password="geleiadoce",
#     database="mercadinho"
# )

# ps = "geleiadoce"
u = "root"

# def login(a, s):
#     con = mysql.connector.connect(
#     host="localhost",
#     user=u,
#     # password=ps,
#     database="mercadinho"
#     )
#     cursor = con.cursor()
#     comando = "SELECT nome, senha FROM users WHERE nome=%s AND senha=%s"
#     cursor.execute(comando, (a, s))
#     resultado = cursor.fetchone()
#     cursor.close()
#     con.close()


#     return resultado

# def venda():
#     con = mysql.connector.connect(
#     host="localhost",
#     user=u,
#     password=ps,
#     database="mercadinho"
#     )

#     cursor = con.cursor()
#     comando = "INSERT INTO vendas (Nome, idDepartamento, Preco) VALUES (%s, %s, %s)"
#     cursor.execute(comando, (id, ))
#     resultado = cursor.fetchall()
#     cursor.close()
#     con.close()

     
     

def search(id):
    con = mysql.connector.connect(
    host="localhost",
    user=u,
    # password=ps,
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


def addprod(n, c, p, qt):
    con = mysql.connector.connect(
    host="localhost",
    user=u,
    # password=ps,
    database="mercadinho"
    )
    cursor = con.cursor()
    comando = "INSERT INTO produto (Nome, Categoria, Preco, Quantidade) VALUES (%s, %s, %s, %s)"
    cursor.execute(comando, (n, c, p, qt))
    con.commit()
    cursor.close()
    con.close()
    return "Salvo"

def addfunc(n, c, ca, e, t):
    con = mysql.connector.connect(
    host="localhost",
    user=u,
    # password=ps,
    database="mercadinho"
    )
    cursor = con.cursor()
    comando = "INSERT INTO funcionario (Nome, CPF, Cargo, Endereco, Telefone) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(comando, (n, c, ca, e, t))
    con.commit()
    cursor.close()
    con.close()
    return "Salvo"

def seefunc():
    con = mysql.connector.connect(
        host="localhost",
        user=u,
        # password=ps,
        database="mercadinho"
    )
    cursor = con.cursor(dictionary=True)
    cursor.execute("SELECT Nome, CPF, Cargo, Endereco, Telefone FROM funcionario")
    resultados = cursor.fetchall()
    cursor.close()
    con.close()
    return resultados

def seeprod():
    con = mysql.connector.connect(
        host="localhost",
        user=u,
        # password=ps,
        database="mercadinho"
    )
    cursor = con.cursor(dictionary=True)
    cursor.execute("SELECT Nome, Categoria, Preco, Quantidade FROM produto")
    resultados = cursor.fetchall()
    cursor.close()
    con.close()
    return resultados
     

def chang(n, ca, e, t, c):
        con = mysql.connector.connect(
        user=u,
        host="localhost",
        # password=ps,
        database="mercadinho"
        )
        cursor = con.cursor()
        comando = """
        UPDATE funcionario
        SET Nome=%s, Cargo=%s, Endereco=%s, Telefone=%s
        WHERE CPF=%s
        """
        cursor.execute(comando, (n, ca, e, t, c))
        con.commit()
        cursor.close()
        con.close()

        return "Mudanças salvas"

def remov(cpf):
    con = mysql.connector.connect(
    host="localhost",
    user=u,
    # password=ps,
    database="mercadinho"
    )
    cursor = con.cursor()
    comando = """DELETE FROM funcionario WHERE CPF=%s"""
    cursor.execute(comando, (cpf,))
    con.commit()
    cursor.close()
    con.close()

    return "Mudanças salvas"

#  File "C:\Users\samuel\OneDrive\Documentos\GitHub\SGI_SA2\api.py", line 61, in listagem
#     result = b.search(i)
#              ^^^^^^^^^^^
#   File "C:\Users\samuel\OneDrive\Documentos\GitHub\SGI_SA2\banco.py", line 31, in search
#     con = mysql.connector.connect(
#           ^^^^^^^^^^^^^^^^^^^^^^^^