import textwrap

class Cliente:
    def __init__(self, cpf, nome, data_nascimento, endereco):
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.endereco = endereco
        self.contas = []

    def adicionar_conta(self, conta):
        self.contas.append(conta)


class ContaCorrente:
    LIMITE_SAQUES = 3
    LIMITE_VALOR_SAQUE = 500.0

    def __init__(self, agencia, numero, cliente):
        self.agencia = agencia
        self.numero = numero
        self.cliente = cliente
        self.saldo = 0.0
        self.extrato = []
        self.numero_saques = 0

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato.append(f"Depósito: R$ {valor:.2f}")
            print("\nDepósito realizado com sucesso!")
        else:
            print("\nOperação falhou! O valor informado é inválido.")

    def sacar(self, valor):
        if valor > self.saldo:
            print("\nOperação falhou! Você não tem saldo suficiente.")
        elif valor > self.LIMITE_VALOR_SAQUE:
            print("\nOperação falhou! O valor do saque excede o limite.")
        elif self.numero_saques >= self.LIMITE_SAQUES:
            print("\nOperação falhou! Número máximo de saques excedido.")
        elif valor > 0:
            self.saldo -= valor
            self.extrato.append(f"Saque: R$ {valor:.2f}")
            self.numero_saques += 1
            print("\nSaque realizado com sucesso!")
        else:
            print("\nOperação falhou! O valor informado é inválido.")

    def exibir_extrato(self):
        print("\n================ EXTRATO ================")
        if not self.extrato:
            print("Não foram realizadas movimentações.")
        else:
            print("\n".join(self.extrato))
        print(f"\nSaldo: R$ {self.saldo:.2f}")
        print("==========================================")


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

def criar_usuario(clientes):
    cpf = input("Informe o CPF do usuário (somente números): ")
    cpf = "".join(filter(str.isdigit, cpf))

    if any(c.cpf == cpf for c in clientes):
        print("\nErro! Já existe um usuário com esse CPF.")
        return

    nome = input("Informe o nome completo do usuário: ")
    data_nascimento = input("Informe a data de nascimento (DD-MM-AAAA): ")
    logradouro = input("Informe o logradouro: ")
    nro = input("Informe o número: ")
    bairro = input("Informe o bairro: ")
    cidade_estado = input("Informe a cidade/sigla estado (ex: São Paulo/SP): ")
    endereco = f"{logradouro}, {nro} - {bairro} - {cidade_estado}"

    cliente = Cliente(cpf, nome, data_nascimento, endereco)
    clientes.append(cliente)
    print("\nUsuário cadastrado com sucesso!")

def criar_conta_corrente(clientes, contas):
    cpf = input("Informe o CPF do titular da conta: ")
    cliente = next((c for c in clientes if c.cpf == cpf), None)

    if cliente:
        agencia = "0001"
        numero = str(len(contas) + 1).zfill(4)
        conta = ContaCorrente(agencia, numero, cliente)
        cliente.adicionar_conta(conta)
        contas.append(conta)
        print("\nConta corrente criada com sucesso!")
    else:
        print("\nUsuário não encontrado!")

def listar_contas(contas):
    if not contas:
        print("\nNão há contas cadastradas.")
        return
    print("\n===== Contas Correntes Cadastradas =====")
    for conta in contas:
        print(f"Agência: {conta.agencia}")
        print(f"Número da Conta: {conta.numero}")
        print(f"Titular: {conta.cliente.nome}")
        print("--------------------------------------")

def encontrar_conta(numero_conta, contas):
    return next((c for c in contas if c.numero == numero_conta), None)

def main():
    clientes = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            numero = input("Informe o número da conta para depósito: ")
            conta = encontrar_conta(numero, contas)
            if conta:
                valor = float(input("Informe o valor do depósito: "))
                conta.depositar(valor)
            else:
                print("\nConta não encontrada!")

        elif opcao == "s":
            numero = input("Informe o número da conta para saque: ")
            conta = encontrar_conta(numero, contas)
            if conta:
                valor = float(input("Informe o valor do saque: "))
                conta.sacar(valor)
            else:
                print("\nConta não encontrada!")

        elif opcao == "e":
            numero = input("Informe o número da conta para exibir o extrato: ")
            conta = encontrar_conta(numero, contas)
            if conta:
                conta.exibir_extrato()
            else:
                print("\nConta não encontrada!")

        elif opcao == "nu":
            criar_usuario(clientes)

        elif opcao == "nc":
            criar_conta_corrente(clientes, contas)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            print("\nObrigado por usar nosso banco. Até logo!")
            break

        else:
            print("\nOperação inválida, por favor selecione novamente a operação desejada.")

if __name__ == "__main__":
    main()
