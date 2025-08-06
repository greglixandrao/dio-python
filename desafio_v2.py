menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[cu] Criar usuário
[cc] Criar conta
[lu] Listar usuarios
[lc] Listar contas
[q] Sair

=> """
LIMITE_SAQUES = 3
AGENCIA = "0001"

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
usuarios = []
contas = []

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("Operação realizada.")
    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato

def saque(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques
    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print("Operação realizada.")
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato

def print_extrato(saldo, /, *, extrato):
    print("\n============ EXTRATO BANCÁRIO ==========")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def criar_usuario(usuarios):
    cpf = input("Por favor, informe o CPF (Somente números): ")
    usuario = procurar_usuario(cpf, usuarios)
    if usuario:
        print("Usuário já existe!")
        return

    nome = input("Informe o nome do usuário: ")
    data_nascimento = input("Informe a data de nascimento (dd/mm/aaaa): ")
    endereco = input("Informe o endereço: (logradouro, número, bairro, cidade/estado(sigla)): ")

    usuarios.append({
        "cpf": cpf,
        "nome": nome,
        "data_nascimento": data_nascimento,
        "endereco": endereco
    })
    print("Usuário criado com sucesso!")

def procurar_usuario(cpf, usuarios):
    return next((u for u in usuarios if u['cpf'] == cpf), None)

def criar_conta(usuarios, AGENCIA, contas):
    cpf = input("Informe o CPF do usuário: ")
    usuario = procurar_usuario(cpf, usuarios)

    if usuario:
        numero_conta = len(contas) + 1
        contas.append({"numero": numero_conta, "usuario": usuario})
        print(f"Conta criada com sucesso! Número da conta: {numero_conta}")

    print("Usuário não encontrado. Conta não criada.")

def listar_contas(contas):
    if not contas:
        print("Nenhuma conta cadastrada.")
        return

    print("\n=== Lista de Contas ===")
    for conta in contas:
        print(f"Conta Número: {conta['numero']}, Usuário: {conta['usuario']['nome']} (CPF: {conta['usuario']['cpf']})")
    print("========================")

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        saldo, extrato = depositar(saldo, valor, extrato)

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        saldo, extrato, = saque(
            saldo=saldo,
            valor=valor,
            extrato=extrato,
            limite=limite,
            numero_saques=numero_saques,
            limite_saques=LIMITE_SAQUES,
        )
    elif opcao == "e":
        print_extrato(saldo, extrato=extrato)

    elif opcao == "cu":
        criar_usuario(usuarios)

    elif opcao == "cc":
        criar_conta(usuarios, AGENCIA, contas)

    elif opcao == "lc":
        listar_contas(contas)

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
