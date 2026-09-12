import string
import secrets

azmin = string.ascii_lowercase
azmaius = string.ascii_uppercase
char = string.punctuation
numero = string.digits

char_disponiveis = azmin+azmaius+char+numero

gerar_senha = ""

nome = "DARLAN"

quanti = int(input("Informa o Tamanho da sua SENHA aleátoria por favor: "))

for i in range(quanti):
    escolhido = secrets.choice(nome)
    gerar_senha = gerar_senha + escolhido
print(gerar_senha)