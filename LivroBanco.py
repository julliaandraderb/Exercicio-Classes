# Classe responsável por representar um livro
class livro:
    # Inicializa os dados do livro
    def __init__(self, titulo, autor, numero_paginas):
        self.titulo = titulo
        self.autor = autor
        self.numero_paginas = numero_paginas
        self.pagina_atual = 1  # Define a página inicial

    # Exibe o título do livro e a página atual
    def abrir_livro(self):
        print(f"Livro '{self.titulo}' aberto na página {self.pagina_atual}.")

    # Avança a leitura de acordo com a quantidade informada
    def ler_paginas(self, quantidade):
        if self.pagina_atual == 0:
            print("Abra o livro primeiro!")
        else:
            self.pagina_atual += quantidade

    # Mostra o progresso da leitura
    def exibir_progresso(self):
        lidas = self.pagina_atual
        faltam = self.numero_paginas - self.pagina_atual
        print(f"Páginas lidas: {lidas}")
        print(f"Páginas faltando: {faltam}")


# Classe responsável por representar uma conta bancária
class banco:
    # Inicializa os dados da conta
    def __init__(self, titular, numero_conta, saldo_inicial):
        self.titular = titular
        self.numero_conta = numero_conta
        self.saldo = saldo_inicial

    # Adiciona dinheiro ao saldo quando o valor é positivo
    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor} feito com sucesso.")
        else:
            print("Valor inválido para depósito.")

    # Retira dinheiro quando há saldo suficiente
    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R${valor} realizado.")
        else:
            print("Saldo insuficiente.")

    # Exibe o saldo atual da conta
    def consultar_saldo(self):
        print(f"Saldo atual: R${self.saldo}")

    # Exibe os dados da conta e o saldo
    def exibir_extrato(self):
        print(f"Titular: {self.titular}")
        print(f"Número da Conta: {self.numero_conta}")
        print(f"Saldo: R${self.saldo}")


# Cria um objeto de livro com seus dados
livro1 = livro("O Senhor dos Anéis", "J.R.R. Tolkien", 1000)

# Exibe a página atual do livro
livro1.abrir_livro()

# Cria uma conta com saldo inicial de R$ 1.000
banco1 = banco("João Silva", "123456", 1000)

# Realiza um depósito inicial de R$ 500
banco1.depositar(500)


# Loop do menu interativo do livro
while True:
    print("\n--- MENU DO LIVRO ---")
    print("1. Abrir livro")
    print("2. Ler páginas")
    print("3. Exibir progresso")
    print("4. Sair")

    # Recebe a opção escolhida pelo usuário
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        livro1.abrir_livro()
    elif opcao == "2":
        # Solicita quantas páginas o usuário deseja ler
        quantidade = int(input("Quantas páginas deseja ler? "))
        livro1.ler_paginas(quantidade)
    elif opcao == "3":
        livro1.exibir_progresso()
    elif opcao == "4":
        print("Saindo do menu do livro!")
        break  # Encerra o menu do livro
    else:
        print("Opção inválida!")


# Loop do menu interativo da conta bancária
while True:
    print("\n--- MENU BANCÁRIO ---")
    print("1. Depositar")
    print("2. Sacar")
    print("3. Consultar saldo")
    print("4. Exibir extrato")
    print("5. Sair")

    # Recebe a opção escolhida pelo usuário
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        # Solicita o valor que será depositado
        valor = float(input("Valor do depósito: R$ "))
        banco1.depositar(valor)
    elif opcao == "2":
        # Solicita o valor que será sacado
        valor = float(input("Valor do saque: R$ "))
        banco1.sacar(valor)
    elif opcao == "3":
        banco1.consultar_saldo()
    elif opcao == "4":
        banco1.exibir_extrato()
    elif opcao == "5":
        print("Saindo do menu bancário!")
        break  # Encerra o menu bancário
    else:
        print("Opção inválida!")
