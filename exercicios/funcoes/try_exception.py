def cadastro():
    while True:
        try:
            nome = int(input("Nome: "))
            return nome
        except ValueError:
            print("O valor informado está incorreto.")


nome = cadastro()
print(nome)