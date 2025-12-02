import mysql.connector

# con = mysql.connector.connect(
#     host="localhost",
#     user="root",        
#     password="geleiadoce",
#     database="mercadinho"
# )

texto = "Salvo com sucesso!"

# if con.is_connected():
#     print("Conectado!")

# cursor = con.cursor()


 

def addfunc(n, c, e, t):
    con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="geleiadoce",
    database="mercadinho"
    )
    cursor = con.cursor()
    comando = "INSERT INTO funcionario (Nome, CPF, Endereco, Telefone) VALUES (%s, %s, %s, %s)"
    cursor.execute(comando, (n, c, e, t))
    con.commit()
    cursor.close()
    con.close()
    return "Salvo com sucesso!"

def seefunc():
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="geleiadoce",
        database="mercadinho"
    )
    cursor = con.cursor(dictionary=True)
    cursor.execute("SELECT Nome, CPF, Endereco, Telefone FROM funcionario")
    resultados = cursor.fetchall()
    cursor.close()
    con.close()
    return resultados