menu = """
Seja muito bem-vindo ao International TK Bank

[d] Depositar
[s] Sacar
[t] Transferir
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES_FREE = 3
ainda_tem = LIMITE_SAQUES_FREE  # Número de saques gratuitos restantes
taxa_saque_extra = 6.5  # Taxa para saques extras

while True:
  
    print(f"Saques gratuitos restantes: {ainda_tem}")
    
    opcao = input(menu).strip().lower()

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("Depósito realizado com sucesso!")
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif valor > 0:
            if ainda_tem > 0:
                # Saque dentro do limite gratuito
                saldo -= valor
                ainda_tem -= 1
                extrato += f"Saque: R$ {valor:.2f}\n"
                print("Saque realizado com sucesso!")
            else:
                # Saque extra com taxa de R$ 6,50
                total_saque = valor + taxa_saque_extra
                if total_saque > saldo:
                    print("Operação falhou! Saldo insuficiente para saque extra.")
                else:
                    saldo -= total_saque
                    extrato += f"Saque Extra: R$ {valor:.2f} + Taxa R$ {taxa_saque_extra:.2f}\n"
                    print(f"Saque extra realizado! Taxa de R$ {taxa_saque_extra:.2f} aplicada.")

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "t":
        valor = float(input("Informe o valor da transferência: "))
        destinatario = input("Transferir para: ").strip()

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor da transferência excede o limite.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Transferência para {destinatario}: R$ {valor:.2f}\n"
            print(f"Transferência de R$ {valor:.2f} para {destinatario} realizada com sucesso!")

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print(extrato if extrato else "Não foram realizadas movimentações.")
        print(f"\nSaldo: R$ {saldo:.2f}")
        print(f"Saques gratuitos restantes: {ainda_tem}")
        print("==========================================")

    elif opcao == "q":
        print("Obrigado por usar o International TK Bank! Até mais.")
        break

    else:
        print("Operação inválida, por favor selecione novamente a opção desejada.")
