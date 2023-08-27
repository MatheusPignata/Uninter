# Função para obter o peso do cachorro
def cachorro_peso():
    while True:
        try:
            peso = float(input("Digite o peso do cachorro (em kg): "))
            
            if peso < 3:
                return 40
            elif peso < 10:
                return 50
            elif peso < 30:
                return 60
            elif peso < 50:
                return 70
            else:
                print("Não aceitamos cachorros tão grandes (50 kg).")
        except ValueError:
            print("Você digitou um valor não númerico.")

# Função para obter o tipo de pelo do cachorro
def cachorro_pelo():
    while True:
        pelo = input("Digite o tipo de pelo do cachorro\nc - curto\nm - médio\nl - longo\n")
        
        if pelo in ['c', 'm', 'l']:
            if pelo == 'c':
                return 1
            elif pelo == 'm':
                return 1.5
            else:
                return 2
        else:
            print("Opção de pelo inválida. Digite 'c', 'm' ou 'l'.")

# Função para obter os serviços adicionais
def cachorro_extra():
    valor_extra = 0
    
    while True:
        extra = input("Deseja adcionar mais algum serviço?\n1 - Corte de Unhas - R$10,00\n2 - Escovar Dentes - R$12,00\n3 - Limpeza de Orelhas R$15,00\n0 - Não desejo mais nada\n")
        
        if extra == '1':
            valor_extra += 10
        elif extra == '2':
            valor_extra += 12
        elif extra == '3':
            valor_extra += 15
        elif extra == '0':
            return valor_extra
        else:
            print("Opção inválida. Digite '1', '2', '3' ou '0'.")

print("Bem-vindo ao PetShop do Matheus Belarmino Pignata!")

# Chamando as funções
base = cachorro_peso()
multiplicador = cachorro_pelo()
extra = cachorro_extra()

# Calculo do total
total = base * multiplicador + extra

# Print do retorno final
print(f"Valor total a pagar: R$ {total:.2f} (peso: {base} * pelo: {multiplicador} + adicional(is): {extra})")