from coleta import nome, idade, pedir_email, cpf

def main():
    nome_usuario = nome()
    idade_usuario = idade()
    email_usuario = pedir_email()
    cpf_usuario = cpf()

    usuario = {
        "nome": nome_usuario,
        "idade": idade_usuario,
        "email": email_usuario,
        "cpf": cpf_usuario
    }

    print(usuario)


if __name__ == "__main__":
    main()