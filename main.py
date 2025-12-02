import os
import keyboard as k
import rand as r



def vanish():
    os.system("cls")

def pagar():
    print("aaaaa")

venda = []

def scan():
    a = 0
    while True:

        print("Escaneie o produto:\n")
       
    
        while True:
            if k.is_pressed("a") == True:
                k.wait("a")
                nome, preco = r.prod()

                tupla = (nome, preco)
                venda.append(tupla)
                # preco = produto['preço']


                for i in venda:
                    a += 1

                    print(f"{a}. {i}")
   
        


        print("\n\n1. Finalizar compra")
        if k.read_key() == "1":
            break

        break
                






        
        

def menu():
    while True:
        print("-"*10, "Caixa", "-"*10)
        print("\n")

        while True:
            print("""1. Cadastrar produto""")
            opt = int(input())

            if opt == 1:
                scan()
                break
        break

menu()
pagar()


