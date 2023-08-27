valor_final = 0

print("Bem-vindo a Sorveteria do Matheus Belarmino Pignata!")

# Criação de uma função para a impressão do Cardápio
def Cardapio():
    print('--' * 17,'Cardápio','--' * 17)
    print('|', 'N° DE BOLAS', '|', 'Sabor Tradicional (tr)', '|', 'Sabor Premium (pr)', '|', 'Sabor Especial', '|')
    print('|','     1     ', '|', '      R$ 6,00         ', '|', '      R$ 7,00     ', '|', '   R$ 8,00    ', '|')
    print('|', '     2     ', '|', '      R$ 11,00        ', '|', '      R$ 13,00    ', '|', '   R$ 15,00   ', '|')
    print('|', '     3     ', '|', '      R$ 15,00        ', '|', '      R$ 18,00    ', '|', '   R$ 21,00   ', '|')
    print('--' * 39)

Cardapio()

while True:
    # Entrada de dado do usuario
    sabor = input("Entre com o sabor desejado (tr/pr/es): ")
    
     # Verifica a entrada do usuario
    if sabor not in ['tr', 'pr', 'es']:
        print("Sabor de inválido. Tente novamente")
        continue
    
    if sabor == 'tr':
        sab = 'TRADICIONAL'
    elif sabor == 'pr':
        sab = 'PREMIUM' 
    else:
        sab = 'ESPECIAL'
        
    # Entrada de dado do usuario
    qnt = input("Digite o número de bolas de sorvete desejado (1/2/3): ")
    
    # Verifica a entrada do usuario
    if qnt not in ['1', '2', '3']:
        print("Númeor de bolas de sorvete inválido. Tente novamente")
        continue
    
    # Cálculo do valor
    if qnt == '1':
        if sabor == 'tr':
            valor = 6
        elif sabor == 'pr':
            valor = 7
        else:
            valor = 8
    elif qnt == '2':
        if sabor == 'tr':
            valor = 11
        elif sabor == 'pr':
            valor = 13
        else:
            valor = 15
    else:
        if sabor == 'tr':
            valor = 15
        elif sabor == 'pr':
            valor = 18
        else:
            valor = 21
    
    # Calculo do total       
    valor_final += valor
    
    # Print do pedido
    if qnt == '1':
        print(f"Você pediu {qnt} bola de sorvete no sabor {sab} Valor a pagar: R$ {valor:.2f}")
    else:
        print(f"Você pediu {qnt} bolas de sorvete no sabor {sab} Valor a pagar: R$ {valor:.2f}")
    
    # Verificação se o usuario quer fazer mais um pedido
    continuar = input("Deseja pedir mais alguma coisa? (s/n): ")
    if continuar.lower() != 's':
        print(f"Valor total a ser pago: R$ {valor_final:.2f}")
        break