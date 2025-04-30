#desfio de codigos DIO



def calcular_saldo(transacoes):
    saldo = 0

    # Itera sobre cada transação na lista e atualiza o saldo
    for transacao in transacoes:
        saldo += transacao

    # Retorna o saldo formatado no formato esperado
    return f"Saldo: R$ {saldo:.2f}"

# Entrada do usuário (listagem das transações)
entrada_usuario = input()

# Processa a entrada: converte a string para uma lista de floats
entrada_usuario = entrada_usuario.strip("[]").replace(" ", "")  # Remove os colchetes e espaços
transacoes = [float(valor) for valor in entrada_usuario.split(",")]

# Calcula o saldo com base nas transações informadas
resultado = calcular_saldo(transacoes)

# Exibe o saldo final
print(resultado)


Descrição
Imagine que você trabalha no setor de TI de um banco e precisa criar um programa que registre as transações de uma conta bancária. Cada transação pode ser um depósito ou um saque, e todas elas serão armazenadas em uma lista. Seu programa deve calcular o saldo final da conta com base nas transações realizadas. Depósitos serão representados como valores positivos e saques como valores negativos.

Entrada
Uma lista contendo valores inteiros ou decimais representando as transações realizadas (ex.: [100, -50, 200]).

Valores positivos representam depósitos.
Valores negativos representam saques.
Saída
O saldo final da conta no formato: "Saldo: R$ X.XX"

Exemplos
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.