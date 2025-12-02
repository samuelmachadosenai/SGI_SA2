import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",   
    password="geleiadoce",
    database="mercadinho"
)

texto = "Salvo com sucesso!"

if con.is_connected():
    print("Conectado!")

cursor = con.cursor()


 

def func(n, c, e, t):
    comando = """INSERT INTO funcionario (Nome, CPF, Endereco, Telefone) VALUES (%s, %s, %s, %s)"""

    cursor.execute(comando, (n, c, e, t))
    con.commit()
    con.close()
    return texto