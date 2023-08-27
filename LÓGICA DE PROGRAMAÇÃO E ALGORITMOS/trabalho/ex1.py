print ('Bem-vindo a Loja do Matheus Belarmino Pignata!')

# Solicita os valores do usuário
valor = float(input("Digite o valor unitário do produto: "))
quantidade = int(input("Digite a quantidade de produtos: "))

# Calcula o valor total sem desconto
valor_total = valor * quantidade

# Calcula o valor com desconto
if quantidade < 200:
    valor_desconto = valor_total
elif quantidade < 1000:
    valor_desconto = valor_total * 0.95
elif quantidade < 2000:
    valor_desconto = valor_total * 0.90
else:
    valor_desconto = valor_total * 0.85

# Exibe os resultados
print(f"Valor total sem desconto: R$ {valor_total:.2f}")
print(f"Valor total com desconto: R$ {valor_desconto:.2f}")