import random

# Pedir ao usuário para especificar o intervalo de números
inicio = int(input("Digite o número inicial do intervalo: "))
fim = int(input("Digite o número final do intervalo: "))

# Gerar um número aleatório dentro do intervalo especificado
numero_sorteado = random.randint(inicio, fim)

# Exibir o número sorteado
print("O número sorteado foi:", numero_sorteado)
