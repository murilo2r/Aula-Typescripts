nome = str(input("Digite seu nome: "))
idade = int(input("Digite sua idade: "))

if idade < 18:
    print("Você é menor de idade.")
else:
    print("Você é maior de idade.")

print(F"Olá, {nome}! Você tem {idade} anos.")
print(f"Obrigado por participar da aula!")