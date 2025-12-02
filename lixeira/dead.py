import os
import keyboard as k
import rand as r



def vanish():
    os.system("cls")

def pagar():
    print("aaaaa")

# def key(key):
#     while True:  # making a loop
#         try:  # used try so that if user pressed other than the given key error will not be shown
#             if k.is_pressed(key):  # if key 'q' is pressed 
#                 return True
#         except:
#             break  # if user pressed a key other than the given key the loop will break

venda = []
total = 0
a = 0

def scan():
   

    while True:

        vanish()
        print("Escaneie o produto:\n")

     

        while True:

                if k.read_key() == 'a':
            
                    nome, preco = r.prod()


                    

                    tupla = (nome, preco)
                  
                    venda.append(tupla)
                    # preco = produto['preço']

                    
                    global total 
                    total += preco

            
                    for i in venda:
                        
                        preco = i[1]

                        global a 
                        a += 1

                        print(f"{a}. {i}")
                        print(preco)
                        print(total)
                        # print(len(tupla))
                        # print(indic)
    
                
                # print("-"*20)
        


                    






        
        

def menu():
    while True:
        print("-"*10, "Caixa", "-"*10)
        print("\n")

        while True:
            print("""1. Cadastrar produto""")
            opt = int(input())

            if opt == 1:
                scan()
                print("Finalizar compra")
                break
        break

menu()
pagar()


