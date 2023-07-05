import banco

print("""Seja bem vindo ao Banco!! 
Qual operação de seja realizar hoje?
 1 - Sacar
 2 - Depositar
 3 - Extrato
 4 - sair
 """)
opção = int(input("Digite a sua opção:\n"))
if opção == 1:
    banco.saque()
elif opção == 2:
    banco.deposito()
elif opção == 3:
    banco.extrato()
elif opção == 4:
    print(""" Obrigada por utilizar os nosssos serviços.
    Tenha um bom dia! """)
else:
    print("Opção inválida!")

