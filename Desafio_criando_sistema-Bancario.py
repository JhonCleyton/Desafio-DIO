conta = input("Digite sua conta: ")
while not conta.isdigit():
    conta = input("Entrada inválida. Digite apenas números por favor: ")
cliente = input("Digite seu nome Completo:")
from datetime import datetime
now = datetime.now()
# tem que formatar a hora para não mostrar vairos centesimos.
formatted_datetime = now.strftime("%d/%m/%y %H:%M:%S")
menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=> """

saldo = 800
limite = 1500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 2

while True:

    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: -R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação inválida! Verifique as opções e tente novamente.")

    elif opcao == "3":
        print(formatted_datetime)
        print(f"\nConta Nº: {conta} - Cliente: {cliente.split()[0]}")
        print("\n********************** EXTRATO *************************")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("\n_____________________ BANCO DIO __________________________")
        print("**Qualquer irregularidade constatada procure o seu gerente")
    

    elif opcao == "0":
         print("Obrigado por usar nosso sistema bancário.Tenha um Exelente dia!")
         break 
else:
 print("Operação inválida, por favor selecione novamente a operação desejada.")