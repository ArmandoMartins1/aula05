#minha versão, funcionando
"""pin = 1234
tentativas = 2
senha = int(input("digite a senha: "))
if pin == senha:
    print("logado com sucesso")
while pin != senha:
    senha = int(input(f"você tem mais {tentativas} tentativas\ndigite a senha novamente: "))
    if senha == pin:
        print("logado com sucesso")
    tentativas -= 1
    if tentativas == 0 and pin != senha:
        print(f"Acabou as tentativas, tente novamente mais tarde...")
        break"""
#versão do professor otimizado
pin = 1234
tentativas = 1
mensagem = "Acesso Bloqueado"
while tentativas<=3:
    senha = int(input("Digite a sua senha: "))
    if senha == pin:
        mensagem="Login efetuado com sucesso"
        break
    tentativas+=1
print(mensagem)