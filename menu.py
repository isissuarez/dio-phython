

saldo = 500
limite_saques_valor = 500
extrato = list(


)
numero_saques = 0
limite_saques = 3

extrato.append(saldo)
print(extrato)

def deposito():
    global saldo
    global  extrato
    valor = int(input("digíte o valor que deseja depositar"))
    if valor > 0:
        saldo = saldo + valor
        print("deposito realizado com sucesso")
        extrato.append(valor)
        extrato.append(saldo)
        
    else:
        print("valor inválido")
       
def saque():
    global saldo
    global limite_saques
    global  extrato
    valor = int(input("digite o valor que deseja sacar\n"))
    if(saldo > 0 and valor < 500):
        if(limite_saques > 0):
            limite_saques = limite_saques - 1
            saldo = saldo - valor
            print("saque efetuado com sucesso! \n")
            extrato.append(saldo)
            extrato.append(valor)
           
    elif(saldo <= 0):
        print("Você não possui saldo em conta para efetuar esta operação")
        
    elif(valor > 500):
        print("seu limite de saque diário é de 500,00\n")

def mostra_extrato():

     print(f'{extrato}')



