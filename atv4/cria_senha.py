"""Crie um programa que verifique se uma senha é forte.
 Uma senha forte deve ter pelo menos 8 caracteres e conter pelo menos um número. 
 O programa deve continuar pedindo senhas até que uma válida seja inserida ou o usuário digite 'sair'.

"""
print("Verificador de senha forte")
print("A senha deve ter pelo menos 8 caracteres e conter pelo menos um número.")
print("Digite 'sair' para encerrar.\n")

while True:
    senha = input("Digite sua senha: ").strip()

    if senha.lower() == 'sair':
        print("Encerrando...")
        break

    if len(senha) < 8:
        print("Senha fraca: menos de 8 caracteres.")
        continue

    if not any(char.isdigit() for char in senha):
        print("Senha fraca: deve conter pelo menos um número.")
        continue

    print("Senha forte!")
    break