# Pedindo o nome do usuário
nome_usuario = input("Qual é o seu nome? ")
print(f"Olá, {nome_usuario}! Seja bem-vindo(a) ao Python.")

# Pedindo um número e convertendo para int
numero_str = input("Digite um número inteiro: ")
numero_int = int(numero_str) # Converte a string para inteiro
print(f"Você digitou o número: {numero_int}")
print(f"O dobro do seu número é: {numero_int * 2}")

# Pedindo um número e convertendo para float
preco_str = input("Digite o preço de um produto (ex: 10.50): ")
preco_float = float(preco_str) # Converte a string para float
print(f"O preço com 10% de desconto é: {preco_float * 0.9}")

