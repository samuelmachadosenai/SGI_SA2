def checkcpf(cpf_str):
    while True:
        cpf_str = cpf_str.strip()
        cpf_str = cpf_str.replace(".", "")
        cpf_str = cpf_str.replace("-", "")

        quant = len(cpf_str)
        #123234345
        # lista = []
        cont = 0

        if quant < 11 or quant > 11 or cpf_str.isalpha == True:
            return False
        
        else:
            while True:
                n1 = int(cpf_str[0])
                n2 = int(cpf_str[1])
                n3 = int(cpf_str[2])
                n4 = int(cpf_str[3])
                n5 = int(cpf_str[4])
                n6 = int(cpf_str[5])
                n7 = int(cpf_str[6])
                n8 = int(cpf_str[7])
                n9 = int(cpf_str[8])

                n1 *= 1
                n2 *= 2
                n3 *= 3
                n4 *= 4
                n5 *= 5
                n6 *= 6
                n7 *= 7
                n8 *= 8
                n9 *= 9

                numero_final = n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8 + n9
                num_top = numero_final % 11

                num_a = str(num_top)

                num_b = num_a[-1]

                strong = cpf_str + num_b

                # __________________________________________

                nn1 = int(strong[0])
                nn2 = int(strong[1])
                nn3 = int(strong[2])
                nn4 = int(strong[3])
                nn5 = int(strong[4])
                nn6 = int(strong[5])
                nn7 = int(strong[6])
                nn8 = int(strong[7])
                nn9 = int(strong[8])
                nn10 = int(strong[9])

                nn1 *= 0
                nn2 *= 1
                nn3 *= 2
                nn4 *= 3
                nn5 *= 4
                nn6 *= 5
                nn7 *= 6
                nn8 *= 7
                nn9 *= 8
                nn10 *= 9

                numero_final2 = nn1 + nn2 + nn3 + nn4 + nn5 + nn6 + nn7 + nn8 + nn9 + nn10

                num_top2 = numero_final2 % 11

                num_a2 = str(num_top2)

                num_b2 = num_a2[-1]
                break

            # verificador1 = num_b
            # verificador2 = num_b2
            

            if num_b == cpf_str[-2] and num_b2 == cpf_str[-1]:
                return True
            else:
                return False



def formatar(cpf):
  #  '146.564.549-74"
  um = cpf[0:3]
  dois = cpf[3:6]
  tres = cpf[6:9]

  qua = cpf[9:11]

  lista = [um, dois, tres]

  componto = ".".join(lista)

  lista = [componto, qua]

  hifen = "-".join(lista)

  print(hifen)

  return hifen