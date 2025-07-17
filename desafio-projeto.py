#! /usr/bin/env python3

"""Desafio Projeto - Sistema Bancário Simples
Este script implementa um sistema bancário simples que permite depósitos, saques e exibição de extrato.
"""
__author__ = "Greg Lixandrão"
__version__ = "1.0.0"

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu).lower()

    if opcao =="d":
        deposito = float(input("Informe o valor do depósito: R$ "))

        if deposito > 0:
            saldo += deposito
            extrato += f"Depósito: R$ {deposito:.2f}\n"
            print(f"Depósito de R$ {deposito:.2f} realizado com sucesso!")
        else:
            print("Valor inválido. Por favor, insira um número positivo.")

    elif opcao == "s":
        try:
            saque = float(input("Informe o valor de saque (R$): "))
        except ValueError:
            print("Valor inválido. Por favor, insira um número válido.")
            continue
        if saque > saldo:
            print("Saldo insuficiente para realizar o saque.")
        elif saque > limite:
            print(f"Valor do saque excede o limite de R$ {limite:.2f}.")
        elif numero_saques >= LIMITE_SAQUES:
            print(f"Limite de saques diários atingido - ({LIMITE_SAQUES} saques).")
        elif saque <= 0:
            print("Valor inválido. Por favor, insira um número positivo.")
        else:
            saldo -= saque
            extrato += f"Saque: R$ {saque:.2f}\n"
            numero_saques += 1
            print(f"Saque de R$ {saque:.2f} realizado com sucesso!")


    elif opcao == "e":
        print("\n================ EXTRATO BANCÀRIO ================")
        print("Nenhuma movimentação realizada!." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("====================================================")


    elif opcao == "q":
        print("Saindo...")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
