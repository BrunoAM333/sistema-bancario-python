import textwrap

def menu():
    menu = """\n
    ================ MENU ================
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [nu] Novo usuário
    [nc] Nova conta
    [lc] Listar contas
    [q] Sair
    => """
    return input(textwrap.dedent(menu))

def depositar(conta, valor, /):
    if valor > 0:
        conta["saldo"] += valor
        conta["extrato"].append(f"Depósito: R$ {valor:.2f}")
        print("\nDepósito realizado com sucesso!")
    else:
        print("\nOperação falhou! O valor informado é inválido.")
    return conta["saldo"], conta["extrato"]

def sacar(*, conta, valor):
    saldo = conta["saldo"]
    limite = conta["limite"]
    extrato = conta["extrato"]
    numero_saques = conta["numero_saques"]
    limite_saques = conta["limite_saques"]

    if valor > saldo:
        print("\nOperação falhou! Você não tem saldo suficiente.")
    elif valor > limite:
        print("\nOperação falhou! O valor do saque excede o limite.")
    elif numero_saques >= limite_saques:
        print("\nOperação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        conta["saldo"] -= valor
        conta["extrato"].append(f"Saque: R$ {valor:.2f}")
        conta["numero_saques"] += 1
        print("\nSaque realizado com sucesso!")
    else:
        print("\nOperação falhou! O valor informado é inválido.")
    return conta["saldo"], conta["extrato"], conta["numero_saques"]

def exibir_extrato(conta, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else "\n".join(extrato))
    print(f"\nSaldo: R$ {conta['saldo']:.2f}")
    print("==========================================")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF do usuário (somente números): ")
    cpf = "".join(filter(str.isdigit, cpf))

    if any(usuario["cpf"] == cpf for usuario in usuarios):
        print("\nErro! Já existe um usuário com esse CPF.")
        return

    nome = input("Informe o nome completo do usuário: ")
    data_nascimento = input("Informe a data de nascimento (DD-MM-AAAA): ")
    logradouro = input("Informe o logradouro: ")
    nro = input("Informe o número: ")
    bairro = input("Informe o bairro: ")
    cidade_estado = input("Informe a cidade/sigla estado (ex: São Paulo/SP): ")
    endereco = f"{logradouro}, {nro} - {bairro} - {cidade_estado}"

    usuarios.append({"cpf": cpf, "nome": nome, "data_nascimento": data_nascimento, "endereco": endereco, "contas": []})
    print("\nUsuário cadastrado com sucesso!")

def criar_conta_corrente(usuarios, contas):
    cpf = input("Informe o CPF do titular da conta: ")
    usuario = next((usuario for usuario in usuarios if usuario["cpf"] == cpf), None)

    if usuario:
        agencia = "0001"
        if contas:
            numero_conta = str(int(contas[-1]["numero_conta"]) + 1).zfill(len(contas[-1]["numero_conta"]))
        else:
            numero_conta = "1"

        conta = {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario, "saldo": 0, "extrato": [], "limite_saques": 3, "numero_saques": 0, "limite": 500}
        contas.append(conta)
        usuario["contas"].append(conta)
        print("Conta corrente criada com sucesso!")
    else:
        print("Usuário não encontrado!")

def listar_contas(contas):
    if not contas:
        print("\nNão há contas cadastradas.")
        return
    print("\n===== Contas Correntes Cadastradas =====")
    for conta in contas:
        print(f"Agência: {conta['agencia']}")
        print(f"Número da Conta: {conta['numero_conta']}")
        print(f"Titular: {conta['usuario']['nome']}")
        print("--------------------------------------")

def main():
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            numero_conta = input("Informe o número da conta para depósito: ")
            conta = next((conta for conta in contas if conta["numero_conta"] == numero_conta), None)
            if conta:
                valor = float(input("Informe o valor do depósito: "))
                saldo, extrato = depositar(conta, valor)
            else:
                print("\nConta não encontrada!")

        elif opcao == "s":
            numero_conta = input("Informe o número da conta para saque: ")
            conta = next((conta for conta in contas if conta["numero_conta"] == numero_conta), None)
            if conta:
                valor = float(input("Informe o valor do saque: "))
                saldo, extrato, numero_saques = sacar(conta=conta, valor=valor)
                conta["saldo"] = saldo
                conta["extrato"] = extrato
                conta["numero_saques"] = numero_saques
            else:
                print("\nConta não encontrada!")

        elif opcao == "e":
            numero_conta = input("Informe o número da conta para exibir o extrato: ")
            conta = next((conta for conta in contas if conta["numero_conta"] == numero_conta), None)
            if conta:
                exibir_extrato(conta, extrato=conta["extrato"])
            else:
                print("\nConta não encontrada!")

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            criar_conta_corrente(usuarios, contas)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            print("\nObrigado por usar nosso banco. Até logo!")
            break

        else:
            print("\nOperação inválida, por favor selecione novamente a operação desejada.")

if __name__ == "__main__":
    main()