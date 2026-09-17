usuario = "admin"
senha = "python"

for i in range(3):
    acesso_usuario = input("Informe seu usuário: ")
    acesso_senha = input("Informe sua senha: ")
    
    if acesso_usuario == usuario and acesso_senha == senha:
        print("Acesso Liberado!")
        break
    elif acesso_usuario != usuario and acesso_senha == senha:
        print("Usuário incorreto")
    elif acesso_usuario == usuario and acesso_senha != senha:
        print("Senha incorreta")
    elif acesso_usuario != usuario and acesso_senha != senha:
        print("Usuário e senha incorretos")
else:
    print("Acesso Bloqueado!")