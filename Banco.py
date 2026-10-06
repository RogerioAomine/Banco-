conta= {"titular":"João","saldo":1000,"historico": []
}


def menu(conta):
       print(" ====== BANCO =======\n")
       print("1 - Consultar Saldo")
       print("2 - Depositar")
       print("3 - Sacar")
       print("4 - Histórico")
       print("5 - Sair")
       print("=====================\n")
       while True:
              escolha = int(input("Digite a sua:"))
              if escolha == 1:
                     consultar_saldo(conta)
              elif escolha == 2:
                     Depositar(conta)
              elif escolha == 3:
                     Sacar(conta)
              elif escolha == 4:
                     Historico(conta)
              elif escolha == 5:
                     print("Saindo do programa!")
                     break
              else:
                     print("Opção invalidar!")
                     

def consultar_saldo(conta):
       print(f"Titula:",conta["titular"])
       print(f"Saldo:",conta["saldo"])
       print(f"Historico:",conta["historico"])
       opcao = int(input("Digite 1 para sair, 2 para continua:"))
       if opcao != 1:
              print("Estamos saindo do programa!")
              print("==============================\n")
       
       

def Depositar(conta):
       valor_depositar = int(input("Qual seria o valor a depositar:"))
       if valor_depositar > 0:
              conta["saldo"] += valor_depositar
              conta["historico"].append(valor_depositar)
              print("Valor depositado em sua conta foi:",valor_depositar)
              print("===================================")
       else:
              print("Valor negativo!")

def Sacar(conta):
       valor_sacar = int(input("Quanto deseja retira da sua conta:"))
       if valor_sacar > conta["saldo"] or valor_sacar <= 0:
              print("Saldo insuficiente!")
       else:
              print("O Valor foi retirado da sua conta:",valor_sacar)
              conta["saldo"] -= valor_sacar
              print("Saldo atual:",conta["saldo"])
              conta["historico"].append(valor_sacar)


def Historico(conta):
       if conta["historico"]:
              print("Historico do seu saldo:",conta["historico"])
       else:
              print("Você não teve movimentação de sua conta a um tempo!")
menu(conta)
