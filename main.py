import random, string
print("Gerador de Senhas Seguras")

nome = input("Bem-vindo ao Gerador de Senhas Seguras, digite o seu nome usuário: ").upper()

while True:
    print("1 - Gerar nova senha")
    print("2 - Sair")
    
    opcao_usuario = int(input(f"Usuário {nome}, digite a opção desejada: "))

    if opcao_usuario == 1:
        
        caracteres_disponiveis = string.ascii_lowercase
        
        tamanho_senha = int(input(f"Usuário {nome}, digite o tamanho da senha que você deseja gerar (mínimo = 12, máximo = 126): "))
        if tamanho_senha < 12 or tamanho_senha > 126:
            print(f"Usuário {nome}, a senha deve ter no mínimo 12 caracteres e no máximo 126!")
            continue
            
        conter_numeros = input(f"Usuário {nome}, você deseja que sua senha contenha números (Digite S ou N):").upper()
        conter_simbolos = input(f"Usuário {nome}, você deseja que sua senha contenha símbolos (Digite S ou N):").upper()
        conter_letras_maiusculas = input(f"Usuário {nome}, você deseja que sua senha contenha letras maiúsculas (Digite S ou N):").upper()
        
        if conter_numeros == "S":
            caracteres_disponiveis += string.digits
        
        if conter_simbolos == "S":
            caracteres_disponiveis += string.punctuation
        
        if conter_letras_maiusculas == "S":
            caracteres_disponiveis += string.ascii_uppercase
            
        senha = "".join(random.choice(caracteres_disponiveis) for i in range(tamanho_senha))
        
        print(f"Usuário {nome}, a senha gerada foi {senha}")
    
    elif opcao_usuario == 2:
        print(f"Usuário {nome}, obrigado por utilizar nosso Gerador de Senhas Seguras, espero que tenha gostado!")
        break
        
    else:
        print(f"Usuário {nome}, a opção digitada é inválida, tente novamente")