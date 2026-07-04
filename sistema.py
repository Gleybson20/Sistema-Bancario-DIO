def depositar(saldo, extrato, valor):
    if valor > 0:
        saldo += valor
        extrato.append(f"Depósito: R$ {valor:.2f}")
        print(f"\nDepósito de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("\nOperação falhou! O valor informado é inválido.")
    
    return saldo, extrato


def sacar(saldo, extrato, valor, numero_saques, limite_por_saque, limite_saques_diarios):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite_por_saque
    excedeu_saques = numero_saques >= limite_saques_diarios

    if excedeu_saldo:
        print("\nOperação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print(f"\nOperação falhou! O valor do saque excede o limite de R$ {limite_por_saque:.2f} por saque.")
    elif excedeu_saques:
        print("\nOperação falhou! Número máximo de saques diários atingido.")
    elif valor > 0:
        saldo -= valor
        extrato.append(f"Saque: R$ {valor:.2f}")
        numero_saques += 1
        print(f"\nSaque de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("\nOperação falhou! O valor informado é inválido.")

    return saldo, extrato, numero_saques


def exibir_extrato(saldo, extrato):
    print("\nEXTRATO")
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        for transacao in extrato:
            print(transacao)
    print(f"\nSaldo atual: R$ {saldo:.2f}")


def main():
    saldo = 0.0
    limite_por_saque = 500.0
    extrato = []
    numero_saques = 0
    LIMITE_SAQUES_DIARIOS = 3

    while True:
        print("\nMENU")
        print("[1] Depositar")
        print("[2] Sacar")
        print("[3] Extrato")
        print("[0] Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = depositar(saldo, extrato, valor)

        elif opcao == "2":
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato, numero_saques = sacar(
                saldo=saldo,
                extrato=extrato,
                valor=valor,
                numero_saques=numero_saques,
                limite_por_saque=limite_por_saque,
                limite_saques_diarios=LIMITE_SAQUES_DIARIOS
            )

        elif opcao == "3":
            exibir_extrato(saldo, extrato)

        elif opcao == "0":
            print("\nObrigado por utilizar nosso sistema bancário. Até logo!")
            break

        else:
            print("\nOpção inválida, por favor selecione novamente a operação desejada.")

main()